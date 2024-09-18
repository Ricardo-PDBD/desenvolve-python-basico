"""
Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.
Digite seu primeiro nome: Alice
Digite seu sobrenome: Silva
Bem-vinda, Alice Silva! 

"""
nome, sobrenome = input("Digite seu primeiro nome: "), input("Digite seu sobrenome: ")
print(f"Bem vindo(a), {nome} {sobrenome}.")