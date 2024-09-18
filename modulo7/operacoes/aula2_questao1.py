"""
Instruções para submissão: Para cada questão, crie no VSCode um arquivo chamado aula2_questaoX.py, sendo X o número da questão. Faça commit de todos os arquivos para a pasta modulo7 do seu repositório da disciplina no GitHub. Marque a atividade como resolvida somente após submeter os arquivos no seu repositório no GitHub.

1) Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
Dica: usando listas você não precisa fazer um "if" para cada mês.
Ex:
Digite uma data de nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""
meses = {
    "01": "janeiro",
    "02": "fevereiro",
    "03": "março",
    "04": "abril",
    "05": "maio",
    "06": "junho",
    "07": "julho",
    "08": "agosto",
    "09": "setembro",
    "10": "outubro",
    "11": "novembro",
    "12": "dezembro"
}

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

dia, mes, ano = data_nascimento.split("/")

mes_nome = meses.get(mes)

if mes_nome:
    print(f"Você nasceu em {dia} de {mes_nome} de {ano}.")