"""
3) Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" (link a seguir) e salve em seu computador com o nome "estomago.txt". 

Link: https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt

Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
O texto das primeiras 25 linhas
O número de linhas do arquivo
A linha com maior número de caracteres
O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).
"""
import re

nome_arquivo = "estomago.txt"

linhas = []
num_mencao_nonato = 0
num_mencao_iris = 0

with open(nome_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()

    print("Primeiras 25 linhas: ")
    for linha in linhas[:25]:
        print(linha.strip())

num_linhas = len(linhas)
print(f"O número total de linhas é: {num_linhas}")

linha_maior = max(linhas, key=len).strip()
print(f"Linha com maior número de caracteres é: {linha_maior}")

for linha in linhas:
    num_mencao_nonato += len(re.findall(r'\bNonato\b', linha, re.IGNORECASE))
    num_mencao_iris += len(re.findall(r'\bÍris\b', linha, re.IGNORECASE))

print(f"Número de menções a Nonato: {num_mencao_nonato}")
print(f"Número de menções a Íris: {num_mencao_iris}")