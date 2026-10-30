# Gerar os relatórios

Dependências Python: reportlab. Executar `python build_report.py` e `python build_english.py`. Os PDFs são criados em `output/`. Os scripts usam a fonte Arial do Windows, conforme o ambiente de autoria. Noutro sistema, substituir as duas localizações de fontes em `build_report.py` por fontes TrueType disponíveis antes de executar. A aplicação publicada não depende destes scripts nem de Python.

Os diagramas de investigação são vetoriais e conceptuais. O mapa usa geometria real do centro histórico de Évora; não é um itinerário validado. As cores dos gráficos distinguem os três casos; não codificam resultados quantitativos. O relatório tem dez páginas e ligações clicáveis para a aplicação, repositório e fontes.

O mapa usa o extrato `evora-osm.json`, dados © OpenStreetMap contributors / ODbL. Os originais municipais não são redistribuídos. Executar o gerador localmente a partir desta pasta conserva as fontes relativas.
