"""
3) Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".Ex:

Digite uma frase (digite "fim" para encerrar): Radar
"Radar" é palíndromo
Digite uma frase (digite "fim" para encerrar): Bom dia!
"Bom dia!" não é palíndromo
Digite uma frase (digite "fim" para encerrar): Ame o poema
"Ame o poema" é palíndromo
Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!
"A Daniela ama a lei? Nada!" é palíndromo
Digite uma frase (digite "fim" para encerrar): fim
"""
import string

def eh_palindromo(frase):
    frase_limpa = ''.join(char.lower() for char in frase if char.isalnum())

while True:
    frase_usuario = input("Digite uma frase (ou 'fim' para encferrar): ")

    if frase_usuario.lower() == "fim":
        break
    if eh_palindromo(frase_usuario):
        print("A frase é um palindromo.")
    else:
        print("A frase não é um palindromo.")