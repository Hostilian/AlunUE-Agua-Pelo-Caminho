# Validação da atualização — 31/10/2026

- 19 testes automáticos aprovados: confiança dos pontos, falhas de API, integridade da exportação, cache offline, SUS, importação consentida, denominadores, CSV e pesquisa sem acentos.
- Verificação de ficheiros locais, manifesto e sintaxe dos módulos aprovada.
- No navegador: pesquisa `agua` mostra 14 candidatos; plano com duas paragens de demonstração; limpar/desfazer; reordenar com recuperação de foco; origem escolhida numa rua do mapa; caderno com zero sessões e bloqueio sem consentimento.
- Interface principal e caderno observados com largura útil de 375 px, sem transbordo horizontal. Isto não equivale a teste num telemóvel real ou TalkBack.
- SDK Leaflet 1.9.4 reutilizado com licença BSD-2-Clause preservada; scaffold e plugins Android oficiais Capacitor.
- APK de depuração compilado: 5 996 270 bytes; assinatura v2 válida; pacote `pt.alunue.aguapelocaminho`, versão `0.1.0-teste`, API mínima 24 / alvo 36. Equipamento de localização opcional. Sem permissão de localização precisa ou em segundo plano, câmara, microfone ou armazenamento geral.
- SHA-256 do APK: `29de661731ea942c85159702227d2bf44c80e7d9f557f8dbfd98c70c3777b7c3`. As adaptações nativas de ligações e exportação estão documentadas; os módulos funcionais web foram comparados com o conteúdo empacotado. Nenhuma chave privada ou APK recursivo no pacote.
- O PDF submetido da fase 1 permanece inalterado: SHA-256 `21381c498b48dfa3400c73be93b1d88915885b1ff4b76f569d9c300b4f240f45`.

## Por verificar com pessoas e no terreno

Instalação e execução Android; TalkBack; recusa/permissão GPS real; pelo menos cinco estudantes distintos da UÉ; avaliação cruzada humana; potabilidade, custo, acesso e funcionamento dos pontos; adesão explícita das lojas. Não existem novos resultados de participantes, inspeções de campo, parceiros ou notificações automáticas. Os rascunhos de contacto não foram enviados.
