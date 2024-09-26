"""
4) Vamos fazer o jogo da forca! Antes de programar crie e salve os seguintes arquivos na mesma pasta onde você vai programar a solução: 
Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.
Baixe o arquivo "gabarito_enforcado.txt": https://github.com/camilalaranjeira/python-basico-exercicios/blob/main/modulo7/gabarito_enforcado.txt
Escreva um programa em Python para executar o jogo, de acordo com as definições:
Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
No início exiba o número de letras da palavra sorteada como underscores;
Permita que o jogador insira letras para adivinhar a palavra;
Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
Limite o número de tentativas para 6 (as partes do enforcado).
"""
import random

def escolher_palavra(arquivo):
    try:
        with open(arquivo, 'r') as file:
            palavras = file.read().splitlines()
            palavra_escolhida = random.choice(palavras)
            return palavra_escolhida
    except FileNotFoundError:
        print(f"Erro: Oarquivo '{arquivo}' não foi encontrado.")
        return None

def carregar_estagios(arquivo):
    try:
        with open(arquivo, 'r') as file:
            estagios = file.read().splitlines()
            return estagios
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return []
    
def imprime_enforcado(estagios, tentativas):
    print(estagios[tentativas])

def jogo():
    palavra = escolher_palavra("gabarito_forca.txt")
    estagios = carregar_estagios("gabarito_enforcado.txt")

    if not palavra or not estagios:
        return
    
    letras_adinhadas = []
    tentativas = 0
    max_tentativas = 6
    palavra_oculta = ["_"] * len(palavra)

    print("Bem vindo ao jogo do Enforcado!")
    print("Adivinhe a palavra: " + " ".join(palavra_oculta))

    while tentativas < max_tentativas and "_" in palavra_oculta:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_adinhadas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        letras_adinhadas.append(letra)

        if letra in palavra:
            print("Você acertou uma letra!")
            for i, l in enumerate(palavra):
                if l == letra:
                    palavra_oculta[i] = letra
        else:
            print("Letra incorreta!")
            tentativas += 1
            imprime_enforcado(estagios, tentativas)

        print("Adivinhe a palavra: " + " ".join(palavra_oculta))
    
    if "_" not in palavra_oculta:
        print("Parabéns! Você adivinhou a palavra: " + palavra)
    else:
        print("Você perdeu! A palavra era: " + palavra)

if __name__ == "__main__":
    jogo()


