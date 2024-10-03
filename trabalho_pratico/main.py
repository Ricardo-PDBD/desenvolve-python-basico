import json
import os
import re

#definição das classes e dos métodos
arquivo_usuarios = "usuarios.txt"
arquivo_produtos = "produtos.txt"

class Usuario:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

#busca dados dos usuários cadastrados no arquivo usuarios.txt
def carregar_usuarios():
    try:
        with open(arquivo_usuarios, 'r') as file:
            usuarios = file.read()
            
    except FileNotFoundError:
        return []
    
#função para salvar usuários no arquivo usuarios.txt
def salvar_usuarios(usuarios):
    with open(arquivo_usuarios, 'w') as file:
        json.dump([u.__dict__ for u in usuarios], file)

#função para carregar dados dos produtos do arquivo produtos.txt
def carregar_produtos():
    try:
        with open(arquivo_produtos, 'r') as file:
            produtos = file.read()
            
    except FileNotFoundError:
        return []
    
#função para salvar produtos no arquivo produtos.txt
def salvar_produtos(produtos):
    with open(arquivo_produtos, 'w') as file:
        json.dump([p.__dict__ for p in produtos], file)

#Função para executar login
#usuários
def login(usuarios):
    username = input("Usuário: ")
    password = input("Senha: ")

    for usuario in usuarios:
        if usuario.username == username and usuario.password == password:
            print(f"Bem-vindo {usuario.username} ({usuario.role})")
            return usuario
    print("Usuário ou senha incorretos.")
    return None

#gerente
def menu_gerente(usuarios, produtos):
    while True:
        print("\n1. Criar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Gerenciar produtos")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_usuario(usuarios)
        elif opcao == '2':
            listar_usuarios(usuarios)
        elif opcao == '3':
            atualizar_usuario(usuarios)
        elif opcao == '4':
            deletar_usuario(usuarios)
        elif opcao == '5':
            menu_produtos(produtos)
        elif opcao == '0':
            salvar_usuarios
            salvar_produtos
            break
        else:
            print("Opção inválida.")

#funcionário (acesso limitado)
def menu_funcionario(produtos):
    while True:
        print("\n1. Listar produtos")
        print("2. Buscar produtos por nome/código")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_produtos(produtos)
        elif opcao == '2':
            buscar_produtos(produtos)
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

#menu de produtos
def menu_produtos(produtos):
    while True:
        print("\n1. Criar produto")
        print("2. Listar produtos")
        print("3. atualizar produtos")
        print("4. Deletar produtos")
        print("5. Buscar produtos")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_produto(produtos)
        elif opcao == '2':
            listar_produtos(produtos)
        elif opcao == '3':
            atualizar_produto(produtos)
        elif opcao == '4':
            deletar_produto(produtos)
        elif opcao == '5':
            buscar_produtos(produtos)
        elif opcao == '0':
            menu_gerente()
            break
        else:
            print("Opção inválida.")


#função CRUD de usuário
def criar_usuario(usuarios):
    username = input("Novo usuário: ")
    password = input("Nova senha: ")
    role = input("Função (gerente/funcionário): ")
    usuarios.append(Usuario(username, password, role))
    print("Usuário criado com sucesso.")

def listar_usuarios(usuarios):
    print("\nUsuários: ")
    for u in usuarios:
        print(f"Username: {u.username}, Função: {u.role}")

def atualizar_usuario(usuarios):
    username = input("Nome do usuário a ser atualizado: ")
    for u in usuarios:
        if u.username == username:
            u.password = input("Nova senha: ")
            u.role = input("Nova função(gerente/funcionário): ")
            print("Usuário atualizado.")
            return
    print("Usuário não encontrado.")

def deletar_usuario(usuarios):
    username = input("Nome do usuário a ser deletado: ")
    for u in usuarios:
        if u.username == username:
            usuarios.remove(u)
            print("Usuário deletado.")
            return
    print("Usuário não encontrado.")

#Função CRUD de produtos
def criar_produto(produtos):
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    preco = input("Preço: ")
    quantidade = input("Quantidade: ")
    produtos.append(Produto(codigo, nome, preco, quantidade))
    print("Produto criado com sucesso.")

def listar_produtos(produtos):
    print("\nProdutos: ")
    for p in produtos:
        print(f"Código: {p.codigo}, Nome: {p.nome}, Preço: {p.preco}, Quantidade: {p.quantidade}")

def atualizar_produto(produtos):
    codigo = input("Código do produto a ser atualizado: ")
    for p in produtos:
        if p.codigo == codigo:
            p.nome = input("Novo nome: ")
            p.preco = float(input("Novo preço: "))
            p.quantidade = int(input("Nova quantidade: "))
            print("Produto atualizado!")
            return
    print("Produto não encontrado.")

def deletar_produto(produtos):
    codigo = input("Código do produto a ser deletado: ")
    for p in produtos:
        if p.codigo == codigo:
            produtos.remove(p)
            print("Produto deletado!")
            return
    print("Produto não encontrado.")

def buscar_produtos(produtos):
    termo = input("Nome ou código do produto: ")
    for p in produtos:
        if termo in (p.codigo, p.nome):
            print(f"Produto encontrado: Código: {p.codigo}, Nome: {p.nome}, Preço: {p.preco}, Quantidade: {p.quantidade}")
            return
    print("Produto não encontrado.")


#Programa
def main():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()

    usuario_logado = login(usuarios)
    if usuario_logado:
        if usuario_logado.role == 'gerente':
            menu_gerente(usuarios, produtos)
        elif usuario_logado == 'funcionario':
            menu_funcionario(produtos)

if __name__ == "__main__":
    main()