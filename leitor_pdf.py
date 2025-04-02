#1° Bibliotecas:
import tabula
import pandas as pd
import zipfile
import os

#2° Extração de todas as tabelas do PDF:
lista_tabelas = tabula.read_pdf("anexorol.pdf", pages="all", lattice=True)

#3° Junção de todas as tabelas em um DataFrame:
tabela_juntas = pd.concat(lista_tabelas, ignore_index=True)

#4° Substituição das abreviações "OD" e "AMB" pelas descrições completas:
abreviacoes = {
  "OD": "Odontologia",
  "AMB": "Ambulatorio"
}

tabela_juntas = tabela_juntas.applymap(lambda x: abreviacoes.get(str(x).strip().upper(), x) if isinstance(x, str) else x)

#5° Salvando arquivo CSV:
tabela_juntas.to_csv("tabela.csv", index=False, encoding="utf-8-sig")
print("Todos os arquivos da tabela.csv foram salvos com sucesso!")

#6° Compactar o arquivo CSV em ZIP:
nome_arquivo_zip = "teste_Bruno_Torres.zip" 
with zipfile.ZipFile(nome_arquivo_zip, 'w') as zipf:
  zipf.write("tabela.csv", os.path.basename("tabela.csv"))

print(f"arquivo {nome_arquivo_zip} foi compactado com sucesso!")

print(tabela_juntas.columns)



