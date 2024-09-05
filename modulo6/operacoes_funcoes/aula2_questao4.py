"""
4) Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
Exemplo de interação via terminal (entradas em negrito):
Digite a quantidade de elementos da lista 1: 4
Digite os 4 elementos da lista 1:
1
2
3
4Digite a quantidade de elementos da lista 2: 6
Digite os 6 elementos da lista 2:
5
6
7
8
9
10Lista intercalada: 1 5 2 6 3 7 4 8 9 10
"""
list1, list2 = [], []
elementos1 = (int(input("Digite a quantidade de itens da lista 1: ")))

for i in range(elementos1):
    list1.append(int(input()))

elementos2 = (int(input("Digite a quantidade de itens da lista 2: ")))

for i in range(elementos2):
    list2.append(int(input()))

list3 = []
for index in range(len(list1)):
    list3.append(list1[index])
    list3.append(list2[index])
    

print(list1)
print(list2)
print(list3)
