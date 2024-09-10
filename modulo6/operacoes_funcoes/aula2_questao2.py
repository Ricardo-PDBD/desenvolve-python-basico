"""
2) Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:
A lista elementos
A soma dos valores da lista
A média dos valores da lista
"""
import random

num_elementos = random.randint(5, 20)
elementos = []

for i in range(num_elementos):
    elementos.append(random.randint(1, 10))

soma = sum(elementos)
media = soma / len(elementos)
print(elementos)
print(f"A soma dos elementos dá: {soma}")
print(f"A média dos elementos dá: {(media):.2f}")