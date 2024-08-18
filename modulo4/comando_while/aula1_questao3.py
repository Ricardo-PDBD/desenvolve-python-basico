# dados de entrada solicitando notas do aluno
n1, n2, n3 = int(input("Digite nota 1: ")), int(input("Digite nota 2: ")), int(input("Digite nota 3: "))

# soma para descobrir a média das 3 notas
m = (n1 + n2 + n3) / 3

# fluxo de condicionais
if m >= 60:
    print("Aprovado!")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado.")

# fim do programa
print("Fim.")