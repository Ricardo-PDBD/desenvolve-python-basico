import os

# Definição das classes e dos métodos
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

# Busca dados dos usuários cadastrados no arquivo usuarios.txt
def carregar_usuarios():
    usuarios = []
    try:
        with open(arquivo_usuarios, 'r') as file:
            for linha in file:
                username, password, role = linha.strip().split(', ')
                usuarios.append(Usuario(username, password, role))
    except FileNotFoundError:
        pass
    return usuarios

# Função para salvar usuários no arquivo usuarios.txt
def salvar_usuarios(usuarios):
    with open(arquivo_usuarios, 'w') as file:
        for u in usuarios:
            file.write(f"{u.username}, {u.password}, {u.role}\n")

# Função para carregar dados dos produtos do arquivo produtos.txt
def carregar_produtos():
    produtos = []
    try:
        with open(arquivo_produtos, 'r') as file:
            for linha in file:
                codigo, nome, preco, quantidade = linha.strip().split(', ')
                produtos.append(Produto(codigo, nome, float(preco.replace('R$', '')), int(quantidade)))
    except FileNotFoundError:
        pass
    return produtos

# Função para salvar produtos no arquivo produtos.txt
def salvar_produtos(produtos):
    with open(arquivo_produtos, 'w') as file:
        for p in produtos:
            file.write(f"{p.codigo}, {p.nome}, R${p.preco:.2f}, {p.quantidade}\n")

# Função para executar login
def login(usuarios):
    username = input("Usuário: ")
    password = input("Senha: ")

    for usuario in usuarios:
        if usuario.username == username and usuario.password == password:
            print(f"Bem-vindo {usuario.username} ({usuario.role})")
            return usuario
    print("Usuário ou senha incorretos.")
    return None

# Menu do gerente
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
            listar_usuarios(usuarios)
        elif opcao == '2':
            listar_usuarios(usuarios)
        elif opcao == '3':
            atualizar_usuario(usuarios)
            listar_usuarios(usuarios)
        elif opcao == '4':
            deletar_usuario(usuarios)
            listar_usuarios(usuarios)
        elif opcao == '5':
            menu_produtos(produtos)
        elif opcao == '0':
            salvar_usuarios(usuarios)
            salvar_produtos(produtos)
            break
        else:
            print("Opção inválida.")

# Menu do funcionário (acesso limitado)
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

# Menu de produtos
def menu_produtos(produtos):
    while True:
        print("\n1. Criar produto")
        print("2. Listar produtos")
        print("3. Atualizar produtos")
        print("4. Deletar produtos")
        print("5. Buscar produtos")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_produto(produtos)
            listar_produtos(produtos)
        elif opcao == '2':
            listar_produtos(produtos)
        elif opcao == '3':
            atualizar_produto(produtos)
            listar_produtos(produtos)
        elif opcao == '4':
            deletar_produto(produtos)
            listar_produtos(produtos)
        elif opcao == '5':
            buscar_produtos(produtos)
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

# Função CRUD de usuário
def criar_usuario(usuarios):
    username = input("Novo usuário: ")
    password = input("Nova senha: ")
    role = input("Função (gerente/funcionário): ")
    usuarios.append(Usuario(username, password, role))
    salvar_usuarios(usuarios)
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
            u.role = input("Nova função (gerente/funcionário): ")
            salvar_usuarios(usuarios)
            print("Usuário atualizado.")
            return
    print("Usuário não encontrado.")

def deletar_usuario(usuarios):
    username = input("Nome do usuário a ser deletado: ")
    for u in usuarios:
        if u.username == username:
            usuarios.remove(u)
            salvar_usuarios(usuarios)
            print("Usuário deletado.")
            return
    print("Usuário não encontrado.")

# Função CRUD de produtos
def criar_produto(produtos):
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    preco = float(input("Preço: ").replace('R$', ''))
    quantidade = int(input("Quantidade: "))
    produtos.append(Produto(codigo, nome, preco, quantidade))
    salvar_produtos(produtos)
    print("Produto criado com sucesso.")

def listar_produtos(produtos):
    print("\nProdutos: ")
    for p in produtos:
        print(f"Código: {p.codigo}, Nome: {p.nome}, Preço: R${p.preco:.2f}, Quantidade: {p.quantidade}")

def atualizar_produto(produtos):
    codigo = input("Código do produto a ser atualizado: ")
    for p in produtos:
        if p.codigo == codigo:
            p.nome = input("Novo nome: ")
            p.preco = float(input("Novo preço: ").replace('R$', ''))
            p.quantidade = int(input("Nova quantidade: "))
            salvar_produtos(produtos)
            print("Produto atualizado!")
            return
    print("Produto não encontrado.")

def deletar_produto(produtos):
    codigo = input("Código do produto a ser deletado: ")
    for p in produtos:
        if p.codigo == codigo:
            produtos.remove(p)
            salvar_produtos(produtos)
            print("Produto deletado!")
            return
    print("Produto não encontrado.")

def buscar_produtos(produtos):
    termo = input("Nome ou código do produto: ")
    for p in produtos:
        if termo in (p.codigo, p.nome):
            print(f"Produto encontrado: Código: {p.codigo}, Nome: {p.nome}, Preço: R${p.preco:.2f}, Quantidade: {p.quantidade}")
            return
    print("Produto não encontrado.")

# Programa
def main():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()

    usuario_logado = login(usuarios)
    if usuario_logado:
        if usuario_logado.role == 'gerente':
            menu_gerente(usuarios, produtos)
        elif usuario_logado.role == 'funcionario':
            menu_funcionario(produtos)

if __name__ == "__main__":
    main()