"""
Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a seguir:
Data: 15/03/2023 
Hora: 14:05


Você pode consultar esse tutorial da Alura sobre a biblioteca datetime. Existem várias maneiras de resolver essa questão. Uma sugestão é:
Função datetime.datetime.now() cujo retorno possui os atributos: day, month, year, hour, minute
Usar a formatação com f-strings no momento de imprimir. Atenção para os atributos que devem sempre ter 2 dígitos precedidos por zero se necessário.

"""

import datetime

data_e_hora_atuais = datetime.datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

print(data_e_hora_em_texto)

