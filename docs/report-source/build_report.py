from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import json
from visual_components import RouteVisual, EvidenceVisual, PersonaCards, EmpathyVisual, paint_page

ROOT=Path(__file__).parent
OUT=ROOT/'output'; OUT.mkdir(exist_ok=True)
pdfmetrics.registerFont(TTFont('Arial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold','C:/Windows/Fonts/arialbd.ttf'))
GREEN=HexColor('#17493e'); LIGHT=HexColor('#edf3eb'); INK=HexColor('#233a34'); MUTED=HexColor('#52665e')
styles=getSampleStyleSheet()
for name in ['Normal','BodyText']: styles[name].fontName='Arial'; styles[name].fontSize=10; styles[name].leading=14; styles[name].textColor=INK
styles.add(ParagraphStyle(name='TitlePT',fontName='ArialBold',fontSize=30,leading=34,textColor=GREEN,spaceAfter=18))
styles.add(ParagraphStyle(name='H1PT',fontName='ArialBold',fontSize=22,leading=26,textColor=GREEN,spaceAfter=15))
styles.add(ParagraphStyle(name='H2PT',fontName='ArialBold',fontSize=11.5,leading=15,textColor=GREEN,spaceBefore=12,spaceAfter=6))
styles.add(ParagraphStyle(name='SmallPT',fontName='Arial',fontSize=8.7,leading=12,textColor=MUTED))
story=[]; text_source=[]
def p(t,style='BodyText'):
    story.append(Paragraph(t,styles[style]));story.append(Spacer(1,7));text_source.append(t)
def h(t): p(t,'H2PT')
def title(n,t):
    if story: story.append(PageBreak())
    p('ALUNUÉ / FASE 1 / '+n,'SmallPT');p(t,'H1PT')
def table(rows,widths=None):
    text_source.append('\n'.join(' | '.join(map(str,r)) for r in rows))
    if rows[0][0] in ['Perfil / base','Profile / basis']:
        story.append(PersonaCards(rows[1:]));story.append(Spacer(1,9));return
    if rows[0][0] in ['Dimensão','Dimension'] and len(rows)==5:
        story.append(EmpathyVisual(rows[1:]));story.append(Spacer(1,5));return
    header_style=ParagraphStyle('whitehead',parent=styles['SmallPT'],textColor=white,fontName='ArialBold')
    cells=[[Paragraph(escape(str(c)).replace('\n','<br/>'),header_style if i==0 else styles['SmallPT']) for c in row] for i,row in enumerate(rows)]
    t=Table(cells,colWidths=widths or [165,330],hAlign='LEFT')
    commands=[('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('BACKGROUND',(0,0),(-1,0),GREEN),('LINEBELOW',(0,0),(-1,-1),.3,HexColor('#DDE5DC'))]
    for row in range(1,len(rows)):commands.append(('BACKGROUND',(0,row),(-1,row),HexColor('#EDF3EA') if row%2 else HexColor('#FFFFFF')))
    t.setStyle(TableStyle(commands));story.append(t);story.append(Spacer(1,9))
class Diagram(RouteVisual):
    pass

p('INTERAÇÃO PESSOA-MÁQUINA · INF13186L','SmallPT')
p('AlunUÉ<br/>Água pelo caminho','TitlePT')
p('Investigação exploratória e requisitos para descobrir pontos de reabastecimento e planear percursos de estudantes em Évora.','H2PT')
p('Eren Ozturk · Universidade de Évora · 30 de outubro de 2026')
p('<link href="https://hostilian.github.io/AlunUE-Agua-Pelo-Caminho/" color="#17493e"><u>Abrir aplicação · GitHub Pages</u></link> &nbsp; | &nbsp; <link href="https://github.com/Hostilian/AlunUE-Agua-Pelo-Caminho" color="#17493e"><u>Consultar repositório e testes</u></link>','SmallPT')
story.append(Diagram('flow'))
h('Âmbito e enquadramento')
p('Propõe-se um módulo de mobilidade e serviços essenciais do AlunUÉ: encontrar informação fiável sobre água para encher uma garrafa e continuar o dia. Supermercados, locais de interesse e lojas voluntárias constituem extensões opcionais. O foco da fase 1 é a investigação e os requisitos; o protótipo é material de exploração, não prova de validação.')
h('Estado do trabalho')
p('Trabalho individual. O autor declara que o docente autorizou esta modalidade; não se apresenta essa declaração como confirmação documental. A pesquisa disponível inclui três sínteses individuais reconstruídas de conversas informais da última semana, além de feedback geral recordado. As três personas e os mapas são provisórios, agora ligados a necessidades concretas desses relatos. Não foi realizado um inquérito estruturado recuperável, nem um teste de usabilidade.')
p('As sínteses são paráfrases recordadas pelo autor, não transcrições. O apêndice apresenta os três casos e distingue o que foi relatado das implicações de conceção.','SmallPT')

title('02','Método e sinais exploratórios')
h('Origem e condições da recolha')
p('O autor conversou informalmente com colegas e conhecidos, incluindo estudantes Erasmus e pessoas da sua faculdade, durante a semana anterior ao relato de 30/10/2026. Após a perda das notas originais, reconstruiu três casos individuais: C1, C2 e C3 (apêndice). O autor confirmou que as três pessoas são estudantes da UÉ e aceitaram a síntese anónima para o trabalho. Os dias e locais exatos não foram recuperados; a confirmação do vínculo e da autorização baseia-se no seu relato. A estimativa de cerca de 30 interlocutores continua aproximada; os três casos não são uma nova amostra representativa.')
p('O autor recorda perguntas sobre o que as pessoas gostariam de encontrar e sobre a utilidade de uma aplicação. A proposta era apresentada nas conversas; a ordem exata das perguntas não é recuperável. Trata-se de uma amostra de conveniência e reconstrução retrospectiva, sujeita a memória seletiva e desejabilidade social. Não mede adoção nem frequência do problema.')
table([['ID / origem','Sinal disponível e implicação'],['E1/E2 · feedback geral','Reações favoráveis, compra repetida de água e desconhecimento dos pontos de abastecimento, segundo o autor. Sem percentagens ou contagem auditável.'],['E3 · preferência do autor','Confiança, percursos, supermercados, vistas e lojas voluntárias: decisões de âmbito, não resultados de votação.'],['E4 · estado operacional','Nenhuma loja aderente confirmada. A rede proposta exige acordos futuros.'],['E5 · caso C1','Dificuldade em encontrar fontes numa cidade nova; dificuldade percebida em localizar compras económicas e pagamento com cartão. Investigar descoberta, preço e informação de pagamento.'],['E6 · caso C2','Pessoa que corre regularmente quer locais onde beber água e descansar. Investigar continuidade do percurso e paragens de descanso.'],['E7 · caso C3','Reação positiva e pedido para receber novidades. Investigar interesse em atualizações voluntárias; não equivale a adoção nem autoriza notificações automáticas.']])
h('Interpretação e proteção dos participantes')
p('Os casos sustentam necessidades específicas a investigar, não generalizações sobre todos os estudantes. A perceção de C1 sobre o comércio não constitui um levantamento dos estabelecimentos de Évora. Não foram recordadas objeções individuais; isso não prova ausência de reservas. Usam-se códigos anónimos e não se publicam contactos ou mensagens privadas. A autorização para síntese anónima dos três casos foi confirmada pelo autor. Pedir nova autorização se o âmbito da utilização mudar.')

title('03','Três personas ligadas aos relatos')
p('As personas são perfis de necessidades provisórios, ancorados nos casos C1-C3. Não são biografias nem segmentos estatisticamente validados. O autor confirmou o vínculo dos três interlocutores à UÉ. A representatividade de cada perfil para outros estudantes continua por validar. Não se atribuem idades, nacionalidades, rendimentos ou ocupações não recordados.')
table([['Perfil / base','Objetivo, evidência e pressupostos'],['P1 · Descoberta numa cidade nova / C1','Objetivo: encontrar água e alternativas económicas sem conhecer a cidade. Relato: fontes difíceis de localizar e incerteza sobre lojas económicas e pagamento com cartão. Implicação: pesquisa com fonte e custo claros; informação de pagamento só quando confirmada. Não assumir que a pessoa não fala português.'],['P2 · Corredor com paragens de água / C2','Objetivo: beber água e descansar ao longo de percursos regulares de corrida. Relato: corre frequentemente e deseja pontos de água e descanso. Implicação: permitir planear paragens e confirmar disponibilidade. Horários de corrida, distâncias e necessidades médicas não foram recolhidos.'],['P3 · Pessoa interessada em acompanhar o serviço / C3','Objetivo: saber quando o serviço estiver disponível. Relato: reação positiva e desejo de receber novidades. Implicação: futuro mecanismo voluntário de atualizações. Não inferir canal preferido, frequência, tolerância a notificações ou utilização efetiva.']])
h('O que já está sustentado e o que falta validar')
p('Descoberta e custo provêm de C1; água e descanso em corrida de C2; interesse em novidades de C3. Emoções, fluxos detalhados e soluções de interface são propostas. Cada perfil assenta num único relato reconstruído; são necessárias novas entrevistas para confirmar padrões e divergências. O perfil P3 descreve interesse na comunicação, sem demonstrar uma terceira necessidade de reabastecimento distinta.')
p('Próxima recolha: confirmar experiências concretas antes de mostrar o protótipo, aprofundar água/descanso e preferências de atualizações, recolher respostas negativas e registar data, contexto e autorização. Não preencher lacunas de memória com suposições.')

title('04','Mapas de empatia com rastreabilidade')
p('“Diz / objetivo” resume o que foi recordado, sem aspas ou transcrição literal. “Pensa”, “faz” e “sente” separam factos relatados de hipóteses para validação.')
for perfil,diz,pensa,faz,sente in [
('P1 · Descoberta numa cidade nova / C1','Relato: fontes difíceis de encontrar; procura de opções económicas e pagamento com cartão.','Hipótese: como encontrar uma alternativa e saber o custo?','Não reconstruído: percurso de procura, compras concretas e aplicação utilizada.','Não recolhido; possível incerteza é uma hipótese.'),
('P2 · Corredor / C2','Relato: deseja locais onde beber água regularmente e descansar.','Hipótese: consigo integrar água e descanso no percurso?','Relato: corre frequentemente. Trajetos, distâncias e horários não recolhidos.','Não recolhido; não presumir cansaço ou ansiedade.'),
('P3 · Acompanhamento / C3','Relato: considera a ideia positiva e gostaria de receber novidades.','Hipótese: como saber quando o serviço estiver disponível?','Manifestou interesse em atualizações; não foi observado uso do produto.','Reação positiva recordada; intensidade não medida.')]:
    h(perfil);table([['Dimensão','Relato ou hipótese identificada'],['Diz / objetivo',diz],['Pensa',pensa],['Faz',faz],['Sente',sente]],[120,375])
p('Confirmar estas interpretações com as próprias pessoas. Não tratar um mapa de empatia como acesso direto aos seus pensamentos.','SmallPT')

title('05','Mapa de jornada proposto')
p('Cenário de conceção: um estudante quer reabastecer a garrafa durante uma deslocação. A sequência abaixo não foi observada num teste nem acompanhada no terreno.')
story.append(Diagram('flow'))
table([['Etapa','Ação e possível dificuldade','Resposta de conceção'],['1 · Necessidade','Procurar água; não saber onde começar.','Lista pesquisável; localização opcional e início manual.'],['2 · Avaliação','Distinguir um ponto real de um registo incerto.','Mostrar fonte, data, acesso, custo e estado de verificação.'],['3 · Planeamento','Escolher paragens sem desvio desnecessário.','Ordem ajustável; supermercado e ponto cultural opcionais.'],['4 · Deslocação','Transferir o plano para navegação externa.','Exportação pedonal para Google Maps e alternativa em texto.'],['5 · No local','Encontrar encerramento ou informação incorreta.','Exibir limitações, procurar alternativa e preparar correção.'],['6 · Continuação','Prosseguir sem obrigação de consumo ou interação.','Sem compra obrigatória; lojas apenas com adesão explícita.']],[65,215,215])
h('Variações ligadas aos relatos')
p('<b>P1 / C1:</b> descobrir água e consultar custo/pagamento quando verificados. <b>P2 / C2:</b> planear água e descanso em corrida. <b>P3 / C3:</b> descobrir proposta → pedir novidades → escolher canal e consentir → receber informação → poder cancelar. Este último fluxo é uma proposta, ainda não implementada.')
p('O esquema não representa ruas ou pontos reais. Os candidatos OpenStreetMap exigem confirmação de potabilidade, gratuidade, acesso e funcionamento.','SmallPT')

title('06','Análise hierárquica de tarefas')
p('Objetivo 0: obter água e continuar a deslocação. A HTA descreve a tarefa pretendida e os caminhos de recuperação; não é uma análise de comportamento já observado.')
story.append(Diagram('hta'))
table([['Tarefa','Subtarefas e condição de conclusão'],['1 · Definir início','1.1 Escolher centro/campus ou coordenadas; 1.2 pedir localização apenas se desejado; 1.3 manter alternativa manual se a permissão for recusada.'],['2 · Avaliar ponto','2.1 Consultar lista; 2.2 ler fonte e data; 2.3 verificar água, custo, acesso e funcionamento; 2.4 rejeitar candidato sem confirmação para um percurso real de água.'],['3 · Planear paragens','3.1 Adicionar ponto elegível; 3.2 escolher supermercado ou local de interesse opcional; 3.3 reordenar; 3.4 rever percurso; 3.5 exportar por partes ou guardar texto.'],['4 · Seguir e confirmar','4.1 Consultar navegação externa; 4.2 verificar condições no local; 4.3 reabastecer se permitido; 4.4 escolher alternativa e registar sugestão se a informação falhar.']])
h('Planos e exceções')
p('<b>Plano principal:</b> executar 1, 2, 3 e 4. Repetir 2 quando não existir um ponto elegível. <b>Sem internet:</b> mostrar a data do último registo e disponibilizar o itinerário guardado; não prometer mapas offline. <b>Sem localização:</b> executar 1.1. <b>Serviço externo indisponível:</b> conservar a lista e oferecer texto. <b>Loja sem adesão:</b> não a apresentar como parceira.')
h('Operações atualmente exploradas no protótipo')
p('Pesquisa e filtros por tipo, demonstração identificada, seleção e ordem das paragens, exportação pedonal, partilha ou cópia com alternativa em ficheiro, sugestões guardadas apenas no dispositivo e consulta opcional de serviços externos. Não existe um diretório operacional verificado, moderação ou registo real de parceiros.')

title('07','Requisitos e critérios de avaliação')
p('Prioridades atribuídas pelo projeto: <b>P0</b> essencial; <b>P1</b> extensão. Os valores abaixo são metas propostas para testes futuros, não resultados medidos.')
table([['ID / prioridade','Requisito e rastreabilidade','Critério proposto'],['R1 · P0','Distinguir candidato, demonstração e ponto confirmado. E2 + risco de informação incorreta.','Nenhum candidato não confirmado deve ser anunciado como água garantida.'],['R2 · P0','Encontrar água sem conta e sem localização obrigatória. E1/E2 + hipótese de acessibilidade.','Pelo menos 4 de 5 participantes concluem a tarefa com início manual.'],['R3 · P0','Mostrar fonte, data, custo e acesso. E2 + decisão de confiança.','Pelo menos 4 de 5 identificam corretamente a incerteza antes de escolher.'],['R4 · P0','Manter todas as paragens ao exportar. E3.','Nenhuma paragem selecionada desaparece; alternativa legível em texto.'],['R5 · P0','Recuperar de falhas de rede e API. Decisão de robustez.','A interface conserva o plano e informa o utilizador da falha.'],['R6 · P1','Combinar supermercado e local de interesse. E3.','A pessoa consegue excluir cada extensão e manter água como foco.'],['R7 · P1','Lojas voluntárias e sem compra obrigatória. E3/E4.','Nenhuma loja aparece como parceira sem acordo explícito.'],['R8 · P1','Água e descanso no percurso; custo/pagamento quando verificados. E5/E6.','Nunca apresentar descanso, preço ou cartão como confirmados sem fonte.'],['R9 · P1','Atualizações futuras por adesão explícita. E7.','Nenhum contacto ou notificação sem autorização; opção de cancelar. Ainda não implementado.']],[60,240,195])
h('Usabilidade e acessibilidade')
p('Metas de conceção: rótulos em português europeu, foco visível, utilização por teclado, contraste legível, ampliação sem perda de conteúdo, controlos táteis adequados e mensagens que expliquem a recuperação. Avaliar reconhecimento dos estados, taxa de conclusão, erros, tempo por tarefa e satisfação. Não foi recolhido SUS nesta fase.')
h('Arquitetura de informação')
p('<b>Descobrir</b> → pesquisar, filtrar e verificar a origem. <b>O meu percurso</b> → início, paragens e exportação. <b>Comunidade</b> → proposta de adesão e sugestão local. <b>O projeto</b> → evidência, limitações e fontes. O percurso mantém-se utilizável sem aderir à rede de lojas.')

title('08','Limitações, próximos passos e fontes')
h('Limitações que afetam a avaliação desta fase')
p('A investigação é exploratória e retrospectiva. Foram reconstruídos três casos individuais, mas faltam transcrições ou notas originais, questionário estruturado, confirmação do universo de participantes e validação independente das três personas. A reação a uma ideia apresentada não mede adoção. Por isso, os artefactos de conceção não devem ser interpretados como resultados de uma investigação concluída. A perda das notas explica a limitação, mas não a elimina.')
h('Plano de validação e evolução')
table([['Passo','Resultado a obter'],['1 · Recolha complementar','Entrevistas neutras com estudantes reais e confirmação dos problemas antes de mostrar o conceito; preservar sínteses anónimas autorizadas.'],['2 · Revisão da fase 1','Atualizar personas, mapas e requisitos com a evidência recolhida e manter um registo das alterações.'],['3 · Avaliação do protótipo','Testar tarefas em papel e média fidelidade; revisão heurística segundo o enunciado.'],['4 · Fase final','Testes com pelo menos cinco utilizadores reais da UÉ, métricas de tarefas e SUS; apresentar apenas os resultados efetivamente recolhidos.'],['5 · Serviço operacional','Verificar pontos de água no terreno, definir manutenção e obter adesão de lojas. Avaliar PWA em Android antes de decidir sobre APK.']])
h('Papel da inteligência artificial')
p('Foi utilizada IA generativa para organizar e redigir este relatório em português, propor artefactos de conceção, produzir diagramas e apoiar o código e a tradução do protótipo. O autor forneceu as recordações e decisões de âmbito. A IA não realizou entrevistas nem verificou locais. O autor deve rever e compreender o conteúdo e é responsável pela autenticidade do que submete.')
h('Fontes e materiais de apoio')
p('1. INF13186L, <i>Introdução à UC</i>, pp. 5-6: âmbito AlunUÉ, relatório até dez páginas e identificação do uso de IA.<br/>2. INF13186L, <i>gemini_fase1</i>, p. 1: pesquisa, personas, mapas de empatia/jornada e HTA. Os exemplos seguintes não foram usados como entrevistas.<br/>3. Declarações e recordações do autor, 30/10/2026.<br/>4. <link href="https://www.openstreetmap.org/copyright"><u>OpenStreetMap: dados e atribuição</u></link>; <link href="https://developers.google.com/maps/documentation/urls/get-started"><u>Google Maps URLs: documentação oficial</u></link>.<br/>5. <link href="https://hostilian.github.io/AlunUE-Agua-Pelo-Caminho/"><u>Aplicação no GitHub Pages</u></link>; <link href="https://github.com/Hostilian/AlunUE-Agua-Pelo-Caminho"><u>Repositório autónomo: código, documentação e testes</u></link>. O PDF é autónomo; as ligações não substituem os artefactos exigidos.','SmallPT')

title('09','Apêndice A · Registos reconstruídos')
p('Fonte: relato do autor em 30/10/2026, acerca de conversas na semana anterior. O autor confirmou vínculo à UÉ e autorização dos três para síntese anónima. Códigos anónimos substituem nomes. As perguntas e respostas abaixo são paráfrases, não citações literais. A ordem precisa das perguntas, os locais e o dia de cada conversa não foram recuperados.')
h('C1 · Primeira pessoa consultada')
table([['Campo','Síntese recordada'],['Pergunta','O que gostaria de encontrar ou o que seria útil nesta proposta? Formulação aproximada.'],['Resposta','É difícil encontrar fontes de água e orientar-se numa cidade nova. Referiu dificuldade em encontrar lojas com produtos económicos, como água, e pagamento com cartão; mencionou a pouca presença percebida de cadeias comerciais.'],['Interpretação','Descoberta de locais e informação económica/de pagamento são necessidades a investigar. A opinião sobre o comércio não comprova as condições reais das lojas.']],[100,395])
h('C2 · Pessoa que corre regularmente')
table([['Campo','Síntese recordada'],['Pergunta','O que gostaria de encontrar no serviço? Formulação aproximada.'],['Resposta','Corre frequentemente e deseja encontrar locais onde possa beber água regularmente e descansar.'],['Interpretação','Água e descanso são necessidades explícitas; não foram recordados trajeto, frequência exata, duração ou locais. O autor confirmou posteriormente a identidade deste interlocutor; mantém-se o código anónimo na análise.']],[100,395])
h('C3 · Pessoa interessada em novidades')
table([['Campo','Síntese recordada'],['Pergunta','O autor diz ter feito perguntas semelhantes sobre a proposta; a sequência exata não está disponível.'],['Resposta','Reagiu positivamente, considerou a ideia útil e manifestou vontade de receber novidades.'],['Interpretação','Existe interesse declarado em acompanhamento, sem canal ou periodicidade definidos. Não constitui consentimento para publicar dados pessoais nem prova de adoção.']],[100,395])
p('O autor refere ter uma lista de outras pessoas interessadas, mas não foram fornecidos nomes, contactos ou respostas adicionais. A lista não é contabilizada como novos participantes nem apresentada como pedidos de notificação autorizados.','SmallPT')

title('10','Síntese visual · Da evidência ao desenho')
p('Cada linha liga um relato reconstruído a uma necessidade, a uma persona provisória e aos requisitos correspondentes. As cores distinguem os casos; não representam percentagens, intensidade ou frequência.')
story.append(EvidenceVisual())
h('Como ler o projeto')
table([['Camada','O que pode ser afirmado'],['RELATO','O autor recorda três conversas e confirmou vínculo à UÉ e autorização para síntese anónima.'],['INTERPRETAÇÃO','Os temas orientam a conceção; a ligação indicada é uma análise do projeto, não uma conclusão estatística.'],['PROPOSTA','Personas, mapas, metas e funcionalidades futuras devem ser confirmados por investigação e testes.']],[100,395])
h('O percurso de validação')
p('<b>Recordar e documentar</b> → confirmar com participantes → aprofundar a pesquisa → rever os artefactos → testar tarefas → medir e melhorar. A qualidade visual ajuda a comunicar; a qualidade da evidência sustenta as decisões.')

def footer(c,doc):
    paint_page(c,doc,en=False)
pdf=OUT/'AlunUE_Agua_Pelo_Caminho_Fase1_PT_v4.pdf'
SimpleDocTemplate(str(pdf),pagesize=(595.28,841.89),rightMargin=50,leftMargin=50,topMargin=43,bottomMargin=57,title='AlunUÉ - Água pelo caminho - Fase 1',author='Eren Ozturk').build(story,onFirstPage=footer,onLaterPages=footer)
(OUT/'Relatorio_editavel_PT.md').write_text('\n\n'.join(text_source),encoding='utf-8')
print(pdf)
