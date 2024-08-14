"""
2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:

86 graus Fahrenheit são 30 graus Celsius.
"""
temperaturaF = float(input("Digite uma temperatudo em Fahrenheit: ")) # entrada pelo usuário
temperaturaC = (temperaturaF - 32) * (5/9) # conversão de temperatura
print(f"{temperaturaF} graus Fahrenheit são {int(temperaturaC)} graus Celsius.") # saída com print formatado