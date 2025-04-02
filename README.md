<h1 align="center">Teste de Web Scraping e Transformação de Dados</h1>

<br>

<h2>Sobre o Projeto 🚀</h2>

Este projeto foi desenvolvido como parte de um desafio técnico, consistindo em três etapas principais:

1. **Download dos PDFs:** Os arquivos PDF são baixados diretamente do site da Agência Nacional de Saúde Suplementar (ANS) utilizando a biblioteca `wget`.
2. **Extração e Processamento de Dados:** As tabelas dos PDFs são extraídas e processadas utilizando a biblioteca `tabula`.
3. **Transformação e Compactação:** Os dados são transformados, salvos em um arquivo CSV e compactados em um arquivo ZIP.

<br>
<h2>Tecnologias Utilizadas 🛠️</h2>

<img align="center" alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>  <img align="center" alt="Tabula" src="https://img.shields.io/badge/Tabula-DC143C?style=for-the-badge&logo=adobeacrobatreader&logoColor=white"/>   <img align="center" alt="Pandas" src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>   <img align="center" alt="Zipfile" src="https://img.shields.io/badge/Zipfile-FFD700?style=for-the-badge&logo=files&logoColor=black"/>   <img align="center" alt="OS" src="https://img.shields.io/badge/OS-808080?style=for-the-badge&logo=linux&logoColor=white"/>  <img align="center" alt="Wget" src="https://img.shields.io/badge/Wget-006699?style=for-the-badge&logo=gnu&logoColor=white"/>  

<br>

<h2>Estrutura do Código 📜</h2>

1. **Download dos PDFs** 📥
   - Os arquivos são baixados automaticamente do site da ANS usando a biblioteca `wget`.
   
2. **Extração e Processamento de Dados** 🔄
   - Todas as tabelas dos PDFs são extraídas utilizando a biblioteca `tabula`.
   - As tabelas são combinadas em um único DataFrame do Pandas.
   - As abreviações "OD" e "AMB" são substituídas por suas descrições completas.
   
3. **Transformação e Compactação** 📦
   - O resultado é salvo em um arquivo CSV.
   - O CSV gerado é compactado em um arquivo ZIP denominado `tabelas_compactadas.zip`.

<br>

<h2>Como Executar o Projeto ▶️</h2>

1. **Instalação das Dependências** ⚙️

Antes de executar o código, certifique-se de que as bibliotecas necessárias estão instaladas:
```
pip install pandas tabula-py wget
```

2. **Execução do Código** 💻

Basta executar o script Python para realizar todas as etapas automaticamente. Ao final, será gerado um arquivo ZIP contendo o CSV processado.

<br>

<h2>Resultado Final 📂</h2>

- **tabela.csv:** Arquivo estruturado contendo os dados das tabelas extraídas dos PDFs.
- **tabelas_compactadas.zip:** Arquivo compactado contendo o CSV final.

Este projeto demonstra uma abordagem automatizada para obtenção, processamento e compactação de dados tabulares extraídos de documentos PDF disponíveis publicamente.
