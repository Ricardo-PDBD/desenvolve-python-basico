# entrada de dados solicitando um número ao usuário
n = int(input("Digite um número de 0 a 10: "))

# condição de parada
maior = 0
    
#  comparação
while n > 0:
    if n > 0:
        x = (int(input("Digite outro valor: ")))
        if x > maior:
            maior = x 
            n = n - 1
        else: n = n - 1
    else: print(maior)
print("fim")