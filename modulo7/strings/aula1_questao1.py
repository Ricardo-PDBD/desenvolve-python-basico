"""
Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.
Digite seu nome: Fulano
F
Fu
Ful
Fula
Fulan
Fulano

"""
nome = input("Digite seu nome: ")
for l in range(len(nome)):
    print(nome[:l + 1])