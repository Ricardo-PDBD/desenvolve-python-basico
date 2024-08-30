"""
Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.
	Exemplo de interação:
Digite o primeiro número: 3.1415
Digite o segundo número: 1.4142
A diferença absoluta entre os números é: 1.73

"""
num1 = float(input("Digite um número decimal: "))
num2 = float(input("Digite outro número decimal: "))
sub = abs(num1 - num2)

print(f"A diferença absoluta entre os número é: {round(sub,2)}")