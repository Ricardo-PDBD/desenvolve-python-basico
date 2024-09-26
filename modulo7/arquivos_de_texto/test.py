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