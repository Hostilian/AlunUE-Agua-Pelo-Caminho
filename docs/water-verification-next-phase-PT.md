# Verificação da água: próxima fase

Revisão documental em 30/10/2026. Este plano prepara a confirmação de locais; não regista vistorias já realizadas.

## Resultado da revisão

O projeto dispõe de 14 candidatos cartográficos no centro histórico, provenientes de 15 registos OpenStreetMap. Nenhuma das fontes consultadas permite confirmar, para um desses pontos em concreto, a combinação atual de água para consumo, funcionamento, acesso autorizado e gratuitidade. A ausência de confirmação não prova a inexistência de bebedouros.

Na aplicação, todos continuam com `status: candidate`. Não se altera um estado porque uma página diz que a água da rede é potável ou porque uma fonte aparece num roteiro turístico.

## Fontes primárias adicionais

| Fonte consultada | Evidência útil | Decisão para o diretório |
|---|---|---|
| [CME: A água que consumimos em Évora](https://www.cm-evora.pt/municipe/areas-de-acao/aguas/a-agua-que-consumimos-em-evora/), página com atualização indicada de 07/01/2021 | Descreve o controlo da água distribuída pela rede e remete para resultados analíticos. | Contexto sobre a rede; não determina a origem, a manutenção ou a autorização de uso de uma torneira concreta. A referência legal antiga da página não é reutilizada como legislação atual. |
| [CME: análises à qualidade da água](https://www.cm-evora.pt/municipe/areas-de-acao/aguas/qualidade-da-agua/) | Na consulta, a secção de 2026 disponibiliza o 1.º e 2.º trimestres; o 2.º tem data de publicação indicada de 18/09/2026. | Guardar ligação e período do boletim pertinente. O boletim não confirma horário, custo, funcionamento ou acesso a cada candidato. |
| [UÉ: catálogo de relatórios de sustentabilidade](https://www.uevora.pt/viver/sustentabilidade-inclusao/relatorios-de-sustentabilidade) e [relatório 2020-2025](https://gdoc.uevora.pt/1005279), disponibilizado em 26/03/2026 | O relatório apresenta consumos de água por polos, edifícios e residências, entre outros indicadores. | É uma fonte institucional recente sobre consumo; não fornece um inventário operacional de locais autorizados para encher garrafas. Pedir confirmação específica ao serviço responsável pelo edifício. |
| [CME: Água, um bem para todos](https://www.cm-evora.pt/municipe/areas-de-acao/ambiente/agua-um-bem-para-todos/), atualização indicada de 07/06/2023 | Explica a poupança de água e o uso da água do aqueduto na rega de espaços verdes pelo projeto LIFE Água da Prata. | Uma infraestrutura de rega ou elemento do aqueduto não passa a ponto de consumo humano. |
| [CME: relatório de manutenção do centro histórico](https://www.cm-evora.pt/wp-content/uploads/2020/07/RELATORIO_02_Manutencao_Higiene_Limpeza_Publicas-Centro_Historico.pdf), outubro de 2012, secção 5.14, p. 78 | Evidência histórica sobre quatro bebedouros fora de zonas verdes e uma avaria nessa avaliação. | Ajuda a formular o pedido de inventário. Não transportar o estado de 2012 para 2026. |
| [CME: roteiro Percursos e Memórias da Água](https://www.cm-evora.pt/wp-content/uploads/2022/10/Agua_FolhetoPT.pdf), 2022 | Identifica património hidráulico. | Usar para contexto cultural; não para certificar água de beber. |

As pesquisas nos domínios institucionais incluíram bebedouro/bebedouros, água potável, dispensadores e reabastecimento de garrafas. Não se encontraram fontes primárias com informação operacional suficiente para promover um candidato. Não é uma pesquisa exaustiva de todos os documentos municipais ou universitários.

## Trabalho que pode começar já

1. **Pedido documental:** solicitar ao Município o inventário atual de bebedouros para consumo humano, coordenadas, entidade gestora, horários, acesso e manutenção. Para locais da UÉ, pedir a identificação do serviço responsável e de pontos onde seja permitido encher garrafas. Há [rascunhos em português](water-contact-drafts-PT.md), ainda não enviados.
2. **Visita de confirmação:** levar a [ficha de terreno](water-field-checklist-PT.md) e o [CSV dos 14 candidatos](water-field-register-PT.csv). A localização OSM é uma hipótese de pesquisa, não uma morada oficial. Não entrar em áreas reservadas.
3. **Revisão da evidência:** relacionar declaração da entidade responsável, observação datada e condições de acesso ao mesmo equipamento. Uma fotografia confirma apenas aquilo que mostra.
4. **Publicação controlada:** rever os campos de cada local e conservar a origem cartográfica. Só promover para `checked` quando a confirmação estiver completa. Não publicar nomes, números pessoais, assinaturas ou mensagens privadas como evidência sem autorização.
5. **Manutenção:** disponibilizar mecanismo de correção, data da última confirmação e suspensão perante aviso de avaria, restrição ou informação contraditória.

## Condições para um percurso real de água

A implementação atual em `dist/core.mjs` exige `potable === true`, `free === true`, `accessConfirmed === true`, `operational === true`, uma data `checkedAt` e `status === 'checked'`. Uma loja exige ainda `optIn === true`. Coordenadas válidas também são obrigatórias. Nada neste documento altera essa regra.

| Campo | Evidência a registar | O que não chega |
|---|---|---|
| `potable` | Indicação atual do responsável ou informação oficial aplicável ao equipamento e ausência de aviso contrário conhecido. Guardar data e referência. | Aspeto, cheiro, sabor, etiqueta OSM, qualidade geral da rede ou fotografia de água a correr. |
| `free` | Confirmação de custo zero para o enchimento proposto, incluindo eventual obrigação de compra. | Não existir preço visível. |
| `accessConfirmed` | Autorização e condições concretas: público/estudantes/clientes, horário, portão, escadas ou outra restrição observável. | Rua pública próxima ou porta aberta durante uma visita. |
| `operational` | Observação datada do equipamento a funcionar, ou informação atual identificada do responsável. Registar se o enchimento de garrafa é possível. | Inventário antigo ou fotografia sem data. |
| `checkedAt` | Data/hora e âmbito da confirmação, com referências recuperáveis. | Data de extração OSM ou data de publicação de um texto sem ligação ao local. |
| `optIn` | Adesão explícita da entidade com legitimidade, condições acordadas e autorização para divulgar o local como participante. | Reação informal favorável de um funcionário ou colocação do nome da loja no mapa. |

Cada confirmação é um retrato datado. O serviço não deve prometer que o estado observado continua válido para sempre. Propõe-se uma política de revisão periódica por local e suspensão imediata perante um aviso; o intervalo precisa de ser acordado com a entidade gestora, não é uma norma legal estabelecida por este projeto.

## Integração recomendada na aplicação

- Mostrar separadamente **registo cartográfico**, **condições confirmadas em data indicada** e **aviso de indisponibilidade**.
- Manter uma lista consultável quando não há pontos elegíveis; explicar os campos em falta sem anunciar que não existe água na cidade.
- Acrescentar referência da verificação e âmbito do acesso às fichas, sem substituir a ligação OSM original.
- Uma falha de API conserva o estado desconhecido. Dados guardados nunca transformam candidatos em confirmados.
- Uma sugestão do utilizador abre uma revisão; não promove automaticamente o ponto.

## O que exige uma ação humana

Não foram realizadas visitas nem enviados pedidos ao Município, à UÉ ou a lojas. Uma confirmação operacional de confiança depende de resposta da entidade gestora e/ou observação no local. Este plano, os modelos e a revisão documental ficam prontos para essa recolha; não são resultados de trabalho de campo.

Dados cartográficos: © OpenStreetMap contributors / ODbL, [licença e atribuição](https://www.openstreetmap.org/copyright). Candidatos e limites anteriores: [auditoria documental](water-source-audit-PT.md).
