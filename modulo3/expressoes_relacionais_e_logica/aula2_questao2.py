"""
2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.
"""

# entrada de dados perguntando idade

idade_juliana = int(input("Qual a idade de Juliana? "))
idade_cris = int(input("Qual a idade de Cris? "))

pode_entrar = idade_juliana >= 18 or idade_cris >= 18 # comparação lógica se um OU outro é verdadeiro

print(pode_entrar) # saída de dados