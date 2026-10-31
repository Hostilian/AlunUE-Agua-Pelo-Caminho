# AlunUÉ · Água pelo caminho

Aplicação em português europeu para explorar pontos de água e planear percursos em Évora, com supermercados e locais culturais opcionais.

Projeto autónomo de Interação Pessoa-Máquina, Universidade de Évora. Autor: Eren Ozturk.

## Executar e verificar

Sem dependências npm, chaves de API ou conta da aplicação.

```sh
python -m http.server 8766 --directory dist
npm test
npm run check
```

Abrir `http://localhost:8766`. Não abrir por `file://`: os módulos JavaScript precisam de HTTP. O alojamento HTTPS permite as funcionalidades de PWA e localização quando suportadas pelo navegador.

## Funções disponíveis

- Pesquisa e filtros de água, supermercados, locais culturais e propostas de lojas.
- Demonstração identificada; os exemplos não são pontos reais de abastecimento.
- Mapa interativo Leaflet com ruas reais, marcadores acessíveis, escolha do início no mapa e alternativa estática.
- Candidatos OpenStreetMap com fonte e estado de verificação. Um registo de mapa não garante água potável gratuita.
- Início manual ou localização opcional, escolha e reordenação de paragens.
- Exportação pedonal para Google Maps em partes que preservam todas as paragens; alternativa por etapa, cópia, partilha ou ficheiro de texto.
- Consultas opcionais de meteorologia e referências culturais.
- Recuperação de falhas através de mensagens claras ou dados guardados com data.
- Sugestões apenas locais; sem mensagens automáticas a terceiros.
- Caderno de investigação em português: consentimento, perguntas neutras, seis tarefas, SUS, importação/exportação local JSON/CSV e análise sem dados inventados.
- Limpeza do percurso com desfazer, confirmação antes de apagar dados, pesquisa sem acentos e gestão de foco por teclado.
- Interface adaptável, foco de teclado, manifesto PWA e interface guardada para utilização limitada sem internet.

## Estrutura

| Pasta | Finalidade |
|---|---|
| `dist/` | Aplicação estática publicável |
| `docs/` | Requisitos, limites e documentação |
| `tests/` | Confiança nos pontos, integridade do percurso e falhas dos serviços |
| `scripts/` | Verificação de ligações e manifesto |
| `.github/workflows/` | Testes e publicação no GitHub Pages |

O mapa usa geometrias reais de Évora, com referências, norte, escala e atribuição. A revisão de fontes municipais está em `docs/water-source-audit-PT.md`; os candidatos também estão em CSV e JSON.

O relatório de dez páginas está em `dist/relatorio-fase1.pdf`. A submissão Moodle é independente de publicar código ou um website. Não existe comprovativo de submissão guardado neste repositório.

## Compatibilidade e limites

O diretório contém 14 candidatos OSM no centro histórico, com fontes e coordenadas, sem confirmação atual de potabilidade, gratuidade, acesso e funcionamento. Não existe rede de lojas aderentes ou comparação atual de preços. A ordenação usa uma estimativa em linha reta; a navegação pelas ruas é calculada pelo Google Maps. Não garante o percurso mais curto, sombra ou acessibilidade.

Os serviços públicos podem limitar pedidos ou falhar. Sem internet, usar dados previamente guardados e itinerário em texto; não existe navegação ou mapa de ruas offline. O invólucro Android com Capacitor está em `android-shell/`, com instruções em `docs/android-PT.md`. A compilação, assinatura de teste e disponibilidade do artefacto são registadas separadamente; instalação em dispositivo, TalkBack e distribuição de produção exigem verificação própria.

A investigação disponível foi reconstruída a partir das recordações do autor. Não se apresentam entrevistas inventadas ou percentagens não medidas; os artefactos provisórios são identificados no relatório.

## Fontes e licenças

Dados OpenStreetMap: © OpenStreetMap contributors / ODbL. Meteorologia Open-Meteo: CC BY 4.0 e termos do serviço. Artigos Wikipédia: termos das páginas de origem. Google Maps: ligações URLs oficiais; não se redistribuem mosaicos. Leaflet 1.9.4 é reutilizado sob BSD-2-Clause, com licença preservada em `dist/vendor/leaflet/LICENSE`; Capacitor e plugins oficiais têm avisos próprios em `android-shell/THIRD_PARTY_NOTICES.md`. Não foi atribuída uma licença de código aberto ao código específico do projeto.

IA generativa apoiou estrutura, tradução, diagramas e código. Não realizou entrevistas nem verificou pontos no terreno.

## Próxima fase

- [Caderno de investigação](https://hostilian.github.io/AlunUE-Agua-Pelo-Caminho/investigacao.html) e [protocolo](docs/usability-protocol-PT.md).
- [Revisão heurística de preparação, assistida por IA](docs/heuristic-review-PT.md); avaliação cruzada humana ainda por realizar.
- [Plano de verificação da água](docs/water-verification-next-phase-PT.md), [ficha de campo](docs/water-field-checklist-PT.md) e [registo dos 14 candidatos](docs/water-field-register-PT.csv).
- [Android: fontes, compilação e limites](docs/android-PT.md).

Os dados iniciais e o relatório submetido da fase 1 mantêm-se identificados. O caderno começa sem sessões; pelo menos cinco pessoas distintas da UÉ, verificação no terreno e revisão humana continuam a exigir participação real. Os rascunhos de contacto não foram enviados.

## APK de teste disponível

[Descarregar APK](https://hostilian.github.io/AlunUE-Agua-Pelo-Caminho/downloads/AlunUE-Android-Teste.apk) · versão 0.1.0-teste, cerca de 6 MB, Android API 24+ / alvo 36. Compilação e assinatura de depuração verificadas; não foi instalado num dispositivo ou emulador. TalkBack e ensaios com pessoas continuam pendentes. SHA-256: `29de661731ea942c85159702227d2bf44c80e7d9f557f8dbfd98c70c3777b7c3`.

A construção e a assinatura de teste não certificam a água, os percursos ou a usabilidade. Consulte a documentação Android antes de distribuir o APK.
