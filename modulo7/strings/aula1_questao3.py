"""
Escreva um script que dado uma frase conta os espaços em branco.
Digite a frase: Meu amor mora em Roma e me deu um ramo de flores
Espaços em branco: 11

"""
frase = "Meu amor mora em Roma e me deu um ramo de flores"
espacos_em_branco = 0

for i in frase:
    if i == " ":
        espacos_em_branco += 1

print(f"Espaços em branco: {espacos_em_branco}")