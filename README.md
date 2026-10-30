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
- Candidatos OpenStreetMap com fonte e estado de verificação. Um registo de mapa não garante água potável gratuita.
- Início manual ou localização opcional, escolha e reordenação de paragens.
- Exportação pedonal para Google Maps em partes que preservam todas as paragens; alternativa por etapa, cópia, partilha ou ficheiro de texto.
- Consultas opcionais de meteorologia e referências culturais.
- Recuperação de falhas através de mensagens claras ou dados guardados com data.
- Sugestões apenas locais; sem mensagens automáticas a terceiros.
- Interface adaptável, foco de teclado, manifesto PWA e interface guardada para utilização limitada sem internet.

## Estrutura

| Pasta | Finalidade |
|---|---|
| `dist/` | Aplicação estática publicável |
| `docs/` | Requisitos, limites e documentação |
| `tests/` | Confiança nos pontos, integridade do percurso e falhas dos serviços |
| `scripts/` | Verificação de ligações e manifesto |
| `.github/workflows/` | Testes e publicação no GitHub Pages |

O relatório de oito páginas está em `dist/relatorio-fase1.pdf`. A submissão Moodle é independente de publicar código ou um website. Não existe comprovativo de submissão guardado neste repositório.

## Compatibilidade e limites

Não existe diretório de água verificado, rede de lojas aderentes ou comparação atual de preços. A ordenação usa uma estimativa em linha reta; a navegação pelas ruas é calculada pelo Google Maps. Não garante o percurso mais curto, sombra ou acessibilidade.

Os serviços públicos podem limitar pedidos ou falhar. Sem internet, usar dados previamente guardados e itinerário em texto; não existe navegação ou mapa de ruas offline. Instalação em Android, TalkBack e APK assinado ainda exigem verificação no dispositivo. Nenhum APK é apresentado como concluído.

A investigação disponível foi reconstruída a partir das recordações do autor. Não se apresentam entrevistas inventadas ou percentagens não medidas; os artefactos provisórios são identificados no relatório.

## Fontes e licenças

Dados OpenStreetMap: © OpenStreetMap contributors / ODbL. Meteorologia Open-Meteo: CC BY 4.0 e termos do serviço. Artigos Wikipédia: termos das páginas de origem. Google Maps: ligações URLs oficiais; não se redistribuem mosaicos. Não foi atribuída uma licença de código aberto ao código do projeto.

IA generativa apoiou estrutura, tradução, diagramas e código. Não realizou entrevistas nem verificou pontos no terreno.
