"""
1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.

O terreno possui 250m2 e custa R$512,490.50

Comente na linha acima de cada instrução uma breve descrição da instrução.

Fórmulas:
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2
"""
# entrada de dados 
comprimento = int(input("Digite o comprimento do terreno: "))
largura =  int(input("Digite a largura do terreno: "))
preco_m2 = float(input("Digite o valor do m²: "))

# cálculos de área e valor
area = comprimento * largura #m²
preco_total = area * preco_m2 #valor em Real

# saída de dados formatado com ponto flutuante.
print(f"O terreno possui {area}m² e o preço total é R${preco_total:,.2f}")