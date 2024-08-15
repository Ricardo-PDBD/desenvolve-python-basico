"""
5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
A: Para mulheres, ter mais de 60 anos. Para homens, 65.
B: Ou ter trabalhado pelo menos 30 anos
C: Ou ter 60 anos  e trabalhado pelo menos 25.
"""

genero = input("Digite f para feminino ou m para masculino: ")
idade  = int(input("qual sua idade? "))
tempo  = int(input("Quantos anos trabalhados? "))

a = (genero == "f" and idade >= 60) or (genero == "m" and idade >= 65)
b = tempo >= 30
c = idade >= 60 and tempo >= 25

pode_aposentar = a or b or c

print(pode_aposentar)