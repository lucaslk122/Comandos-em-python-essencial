class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuarios:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.senha= senha

while True:
    email = input("Digite seu email: ")
    if "@" in email:
        break
    else:
        print("Email invalido, digite novamente")
senha = input("Digite a senha: ")
lista_teste = [senha.replace(senha,"*") for senhai in senha ]
#print(lista_teste)
nova_senha = "".join(lista_teste)
user = Acesso(email, nova_senha)
print(vars(user))