"""
3) Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
Ambas as listas
A lista intersecção ordenada
A quantidade de vezes que cada elemento aparece em cada lista
Atenção, a lista de intersecções não pode ter duplicatas. Segue um exemplo da saída esperada.
lista1 - [10, 10, 28, 10, 29, 20, 30, 10, 29, 11]
lista2 - [11, 16, 26, 44, 11, 10, 20, 29, 10, 12]
Interseccao - [10, 11, 20]
Contagem
10: (lista1=4, lista2=1)
11: (lista1=1, lista2=2)
20: (lista1=1, lista2=1)
"""
import random

list1, list2 = [], []

for i in range(10):
    list1.append(random.randint(0, 50))
    list2.append(random.randint(0, 50))

print(sorted(list1))
print(sorted(list2))

inters = []

for elemento in list1:
    if elemento in list2 and elemento not in inters:
        inters.append(elemento)

inters.sort()
for i in inters:
    print(f"{i}: ({list1.count(i)}, {list2.count(i)})")