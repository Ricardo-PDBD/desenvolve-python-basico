"""
2) Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".
Ex:
Bom
dia
meu
nome
é
Davi
"""
import os
import re

arquivo_frase = "frase.txt"
arquivo_palavras = "palavras.txt"

with open(arquivo_frase, "r") as arquivo:
    conteudo = arquivo.read()

    palavras = re.findall(r'\b[a-zA-ZÀ-ÿ]+\b', conteudo)

with open(arquivo_palavras, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

with open(arquivo_palavras, "r") as arquivo:
    conteudo_palavras = arquivo.read()

print(f"Conteúdo do arquivo 'palavras.txt: {conteudo_palavras}")