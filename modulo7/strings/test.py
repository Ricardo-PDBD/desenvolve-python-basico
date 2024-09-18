numero = input("Digite o celular: ")
if len(numero) == 8:
    numero_formatado = "9" + numero

numero_final = f"{numero_formatado[:5]}-{numero_formatado[5:]}"
print("Numero formatado:", numero_final)