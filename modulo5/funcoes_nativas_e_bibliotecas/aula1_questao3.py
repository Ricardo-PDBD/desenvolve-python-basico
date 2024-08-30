"""
Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.
Exemplo de interação:
Adivinhe o número entre 1 e 10: 5
Muito alto, tente novamente!
Adivinhe o número entre 1 e 10: 3
Correto! O número é 3.

"""
import random

n = random.randint(1,10)
chute = None

print("Advinhe o número entre 1 e 10: ")

while chute != n:
    
    chute = int(input("Escolha o número: "))

    if chute < n:
        print("O número é maior. Tente novamente!")
        continue
    elif chute > n:
        print("O número é menor. Tente de novo!")
        continue
    else:
        print(f"Você acertou! o número é {n}")