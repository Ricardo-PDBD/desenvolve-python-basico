"""
2) Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
Ex:
Digite uma frase: O rato roeu a roupa do rei
Frase modificada: * r*t* r*** * r**p* d* r**
"""
frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"

frase_modificada = ''.join(['*' if letra in vogais else letra for letra in frase])

print(frase_modificada)