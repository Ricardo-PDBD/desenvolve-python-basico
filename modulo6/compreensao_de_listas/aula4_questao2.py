"""
2) Solicite uma frase do usuário e usando compreensão de listas imprima:
A lista de vogais da frase, ordenada alfabeticamente
A lista de consoantes da frase
Exemplo:
Digite uma frase: Eu gosto de programar em Python
Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']
"""
#Solicitação ao usuário
frase = input("Digite uma frase: ")

#definindo vogais e consoantes
vog = "aeiou"
cons = "bcdfghjklmnpqrstvwxyz"

#listas 
list_vog = sorted([l for l in frase if l in vog])
list_cons = [l for l in frase if l in cons]

#saida de dados
print(f"Lista de vogais: {list_vog}")
print(f"Lista de consoantes: {list_cons}")