# Revisão heurística preparatória com apoio de IA

Data: 30/10/2026. Projeto: AlunUÉ - Água pelo caminho.

Esta é uma inspeção estática do código, preparada por IA para apoiar melhorias. **Não é a avaliação heurística cruzada entre colegas exigida na fase 2, nem um teste com utilizadores.** Não foram realizados nesta revisão ensaios no navegador, sessões com participantes, medições de frequência ou avaliações humanas independentes. As consequências previstas e a gravidade são hipóteses de inspeção a confirmar.

## Método e fontes

Foram lidos `dist/index.html`, `dist/app.mjs`, `dist/style.css`, `dist/core.mjs` e o novo `dist/map.mjs`. Consideraram-se descoberta, localização, filtragem, planeamento, exportação, recuperação e mapa. As evidências referem funções, seletores e texto do código; não são relatos de comportamentos observados em pessoas.

Referenciais primários, consultados em 30/10/2026:

- Jakob Nielsen, [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/), NN/g, artigo com revisão indicada de 30/01/2024.
- Jakob Nielsen, [Severity Ratings for Usability Problems](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/), NN/g.

Os princípios e a escala abaixo são resumidos em português; os achados são análise específica deste código. Não se reproduzem os cartazes ou ilustrações da NN/g.

Instantâneo inicial, antes das correções desta ronda:

| Ficheiro | SHA-256 |
|---|---|
| `dist/app.mjs` | `8bcdde07a84405cd7e3b00abc30054627a48ca9c33da23c1d4b9d1e085f10c05` |
| `dist/map.mjs` | `ac047e38849fe571d68825bdc6dbefefa0210d71fd16176e8f17f6fc6fc16436` |

Os números de linha podem mudar durante a integração; procurar pelos nomes das funções e seletores indicados. A secção de acompanhamento distingue achados originais de correções posteriores.

## Escala proposta de gravidade

| Grau | Interpretação usada nesta inspeção |
|---|---|
| 0 | Não se confirma um problema; conservar como observação ou ponto forte. |
| 1 | Ajuste de apresentação ou clareza, com baixo impacto previsto. |
| 2 | Dificuldade contornável, esforço adicional ou risco de confusão numa tarefa. |
| 3 | Risco de perda de trabalho ou de resultado relevante diferente do esperado; tratar com prioridade. |
| 4 | Bloqueio crítico que impediria disponibilizar a funcionalidade; nenhum caso deste nível foi estabelecido nesta inspeção. |

A classificação considera impacto, repetição provável e dificuldade de recuperação. A frequência real não foi medida. Um grau atribuído por esta inspeção não é uma média de avaliadores nem um resultado de investigação.

## Cobertura das dez heurísticas

| Heurística | Evidência concreta e problema/oportunidade | Gravidade proposta | Correção ou verificação sugerida |
|---|---|---|---|
| **H1. Estado do sistema visível** | **A01:** no instantâneo, `#locate` guarda `state.location` e anuncia localização definida, mas não altera `state.start` nem `#start`. `origin()` continua a devolver o centro quando a seleção permanece `center`. O anúncio pode ser interpretado como início do percurso alterado. | **3**: um percurso pode começar num local diferente do pretendido; é uma inferência do fluxo, não ocorrência medida. | Depois de obter coordenadas, selecionar explicitamente a origem GPS ou explicar que apenas a ordenação por distância mudou. Confirmar o início no resumo e na ligação exportada. |
| **H2. Linguagem e conceitos do mundo real** | **A02:** o início manual em `#start` oferece latitude/longitude, além de duas zonas aproximadas e GPS. Para quem sabe uma morada ou referência, mas não coordenadas, a alternativa manual exige uma procura adicional. O mapa interativo ainda só seleciona candidatos para a lista. | **2**: obstáculo previsto para recém-chegados; não impede escolher o centro. | Permitir escolher uma referência conhecida ou um ponto no mapa como início; explicar claramente quando a partida é aproximada. Validar os nomes de polos com estudantes. |
| **H3. Controlo e liberdade** | **A03:** `#clear` elimina imediatamente as paragens; `#delete-local` remove preferências, cache e sugestões sem confirmação ou recuperação. As sugestões não têm envio remoto que permita recuperá-las. | **3** para perda de sugestões; **2** para limpar um percurso simples. | Confirmar a eliminação permanente de registos locais; oferecer desfazer para a limpeza do percurso e exportação antes da eliminação. Cancelar deve conservar os dados. |
| **H4. Consistência e padrões** | **A04:** o filtro de categoria apenas muda a classe `.selected`; não expõe `aria-pressed`, enquanto o botão de demonstração já usa esse estado. Além disso, o CSS global aplica `cursor:wait` a todos os botões desativados, incluindo candidatos que aguardam verificação humana, não uma operação em curso. | **2** para estado não exposto; **1** para cursor. | Sincronizar o estado acessível dos filtros; reservar o cursor de espera para operações em curso. Ensaiar teclado e leitor de ecrã; não inferir conformidade só pelo atributo. |
| **H5. Prevenção de erros** | **A05:** `navigate()` esconde a vista anterior e muda o título, mas não coloca foco no título da nova vista. `renderCards()` e `renderJourney()` substituem HTML com os controlos focados, sem recuperação explícita de foco após adicionar/retirar. Pode ser difícil perceber onde continuar usando teclado. | **2**: risco de navegação repetida ou ativação no contexto errado. | Gerir foco ao mudar de vista e depois de alterações destrutivas do elemento focado. Conservar sequência de teclado e não deslocar o foco durante a escrita na pesquisa. |
| **H6. Reconhecimento em vez de memorização** | **A06:** `renderJourney()` numera a lista segundo `selected()`, enquanto a exportação usa `ordered()`. Nos modos automáticos, a ordem sugerida aparece numa frase do resumo e pode diferir da lista numerada que a pessoa está a rever. | **2**: a pessoa precisa de comparar duas representações do mesmo plano. | Apresentar uma previsão numerada da ordem efetivamente exportada, ou atualizar claramente a lista. Distinguir ordem manual guardada de sugestão automática, preservando a possibilidade de voltar à primeira. |
| **H7. Flexibilidade e eficiência** | **A07:** a pesquisa em `renderCards()` usa apenas `toLowerCase().includes()`. Assim, `agua` não corresponde a `Água`; o mesmo risco existe para nomes com diacríticos. | **2**: pesquisas plausíveis podem devolver vazio apesar de haver correspondências. | Comparar uma versão normalizada dos textos e da consulta, preservando a grafia original na apresentação. Verificar `agua`/`Água`, variantes de nomes e pesquisa com espaços. |
| **H8. Apresentação focada no essencial** | **A08:** a vista Descobrir coloca mapa estático no herói, uma secção adicional de mapa interativo e explicações antes dos filtros e cartões. Há também repetição de avisos nos cartões. São avisos úteis, mas a hierarquia pode alongar o acesso à tarefa principal em ecrãs pequenos. | **1**, hipótese de composição a observar em navegador e com participantes. | Considerar um único bloco de mapa com alternativa estática, aviso principal conciso e detalhes progressivos. Conservar a distinção entre candidato e confirmado; não ocultar informação de confiança para encurtar o ecrã. |
| **H9. Diagnóstico e recuperação de erros** | **A09:** o `try` de `#copy` inclui `itinerary()`, mas o `catch` anuncia sempre indisponibilidade de cópia. Uma origem manual inválida pode lançar antes de qualquer acesso à área de transferência. `#share` também agrega causas distintas numa mensagem genérica. No mapa, `failed` fica verdadeiro após o primeiro `tileerror`, mesmo que carregamentos posteriores recuperem. | **2** para diagnóstico da exportação; **1** para aviso persistente do mapa. | Separar validação do plano dos erros de partilha/cópia; mostrar a causa recuperável junto da origem e colocar foco nesse campo. Rever o estado do mapa quando o carregamento recupera, sem esconder falhas que permaneçam. |
| **H10. Ajuda no contexto da tarefa** | **A10:** os candidatos têm botão desativado com indicação de verificação necessária; a explicação detalhada está em Fonte e verificação e na secção O projeto, com documentos `.md`. Falta um caminho curto junto da decisão para perceber o que falta confirmar ou como explorar o planeamento sem pontos verificados. | **2**, oportunidade de reduzir a necessidade de procurar documentação. | Ligar à ficha de verificação ou a uma ajuda curta junto dos candidatos. Explicar em passos a diferença entre explorar o mapa, testar demonstrações e obter água real. A ajuda deve dizer que um utilizador não confirma potabilidade pelo aspeto da água. |

## Pontos fortes encontrados no código

- `canRoute()` impede que uma simples etiqueta cartográfica seja tratada como água potável gratuita; lojas exigem adesão explícita. Esta proteção deve ser preservada ao resolver as dificuldades de descoberta.
- O início não depende de conta nem de autorização de localização. Existem partida aproximada e introdução manual.
- A exportação divide percursos longos em partes ligadas; há alternativas por etapa e em texto.
- Os serviços têm mensagens de erro e preservam uma alternativa quando uma consulta falha. Os estados de demonstração e de candidato estão identificados em texto.
- O mapa interativo é opcional, carrega a biblioteca localmente, identifica o pedido de ruas ao OpenStreetMap e oferece escala, atribuição, marcadores com nomes e teclado. O mapa estático e a lista são alternativas explícitas.
- O CSS contém foco visível, adaptação de colunas e controlos geralmente amplos. Contraste real, ampliação e TalkBack ainda precisam de ensaio, não foram certificados nesta revisão.

## Acompanhamento das correções

O responsável pela integração comunicou as alterações seguintes, cuja presença foi conferida por leitura do código em 30/10/2026. **Correção implementada no código, verificar em browser** não significa validação por participantes nem avaliação cruzada concluída. A inspeção posterior encontrou `dist/app.mjs` com SHA-256 `9e85956ef2cb1f94a8f8b08a3fc406536e3c682acb15c0adacf532b2f9afc934` e `dist/map.mjs` com SHA-256 `fc7083dc409054fd0e107cdf728a723418e525d088e2b66dd2609e55fc07a0d5`.

| Achado | Estado de integração | Verificação ainda necessária |
|---|---|---|
| A01 - GPS como início | Correção implementada no código, verificar em browser: sucesso seleciona `state.start` e `#start` como GPS. | Autorizar localização numa sessão de teste; comparar seletor, resumo e origem exportada. Repetir com recusa/indisponibilidade. |
| A02 - Início sem conhecer coordenadas | Alternativa implementada no código, verificar em browser: modo de escolha de início no mapa atualiza a origem manual. Pesquisa de morada/nome continua uma oportunidade. | Escolher uma rua no mapa e conferir coordenadas e origem exportada. Verificar alternativa por teclado e quando as ruas não carregam. |
| A03 - Limpeza e eliminação local | Correção implementada no código, verificar em browser: desfazer na limpeza do percurso; confirmação antes de apagar registos locais e ligação ao apagamento de exportações nativas. | Criar plano e sugestão de teste; cancelar eliminação; desfazer limpeza; confirmar eliminação pretendida. Não usar registos de participantes reais. |
| A04 - Estado dos filtros | `aria-pressed` implementado no código, verificar em browser. O cursor global de espera em controlos desativados permanece oportunidade de apresentação. | Confirmar estado visual/acessível e navegação por teclado. |
| A05 - Foco | Correção parcial implementada no código, verificar em browser: título recebe foco na mudança de vista; cartões preservam foco ao adicionar/retirar. Os controlos de retirar/reordenar da lista do percurso ainda não recuperam foco explicitamente neste instantâneo. | Mudar entre vistas, adicionar/retirar cartões e retirar/reordenar paragens sem rato; confirmar foco útil e ordem previsível. |
| A06 - Ordem revista e exportada | Correção implementada no código, verificar em browser: a lista começa pela ordem de `ordered()` e conserva separadamente os selecionados não elegíveis. | Comparar lista, resumo e ligações nas três opções de ordenação. Confirmar que reordenar manualmente continua previsível. |
| A07 - Pesquisa sem acentos | Correção implementada no código, verificar em browser: pesquisa utiliza `foldText`; foi acrescentado um teste automático pelo responsável pela integração. Esta revisão não executou esse teste. | Pesquisar com/sem acentos e espaços; confirmar igualdade de resultados sem alterar os nomes apresentados. |
| A09 - Diagnóstico da exportação/mapa | Correção implementada no código, verificar em browser: validação do itinerário separada da partilha/cópia; o ciclo de carregamento das ruas repõe o indicador de falha. | Testar coordenadas inválidas, recusa de área de transferência, cancelamento de partilha e recuperação após falha de mosaicos. |
| A08 - Hierarquia visual; A10 - Ajuda contextual | Oportunidades abertas neste instantâneo. | Confirmar prioridade com avaliação humana e observação da interface antes de fechar cada achado. |

## Preparar a avaliação cruzada da fase 2

1. Fixar uma versão identificável do protótipo e fornecer as tarefas, sem apresentar esta lista antes da primeira inspeção independente, para reduzir condicionamento.
2. Cada colega regista individualmente tarefa, ação, problema, heurística, evidência e gravidade. Usar capturas de ecrã autorizadas e exemplos reproduzíveis.
3. Consolidar duplicados e discutir a gravidade depois das inspeções; conservar divergências em vez de inventar consenso.
4. Verificar correções no navegador, por teclado e no dispositivo previsto. Registar também o que não foi verificado.
5. Apresentar ao docente os nomes/códigos e papéis efetivos de quem participou, datas, versão e resultados reais. Esta preparação por IA permanece identificada separadamente.

Não existem neste documento taxas de sucesso, pontuações SUS, tempos de tarefa ou percentagens de utilizadores afetados. Esses resultados dependem de recolha real com autorização.


## Verificação funcional da integração — 31/10/2026

O integrador verificou no navegador: pesquisa `agua` devolve os 14 candidatos sem alterar os nomes; dois exemplos fictícios podem ser selecionados; limpar e desfazer recuperam o plano; reordenar conserva foco num controlo válido e atualiza a exportação; a mudança de vista foca o título; escolher uma rua no mapa seleciona origem manual e atualiza as coordenadas. O caderno abriu com zero sessões e bloqueou registo sem consentimento. Interface principal e caderno foram observados com largura útil de 375 px, sem transbordo horizontal. A recuperação offline e a exclusão de mosaicos/APIs da cache da interface têm testes automáticos.

Os controlos da lista do percurso passaram a recuperar foco explicitamente; o cursor de espera dos botões desativados foi substituído. A permissão GPS real, TalkBack, testes em Android e avaliação com pessoas permanecem pendentes. Esta verificação pelo assistente não é uma avaliação cruzada humana nem um teste com participantes.
