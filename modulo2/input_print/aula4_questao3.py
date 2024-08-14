"""
3) Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:
Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito).
A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
Entrada:
Digite o nome do produto 1: calça
Digite o preço unitário do produto 1: 199.90
Digite a quantidade do produto 1: 3
Digite o nome do produto 2: camisa
Digite o preço unitário do produto 2: 49.95
Digite a quantidade do produto 2: 10
Digite o nome do produto 3: cinto
Digite o preço unitário do produto 3: 25
Digite a quantidade do produto 3: 3

Saída:
Total: R$1,174.20

"""
# produto 1
nomeProduto1        = input("Digite o nome do produto: ")
precoUnitario1      = float(input("Digite o preço do produto: "))
quantidadeProdruto1 = int(input("Digite a quantidade do produto: "))
totalProduto1 = quantidadeProdruto1 * precoUnitario1
# produto 2
nomeProduto2        = input("Digite o nome do produto: ")
precoUnitario2      = float(input("Digite o preço do produto: "))
quantidadeProdruto2 = int(input("Digite a quantidade do produto: "))
totalProduto2 = quantidadeProdruto2 * precoUnitario2
# produto 3
nomeProduto3        = input("Digite o nome do produto: ")
precoUnitario3      = float(input("Digite o preço do produto: "))
quantidadeProdruto3 = int(input("Digite a quantidade do produto: "))
totalProduto3 = quantidadeProdruto3 * precoUnitario3

print(f"Total: R$ {totalProduto1 + totalProduto2 + totalProduto3:,.2f}")