// AlunUÉ research kit: standard browser APIs, no requests, analytics or third-party scripts.
// SUS scoring: Brooke (1996); Portuguese item wording: Martins et al. (2015),
// https://doi.org/10.1016/j.procs.2015.09.273 (article CC BY-NC-ND 4.0).
export const SCHEMA = 'alunue-research/1';
const STORAGE_KEY = 'alunue-research-consented-v1';
const MAX_SESSIONS = 50;
export const TASKS = [
  ['T1', 'Escolher sem localização', 'Sem permitir localização, escolhe um início manual e explica a diferença entre candidato, demonstração e ponto confirmado.'],
  ['T2', 'Preparar duas paragens', 'Ativa a demonstração identificada, escolhe duas paragens fictícias e altera a ordem. Confirma que os exemplos não garantem água real.'],
  ['T3', 'Ajustar o percurso', 'Acrescenta um supermercado e um local cultural da demonstração. Retira uma extensão e explica o que muda no plano.'],
  ['T4', 'Reconhecer uma falha', 'Com uma falha de serviço preparada pelo moderador, identifica a mensagem, a data dos dados e o que ainda consegues consultar.'],
  ['T5', 'Guardar uma alternativa', 'Exporta todas as paragens ou guarda o itinerário em texto. Não é preciso iniciar uma deslocação nem abrir um percurso real.'],
  ['T6', 'Compreender uma sugestão', 'Prepara uma sugestão sem nomes nem contactos e explica onde fica guardada e se alguém é contactado automaticamente.']
];
export const SUS_ITEMS = [
  'Acho que gostaria de utilizar este produto com frequência.',
  'Considerei o produto mais complexo do que necessário.',
  'Achei o produto fácil de utilizar.',
  'Acho que necessitaria de ajuda de um técnico para conseguir utilizar este produto.',
  'Considerei que as várias funcionalidades deste produto estavam bem integradas.',
  'Achei que este produto tinha muitas inconsistências.',
  'Suponho que a maioria das pessoas aprenderia a utilizar rapidamente este produto.',
  'Considerei o produto muito complicado de utilizar.',
  'Senti-me muito confiante a utilizar este produto.',
  'Tive que aprender muito antes de conseguir lidar com este produto.'
];
const DISCOVERY_FIELDS = ['waterFrequency', 'easeLast', 'changedRoute', 'usualContext', 'reusableBottle', 'lastExperience', 'currentApproach', 'difficulties', 'trustInformation', 'routeDecisions', 'costAccess', 'proposalReaction', 'reservations'];
const DISCOVERY_LABELS = ['Procura de água nas últimas duas semanas', 'Facilidade no último episódio', 'Mudança de percurso', 'Contexto do episódio', 'Garrafa reutilizável nas últimas duas semanas', 'Última experiência', 'Recursos usados', 'Dificuldades ou ausência de problema', 'Informação de confiança', 'Decisões sobre paragens', 'Custo, acesso e pagamento', 'Utilidade e ausência de utilidade', 'Reservas e alternativas'];
const STATUSES = ['', 'concluida', 'com-ajuda', 'nao-concluida', 'nao-tentada'];
const STATUS_LABELS = ['Não registado', 'Concluída sem ajuda', 'Concluída com ajuda', 'Não concluída', 'Não tentada'];
const text = (value, max = 1800) => typeof value === 'string' ? value.slice(0, max) : '';
const enumValue = (value, options) => options.includes(value) ? value : '';
const optionalInt = (value, max) => value === null || value === '' || value === undefined ? null : Number.isInteger(Number(value)) && Number(value) >= 0 && Number(value) <= max ? Number(value) : null;

export function scoreSus(values) {
  if (!Array.isArray(values) || values.length !== 10 || values.some(v => !Number.isInteger(v) || v < 1 || v > 5)) return null;
  return values.reduce((sum, value, index) => sum + (index % 2 === 0 ? value - 1 : 5 - value), 0) * 2.5;
}

export function csvCell(value) {
  let safe = value === null || value === undefined ? '' : String(value);
  // Spreadsheet applications may execute a cell beginning with a formula marker.
  if (/^[\s]*[=+\-@]/.test(safe) || /^[\t\r\n]/.test(safe)) safe = `'${safe}`;
  return `"${safe.replaceAll('"', '""')}"`;
}

function isDate(value) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value || '')) return false;
  const d = new Date(`${value}T12:00:00Z`);
  return Number.isFinite(d.valueOf()) && d.toISOString().slice(0, 10) === value;
}

export function validateSession(raw) {
  if (!raw || typeof raw !== 'object' || Array.isArray(raw) || raw.schema !== SCHEMA) throw new Error('Formato de sessão incompatível.');
  if (raw.consent !== true) throw new Error('A sessão não tem autorização de participação registada.');
  if (!['discovery', 'usability'].includes(raw.kind)) throw new Error('Tipo de sessão inválido.');
  if (!/^R-[A-Za-z0-9-]{8,60}$/.test(raw.id || '')) throw new Error('Código de sessão inválido.');
  if (!isDate(raw.date)) throw new Error('Data da sessão inválida.');
  const context = raw.context || {}, answers = raw.discovery || {};
  const sus = Array.from({ length: 10 }, (_, i) => Number.isInteger(raw.sus?.[i]) && raw.sus[i] >= 1 && raw.sus[i] <= 5 ? raw.sus[i] : null);
  // Whitelist fields. Imported HTML is never rendered as HTML, and unknown data is discarded.
  return {
    schema: SCHEMA, id: raw.id, kind: raw.kind, date: raw.date, consent: true,
    recordedAt: typeof raw.recordedAt === 'string' && Number.isFinite(Date.parse(raw.recordedAt)) ? raw.recordedAt : null,
    context: {
      ueStudent: enumValue(context.ueStudent, ['sim', 'nao', '']),
      profile: enumValue(context.profile, ['primeiro-ano', 'internacional', 'trabalhador', 'outro', '']),
      device: enumValue(context.device, ['telemovel', 'computador', 'tablet', 'papel', '']),
      prototype: text(context.prototype, 100)
    },
    discovery: Object.fromEntries(DISCOVERY_FIELDS.map(k => [k, text(answers[k])])),
    tasks: TASKS.map(([id]) => {
      const task = Array.isArray(raw.tasks) ? raw.tasks.find(t => t?.id === id) || {} : {};
      return { id, status: enumValue(task.status, STATUSES), seconds: optionalInt(task.seconds, 36000), errors: optionalInt(task.errors, 999), notes: text(task.notes, 1200) };
    }),
    sus, susScore: raw.kind === 'usability' ? scoreSus(sus) : null,
    debrief: text(raw.debrief), moderatorNotes: text(raw.moderatorNotes)
  };
}

export function summariseSessions(sessions) {
  const usability = sessions.filter(s => s.kind === 'usability');
  const completeSus = usability.map(s => scoreSus(s.sus)).filter(s => s !== null);
  const attempted = usability.flatMap(s => s.tasks).filter(t => ['concluida', 'com-ajuda', 'nao-concluida'].includes(t.status));
  const unaided = attempted.filter(t => t.status === 'concluida').length;
  return { count: sessions.length, usability: usability.length, ueUsability: usability.filter(s => s.context.ueStudent === 'sim').length, completeSus: completeSus.length, meanSus: completeSus.length ? completeSus.reduce((a, b) => a + b, 0) / completeSus.length : null, attempted: attempted.length, unaided, unaidedRate: attempted.length ? unaided / attempted.length * 100 : null };
}

export function sessionsCsv(sessions) {
  const headers = ['sessao_id', 'tipo', 'data', 'consentimento', 'ue_estudante', 'perfil', 'dispositivo', 'prototipo', ...DISCOVERY_FIELDS, ...TASKS.flatMap(([id]) => [`${id}_estado`, `${id}_segundos`, `${id}_erros`, `${id}_notas`]), ...SUS_ITEMS.map((_, i) => `SUS_${i + 1}`), 'SUS_total_0_100', 'conversa_final', 'notas_moderador'];
  const rows = sessions.map(s => [s.id, s.kind, s.date, s.consent, s.context.ueStudent, s.context.profile, s.context.device, s.context.prototype, ...DISCOVERY_FIELDS.map(k => s.discovery[k]), ...s.tasks.flatMap(t => [t.status, t.seconds, t.errors, t.notes]), ...s.sus, s.susScore, s.debrief, s.moderatorNotes]);
  return '\uFEFF' + [headers, ...rows].map(row => row.map(csvCell).join(';')).join('\r\n');
}

function boot() {
  const $ = id => document.getElementById(id);
  const form = $('session-form');
  let sessions = [];
  let draftId = makeId();
  function makeId() {
    if (crypto.randomUUID) return `R-${crypto.randomUUID()}`;
    return 'R-' + Array.from(crypto.getRandomValues(new Uint8Array(16)), b => b.toString(16).padStart(2, '0')).join('');
  }
  function localDate() { const date = new Date(); return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`; }
  function node(tag, className, content) { const el = document.createElement(tag); if (className) el.className = className; if (content !== undefined) el.textContent = content; return el; }
  function labelSelect(parent, labelText, name, options) {
    const label = node('label', '', labelText), select = document.createElement('select'); select.name = name;
    options.forEach(([value, caption]) => { const option = node('option', '', caption); option.value = value; select.append(option); }); label.append(select); parent.append(label); return select;
  }
  function labelInput(parent, caption, name, max) { const label = node('label', '', caption), input = document.createElement('input'); input.type = 'number'; input.name = name; input.min = 0; input.max = max; input.step = 1; label.append(input); parent.append(label); }
  TASKS.forEach(([id, title, instruction]) => {
    const item = node('section', 'task'); item.append(node('h3', '', `${id} · ${title}`), node('p', '', instruction));
    const grid = node('div', 'grid three'); labelSelect(grid, 'Resultado observado', `${id}_status`, STATUSES.map((s, i) => [s, STATUS_LABELS[i]])); labelInput(grid, 'Tempo medido em segundos', `${id}_seconds`, 36000); labelInput(grid, 'Erros observados', `${id}_errors`, 999); item.append(grid);
    const label = node('label', '', 'Observação / ajuda / motivo de não tentativa'), area = document.createElement('textarea'); area.name = `${id}_notes`; area.maxLength = 1200; label.append(area); item.append(label); $('tasks').append(item);
  });
  SUS_ITEMS.forEach((caption, index) => {
    const row = node('div', 'sus-row'), label = node('label', '', `${index + 1}. ${caption}`), select = document.createElement('select'); select.id = `sus-${index + 1}`; select.name = `sus${index + 1}`; label.htmlFor = select.id;
    [['', 'Sem resposta'], ['1', '1 · Discordo totalmente'], ['2', '2 · Discordo'], ['3', '3 · Nem concordo nem discordo'], ['4', '4 · Concordo'], ['5', '5 · Concordo totalmente']].forEach(([value, title]) => { const option = node('option', '', title); option.value = value; select.append(option); }); row.append(label, select); $('sus-items').append(row);
  });
  $('session-date').value = localDate();
  $('session-date').max = localDate();
  $('kind').addEventListener('change', () => {
    const discovery = $('kind').value === 'discovery';
    $('discovery-panel').hidden = !discovery; $('discovery-panel').disabled = !discovery;
    $('usability-panel').hidden = discovery; $('usability-panel').disabled = discovery;
  });
  function readForm() {
    const data = new FormData(form), get = k => String(data.get(k) || '');
    return validateSession({ schema: SCHEMA, id: draftId, kind: get('kind'), date: get('date'), recordedAt: new Date().toISOString(), consent: data.get('consent') === 'on', context: Object.fromEntries(['ueStudent', 'profile', 'device', 'prototype'].map(k => [k, get(k)])), discovery: Object.fromEntries(DISCOVERY_FIELDS.map(k => [k, get(k)])), tasks: TASKS.map(([id]) => ({ id, status: get(`${id}_status`), seconds: get(`${id}_seconds`), errors: get(`${id}_errors`), notes: get(`${id}_notes`) })), sus: SUS_ITEMS.map((_, i) => get(`sus${i + 1}`) === '' ? null : Number(get(`sus${i + 1}`))), debrief: get('debrief'), moderatorNotes: get('moderatorNotes') });
  }
  function storedSessions() {
    const raw = localStorage.getItem(STORAGE_KEY); if (!raw) return [];
    const parsed = JSON.parse(raw); if (!Array.isArray(parsed) || parsed.length > MAX_SESSIONS) throw new Error('Cópias locais inválidas.'); return parsed.map(validateSession);
  }
  function merge(incoming) {
    const newIds = new Set(incoming.filter(s => !sessions.some(saved => saved.id === s.id)).map(s => s.id));
    if (sessions.length + newIds.size > MAX_SESSIONS) throw new Error('Limite de 50 sessões nesta página. Exporta os dados antes de continuar.');
    let added = 0, duplicates = 0;
    for (const session of incoming) { if (sessions.some(s => s.id === session.id)) { duplicates++; continue; } sessions.push(session); added++; }
    render(); return { added, duplicates };
  }
  async function exportFile(filename, content, mime) {
    if(window.AlunUENative?.saveText){try{await window.AlunUENative.saveText(content,filename);$('analysis-status').textContent='Ficheiro preparado para partilha. Escolhe o destino; as respostas continuam apenas no dispositivo até partilhares.';}catch{$('analysis-status').textContent='Não foi possível partilhar o ficheiro. As sessões continuam abertas nesta página.';}return;}
    const url = URL.createObjectURL(new Blob([content], { type: mime })); const anchor = node('a'); anchor.href = url; anchor.download = filename; document.body.append(anchor); anchor.click(); anchor.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  function metric(title, value, detail) { const box = node('div', 'metric'); box.append(node('strong', '', value), node('p', '', title), node('span', '', detail)); return box; }
  function render() {
    const info = summariseSessions(sessions); $('session-count').textContent = `${info.count} ${info.count === 1 ? 'sessão' : 'sessões'}`;
    $('export-json').disabled = $('export-csv').disabled = !sessions.length;
    $('summary').replaceChildren(); $('session-list').replaceChildren();
    if (!sessions.length) { $('summary').append(node('p', 'empty', 'Ainda não há sessões. Sem dados, não há taxas, médias SUS ou conclusões a mostrar.')); return; }
    $('summary').append(metric('Sessões registadas', String(info.count), `${info.usability} de usabilidade; ${info.ueUsability} indicam vínculo à UÉ. Sessões não equivalem a pessoas distintas.`), metric('SUS completos', info.meanSus === null ? '—' : info.meanSus.toFixed(1).replace('.', ','), info.meanSus === null ? 'Sem questionários completos. Não se substituem respostas em falta.' : `Média de ${info.completeSus} questionário(s), escala 0–100. Não é uma percentagem.`), metric('Tarefas sem ajuda', info.unaidedRate === null ? '—' : `${Math.round(info.unaidedRate)}%`, info.attempted ? `${info.unaided} de ${info.attempted} tentativas. Não tentadas e não registadas excluídas.` : 'Sem tarefas observadas com resultado registado.'));
    sessions.forEach(session => {
      const card = node('details', 'session-card'), heading = node('summary', '', `${session.kind === 'discovery' ? 'Descoberta' : 'Usabilidade'} · ${session.date} · ${session.id.slice(0, 10)}…`), dl = node('dl'); card.append(heading);
      const add = (title, value) => { dl.append(node('dt', '', title), node('dd', '', value || 'Não registado')); };
      add('Código completo', session.id); add('Vínculo UÉ', session.context.ueStudent || 'Não indicado'); add('Perfil / dispositivo', [session.context.profile, session.context.device].filter(Boolean).join(' / ')); add('Protótipo', session.context.prototype);
      if (session.kind === 'discovery') DISCOVERY_FIELDS.forEach((k, i) => add(DISCOVERY_LABELS[i], session.discovery[k]));
      else { session.tasks.forEach(task => add(task.id, `${STATUS_LABELS[STATUSES.indexOf(task.status)]}; tempo: ${task.seconds ?? 'não medido'}; erros: ${task.errors ?? 'não registados'}. ${task.notes}`)); add('SUS 1–10', session.sus.map(v => v ?? '—').join(' / ')); add('SUS total', session.susScore === null ? 'Incompleto; não calculado.' : `${session.susScore} / 100`); add('Conversa final', session.debrief); }
      add('Notas', session.moderatorNotes); card.append(dl);
      const remove = node('button', '', 'Retirar desta análise'); remove.type = 'button'; remove.addEventListener('click', () => { sessions = sessions.filter(s => s.id !== session.id); render(); $('analysis-status').textContent = 'Sessão retirada da memória desta página. Ficheiros e cópias no navegador não foram alterados.'; }); card.append(remove); $('session-list').append(card);
    });
  }
  form.addEventListener('submit', event => {
    event.preventDefault(); if (!form.reportValidity()) return;
    try {
      const session = readForm();
      if (sessions.some(s => s.id === session.id)) { $('form-status').textContent = 'Esta sessão já está registada. Limpa o formulário antes de iniciar uma pessoa/sessão diferente.'; return; }
      merge([session]);
      let stored = false;
      if (form.elements.saveLocal.checked) { const existing = storedSessions(); if (!existing.some(s => s.id === session.id)) { if (existing.length >= MAX_SESSIONS) throw new Error('Sessão registada na página, mas o navegador já tem 50 cópias. Exporta e revê antes de apagar.'); existing.push(session); localStorage.setItem(STORAGE_KEY, JSON.stringify(existing)); } stored = true; }
      $('form-status').textContent = `Sessão registada. ${stored ? 'Cópia guardada neste navegador por escolha explícita.' : 'Só está na memória desta página: descarrega o JSON antes de fechar.'} ${session.kind === 'usability' && session.susScore === null ? 'SUS incompleto; não foi calculado.' : ''}`;
    } catch (error) { $('form-status').textContent = `Não foi possível concluir: ${error.message}`; }
  });
  $('reset-session').addEventListener('click', () => { form.reset(); $('session-date').value = localDate(); $('kind').dispatchEvent(new Event('change')); draftId = makeId(); $('form-status').textContent = 'Formulário limpo. As sessões já registadas na análise não foram apagadas.'; $('consent').focus(); });
  $('import-files').addEventListener('change', async event => {
    if (!$('import-consent').checked) { $('analysis-status').textContent = 'Confirma a autorização e a origem real das sessões antes de importar.'; event.target.value = ''; return; }
    try {
      const pending = [];
      for (const file of event.target.files) { if (file.size > 2 * 1024 * 1024) throw new Error('Um ficheiro excede 2 MB.'); const raw = JSON.parse(await file.text()), records = Array.isArray(raw.sessions) ? raw.sessions : [raw]; if (records.length > MAX_SESSIONS) throw new Error('Um conjunto excede 50 sessões.'); records.forEach(rawSession => pending.push(validateSession(rawSession))); }
      const uniqueNew = new Set(pending.filter(s => !sessions.some(saved => saved.id === s.id)).map(s => s.id));
      if (sessions.length + uniqueNew.size > MAX_SESSIONS) throw new Error('A importação ultrapassaria 50 sessões. Nada foi importado.');
      const result = merge(pending); $('analysis-status').textContent = `${result.added} sessão(ões) importada(s); ${result.duplicates} identificador(es) repetido(s) ignorado(s). Origem declarada pelo autor; sem autenticação independente.`;
    } catch (error) { $('analysis-status').textContent = `Importação recusada: ${error.message}`; }
    event.target.value = '';
  });
  $('load-local').addEventListener('click', () => { try { const result = merge(storedSessions()); $('analysis-status').textContent = `${result.added} cópia(s) local(is) carregada(s); ${result.duplicates} repetida(s) ignorada(s).`; } catch (error) { $('analysis-status').textContent = `Não foi possível ler as cópias locais: ${error.message}`; } });
  $('clear-local').addEventListener('click', () => { if (!window.confirm('Apagar apenas as cópias de investigação guardadas por este kit neste navegador? Os ficheiros descarregados e a análise aberta não serão apagados.')) return; try { localStorage.removeItem(STORAGE_KEY); $('analysis-status').textContent = 'Cópias deste kit apagadas do navegador. Verifica também os ficheiros descarregados num dispositivo partilhado.'; } catch { $('analysis-status').textContent = 'O navegador não permitiu apagar as cópias locais.'; } });
  $('clear-memory').addEventListener('click', () => { if (!sessions.length || window.confirm('Limpar as sessões abertas nesta página? Descarrega o JSON primeiro se quiseres conservar os dados.')) { sessions = []; render(); $('analysis-status').textContent = 'Memória desta página limpa. Cópias no navegador e ficheiros descarregados não foram alterados.'; } });
  $('export-json').addEventListener('click', () => exportFile(`alunue-sessoes-${localDate()}.json`, JSON.stringify({ schema: SCHEMA, exportedAt: new Date().toISOString(), provenance: 'Sessões fornecidas pelo autor; a importação não autentica participantes ou respostas.', sessions }, null, 2), 'application/json;charset=utf-8'));
  $('export-csv').addEventListener('click', () => exportFile(`alunue-sessoes-${localDate()}.csv`, sessionsCsv(sessions), 'text/csv;charset=utf-8'));
  $('print').addEventListener('click', () => { document.querySelectorAll('.session-card').forEach(card => { card.open = true; }); window.print(); });
  render();
}

if (typeof document !== 'undefined') boot();
