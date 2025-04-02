import wget
import tabula
import pandas as pd
import zipfile
import os

# URLs dos PDFs
urls = [
    ("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf", "Rol_de_procedimentos_Anexo01.pdf"),
    ("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", "Rol_de_procedimentos_Anexo02.pdf")
]

# Baixando ambos os PDFs
for url, filename in urls:
    print(f"Baixando {filename}...")
    wget.download(url, filename)

# Processando apenas o primeiro PDF (Anexo 1)
filename = urls[0][1]  # Pegando o nome do primeiro arquivo baixado
print(f"\nExtraindo tabelas de {filename}...")
tabelas = tabula.read_pdf(filename, pages="all", lattice=True)

# Processando tabelas extraídas
if tabelas:
    tabela_final = pd.concat(tabelas, ignore_index=True)
    
    # Substituição das abreviações
    abreviacoes = {
        "OD": "Odontologia",
        "AMB": "Ambulatorio"
    }
    tabela_final = tabela_final.applymap(lambda x: abreviacoes.get(str(x).strip().upper(), x) if isinstance(x, str) else x)
    
    # Salvando CSV
    nome_csv = "tabela.csv"
    tabela_final.to_csv(nome_csv, index=False, encoding="utf-8-sig")
    print(f"Arquivo {nome_csv} salvo com sucesso!")
    
    # Compactando o CSV em ZIP
    nome_zip = "teste.Bruno.zip"
    with zipfile.ZipFile(nome_zip, 'w') as zipf:
        zipf.write(nome_csv, os.path.basename(nome_csv))
    
    print(f"Arquivo {nome_zip} compactado com sucesso!")
    print("Colunas do DataFrame:", tabela_final.columns)
else:
    print("Nenhuma tabela encontrada no PDF.")
