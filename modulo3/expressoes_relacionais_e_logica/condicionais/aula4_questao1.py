# 1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão.

# entrada de dados solicitando dois números
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
soma    = numero1 + numero2

# averiguando se a soma é par ou ímpar. Condicionais com resposta.
if soma % 2 == 0:
    print(f"{soma} é par.")
else:
    print(f"{soma} é impar")