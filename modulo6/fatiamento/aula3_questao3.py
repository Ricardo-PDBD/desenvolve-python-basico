"""
3) Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.

Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]
"""

import random

# gerando lista
lista = [random.randint(-10, 10) for _ in range(20)]

print(f"Lista origial: {lista}")

inicio_fatia_maior, tam_fatia_maior = 0, 0
inicio_fatia_atual, tam_fatia_atual = 0, 0

for i in range(len(lista)):
    if lista[i] < 0:
        tam_fatia_atual += 1
        if tam_fatia_atual == 1:
            inicio_fatia_atual = i
    else:
        if tam_fatia_atual > tam_fatia_maior:
            tam_fatia_maior = tam_fatia_atual
            inicio_fatia_maior = inicio_fatia_atual
        tam_fatia_atual = 0

del lista[inicio_fatia_maior:inicio_fatia_maior+tam_fatia_maior]
print(f"Lista fatiada: {lista}")