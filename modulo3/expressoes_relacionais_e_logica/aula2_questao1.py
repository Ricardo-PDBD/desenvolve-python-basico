"""
1) Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no bar, e False caso contrário.
"""

# entrada de dados perguntando idade

idade_juliana = int(input("Qual a idade de Juliana? "))
idade_cris = int(input("Qual a idade de Cris? "))

pode_entrar = idade_juliana >= 18 and idade_cris >= 18 # comparação lógica se AMBOS são verdadeiros

print(pode_entrar) # saída de dados