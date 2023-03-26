import random
import string

# função para gerar uma senha forte com letras maiúsculas, minúsculas, números e símbolos
def generate_password():
    length = 12
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

# função para enviar um token de acesso para o usuário
def send_access_token(user):
    token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
    print(f"Token de acesso enviado para {user}: {token}")
    return token

# função para verificar o login com autenticação de dois fatores
def two_factor_auth(user):
    access_granted = False
    while not access_granted:
        password = input("Digite sua senha: ")
        if password != users[user]['password']:
            print("Senha incorreta. Tente novamente.")
            continue
        token = input("Digite o token de acesso enviado para seu email: ")
        if token != users[user]['access_token']:
            print("Token de acesso inválido. Tente novamente.")
            continue
        access_granted = True
    print("Bem-vindo(a)!", user)

# banco de dados de usuários e senhas
users = {
    'user1': {'password': generate_password(), 'access_token': send_access_token('user1')},
    'user2': {'password': generate_password(), 'access_token': send_access_token('user2')},
    'user3': {'password': generate_password(), 'access_token': send_access_token('user3')}
}

# programa principal para login
username = input("Digite seu nome de usuário: ")
if username not in users:
    print("Usuário não encontrado. Tente novamente.")
else:
    print("Olá,", username)
    two_factor_auth(username)
