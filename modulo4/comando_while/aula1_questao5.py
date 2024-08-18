# entrada de dados perguntando quantos respondentes
n_respondentes = int(input("Digite quantos respondetes são: "))

# variáveis de contrrole
soma = 0
cont = 0

# laço de repetição
while cont < n_respondentes:
    idade = int(input("Digite a idade: "))
    soma += idade
    
    cont += 1

# resultado
print(f"A Média das idade é {soma / 3:,.0f} anos.")