"""
4) Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
Pelo menos 8 caracteres de comprimento.
Contém pelo menos uma letra maiúscula e uma letra minúscula.
Contém pelo menos um número.
Contém pelo menos um caractere especial (por exemplo, @, #, $).
Complete o seguinte código:
def validador_senha(senha):
    #### Escreva a função

# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False
"""
import re

def validador_senha(senha):
    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'[a-z]', senha):
        return False
    if not re.search(r'[0-9]', senha):
        return False
    if not re.search(r'[!@#$%¨&*(),.?":{|<>}]', senha):
        return False
    
    return True

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))