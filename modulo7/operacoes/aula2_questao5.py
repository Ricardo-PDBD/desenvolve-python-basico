"""
5) De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras embaralhadas, contanto que a primeira e a última letra estejam no lugar correto. Implemente uma função chamada embaralhar_palavras() para ajudar a testar a hipótese do Matt Davis. Sua função vai receber uma frase, embaralhar as letras internas de cada palavra e retornar a frase modificada. Dica: use a biblioteca random.

Complete o seguinte código:
def embaralhar_palavras(frase):
    #### Escreva a função

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"
"""
import random

def embaralha_palavras(frase):
    palavras = frase.split()
    palavras_embaralhadas = []

    for palavra in palavras:
        if len(palavra) <= 3:
            palavras_embaralhadas.append(palavra)
        else:
            primeir_letra = palavra[0]
            ultima_letra = palavra[-1]
            meio = list(palavra[1:-1])
            random.shuffle(meio)

            nova_palavra = primeir_letra + ''.join(meio) + ultima_letra
            palavras_embaralhadas.append(nova_palavra)
    return ' '.join(palavras_embaralhadas)

frase_input = input("Digite uma frase: ")
resultado = embaralha_palavras(frase_input)
print("Frase embaralhada:", resultado)