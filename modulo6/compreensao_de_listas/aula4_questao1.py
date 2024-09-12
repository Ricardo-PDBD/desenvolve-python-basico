"""
1) Escreva um script python que use compreensão de listas para criar as seguintes listas:
Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
Todos os números entre 1 e 100 que sejam divisíveis por 7
Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex: ['par', 'impar',… , 'impar']) 

"""
#números pares entre 20 e 50
pares = [num for num in range(20,51) if num % 2 == 0]
print(pares)

#os quadrados dos números de 1 a 9
val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [x**2 for x in val]
print(quadrados)

#todos números divisíveis por 7 entre 1 e 100
divi_7 = [num for num in range(1, 101) if num % 7 == 0]
print(divi_7)

#imprimindo par ou ímpar dependendo do elemento
paridade = ["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]
print(paridade)