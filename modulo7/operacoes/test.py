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