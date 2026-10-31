# AlunUÉ · Protocolo de usabilidade e SUS

Instrumento preparado em 30/10/2026 para sessões futuras. Não contém testes executados nem resultados de utilizadores. O protocolo deve ser pilotado e ajustado antes de congelar o ciclo formal.

## Desenho da sessão

Objetivo: avaliar reconhecimento dos estados de confiança, descoberta, planeamento, exportação e recuperação de falhas. Recrutar pelo menos cinco estudantes reais e distintos da UÉ para a fase final, conforme o enunciado. Procurar diversidade de contexto e dispositivo. Não afirmar representatividade estatística com esta amostra.

1. Fixar commit/versão, dispositivo, navegador e condições de rede; registar o contexto sem identificadores pessoais.
2. Explicar que se testa o produto, não a pessoa; obter autorização voluntária para notas e síntese anónima. Áudio/vídeo exige autorização separada e não é necessário para este kit.
3. Fazer um piloto do procedimento, anotado como piloto; não o juntar silenciosamente à versão final.
4. Ler cada objetivo, sem indicar botões ou resolver a tarefa. Pedir à pessoa que descreva o que está a pensar se se sentir confortável.
5. Iniciar o cronómetro após a instrução; parar quando a pessoa terminar, desistir, atingir o limite previamente fixado ou precisar de ajuda. Registar o motivo.
6. Aplicar os dez itens SUS depois da utilização, antes da discussão final. Recolher uma reação imediata, sem persuadir a pessoa.
7. Fazer a conversa final e confirmar o significado das observações sem sugerir respostas.

Tempo de planeamento: cerca de 25–35 minutos, a confirmar no piloto. Definir e conservar limites por tarefa antes do ciclo (por exemplo, três minutos para descoberta e cinco para planeamento). Estes tempos são parâmetros propostos, não resultados.

## Preparação que evita resultados enganadores

- Não navegar realmente para pontos não verificados nem pedir que alguém beba água durante o teste.
- Tarefas de planeamento usam demonstrações explicitamente fictícias; confirmar que a pessoa distingue isso dos candidatos OSM.
- Para T4, o moderador prepara uma falha repetível: bloquear/rejeitar um pedido de serviço no ambiente de teste, ou usar o modo offline depois de existir um registo guardado. Dizer que é uma simulação técnica; não fingir que a falha aconteceu espontaneamente.
- Registar se havia dados anteriores. Testar primeira utilização sem rede e registo antigo em condições separadas; não classificar uma lista antiga como dados atuais.
- Não misturar versões, modo demo e uso real no mesmo conjunto de resultados sem assinalar a diferença.
- Disponibilizar início manual, teclado, ampliação e leitor de ecrã quando aplicáveis. TalkBack e instalação Android exigem execução real no dispositivo.

## Tarefas e critérios observáveis

| ID | Objetivo lido à pessoa | Conclusão / observação |
|---|---|---|
| T1 | Sem permitir localização, escolhe um início manual e explica os estados dos pontos. | Início definido; distingue candidato, demonstração e confirmado sem ajuda. |
| T2 | Ativa a demonstração identificada, escolhe duas paragens e altera a ordem. | Duas paragens fictícias aparecem na ordem pretendida; não as interpreta como água garantida. |
| T3 | Acrescenta supermercado e local cultural e retira uma extensão. | A pessoa mantém controlo sobre os extras; nenhuma paragem obrigatória é introduzida. |
| T4 | Com a falha preparada pelo moderador, indica a mensagem, a data e o que continua disponível. | Reconhece erro/antiguidade; plano preservado; não confunde cache com verificação atual. |
| T5 | Exporta as paragens ou guarda alternativa legível em texto. | Todas as paragens e a ordem mantidas; recuperação se partilha/cópia não estiver disponível. |
| T6 | Prepara uma sugestão anónima e explica onde fica. | Entende armazenamento local e ausência de contacto automático. |

Registar por tarefa: estado (`concluida`, `com-ajuda`, `nao-concluida`, `nao-tentada` ou não registado), segundos efetivamente medidos, erros observados e notas. “Não medido” não equivale a zero. Erro é uma ação que impede/atrasa o objetivo; definir a taxonomia no piloto. “Com ajuda” exige registar que ajuda foi dada.

## SUS: instrumento, idioma e cálculo

O kit apresenta os dez itens da versão europeia portuguesa de Martins et al. (2015), mantendo a palavra “produto”. Usar a sequência e polaridade publicadas, escala 1–5 e os mesmos rótulos em todas as sessões. Atribuir a fonte ao instrumento; não afirmar que o próprio AlunUÉ ou uma amostra recolhida já foi validada.

Aplicar depois de experimentar o produto, antes da discussão. O moderador não escolhe respostas nem transforma ausência de resposta em ponto neutro. O cálculo automático só ocorre com dez inteiros válidos entre 1 e 5. Caso contrário, guardar como incompleto e descrever a ausência; não incluir essa sessão na média SUS.

Para os itens ímpares, subtrair 1 à resposta. Para os pares, subtrair a resposta a 5. Somar as dez contribuições e multiplicar por 2,5. O resultado varia de 0 a 100; não é uma percentagem, uma taxa de sucesso ou uma nota académica. Não somar diretamente as respostas e não interpretar itens isolados como subescalas sem justificação.

Exemplo exclusivamente para verificar o cálculo do software, sem representar um participante: respostas `[4, 2, 5, 1, 3, 3, 4, 1, 3, 1]` produzem 77,5. Os testes automáticos usam também os limites 0 e 100, respostas em falta e valores inválidos. Nenhum exemplo é carregado como dados na interface.

Fontes primárias:

- Brooke, J. (1996). [SUS: A “quick and dirty” usability scale](https://hci-studies.org/methods-and-measures/downloads/SUS_Brooke1996.pdf). Em *Usability Evaluation in Industry*, pp. 189–194. Fonte do procedimento e cálculo. © Digital Equipment Corporation, 1986; reconhecer a origem do instrumento.
- Martins, A. I., Rosa, A. F., Queirós, A., Silva, A., & Rocha, N. P. (2015). [European Portuguese Validation of the System Usability Scale (SUS)](https://doi.org/10.1016/j.procs.2015.09.273). *Procedia Computer Science, 67*, 293–300. © 2015 autores; artigo de acesso aberto CC BY-NC-ND 4.0. Os itens portugueses reproduzidos no kit mantêm a formulação e a atribuição. O próprio artigo descreve limites de fiabilidade; não os omitir ao discutir a escala.

## Análise antes de escrever o relatório

Verificar ficheiros, consentimento, vínculo à UÉ, completude e pessoas distintas. Identificadores de sessão repetidos são ignorados pela página, mas identificadores diferentes não provam participantes diferentes. Não publicar JSON/CSV individuais no repositório público.

Reportar:

- Participantes distintos, sessões por versão, contexto e recrutamento; exclusões e motivos.
- Conclusões sem ajuda / tentativas, mostrando os valores absolutos. Tarefas não tentadas e não registadas ficam fora do denominador e são descritas à parte. Conclusão com ajuda é categoria separada.
- Tempo por tarefa apenas quando medido; preferir mediana e intervalo com amostras pequenas, identificando interrupções.
- Erros e problemas com evidência observada e consequência; distinguir falha de produto, rede e procedimento.
- SUS: número completo, valores por sessão anónima, média/mediana e dispersão. Não usar apenas a média como prova de qualidade ou de ausência de problemas.
- Evidência negativa, reservas, divergências e alterações realizadas, ligadas a requisitos R1–R9.

Os totais da página são descritivos, não uma validação estatística. Não anunciar aprovação, acessibilidade completa, água confirmada ou adesão de lojas a partir destes testes.

## Entregáveis por ciclo

1. Protocolo congelado e versão do protótipo.
2. Registos reais, consentidos e guardados de forma controlada pelo autor.
3. Matriz anónima de problemas: ID, tarefa, evidência, gravidade justificada, requisito e alteração.
4. Tabela de métricas com denominadores e ausências; SUS calculado apenas quando completo.
5. Comparação antes/depois e limitações. Separar avaliação heurística entre pares de testes com estudantes: uma não substitui a outra.
