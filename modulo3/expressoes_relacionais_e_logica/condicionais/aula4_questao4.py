"""
4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
Distância até 100 km: R$1 por kg.
Distância entre 101 e 300 km: R$1.50 por kg.
Distância acima de 300 km: R$2 por kg.
Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg
"""

distancia = float(input("Digite qual a distância(KM): "))
peso = float(input("Digite qual o peso(KG)): "))

a = distancia * 1
b = distancia * 1.5
c = distancia * 2

if distancia <= 100 and peso <= 10:
    print(f"Frete: R${a:,.2f}")
if distancia <= 100 and peso > 10:
    print(f"Frete: R${a + 10:,.2f}")
if (distancia > 100 and distancia < 301) and peso <= 10:
    print(f"Frete: R${b:,.2f}")
if (distancia > 100 and distancia < 301) and peso > 10:
    print(f"Frete: R${b + 10:,.2f}")
if distancia > 300 and peso <= 10:
    print(f"Frete: R${c:,.2f}")
if distancia > 300 and peso > 10:
    print(f"Frete: R${c + 10:,.2f}")
