"""
1) Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
A lista original
Os 3 primeiros elementos
Os 2 últimos elementos
A lista invertida (do fim para o começo)
Os elementos de índice par (0, 2, 4 … )
Os elementos de índice ímpar (1, 3, 5, … )
"""
lista = []

while True:
    entrada = input("Digite um número inteiros (minímo 4 números) ou X para sair.")
    if entrada == "x":
        break
    else:
        lista.append(entrada)
        continue

print(f"A lista original é: {lista}")
print(f"Os 3 primeiros elementos são: {lista[:3]}")
print(f"Os 2 últimos elementos são: {lista[-2:]}")
print(f"A lista invertida é: {lista[::-1]}")
print(f"Os elementos de índice par são: {lista[::2]}")
print(f"Os elementos de índice ímpar são: {lista[1::2]}")