# Importando as bibliotecas necessárias
import hashlib
import getpass

# Dicionário de usuários e senhas
users = {"user1": "password1", "user2": "password2", "user3": "password3"}

# Sistema de segurança 1: criptografia SHA256


def sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Sistema de segurança 2: encriptação por salt


def encrypt_with_salt(password):
    salt = b'\xb3\xeaW*\x8f\x86\x0e^\xf2"\x9b\xe8t\xff\x0c'
    password = password.encode() + salt
    return hashlib.sha256(password).hexdigest()

# Sistema de segurança 3: exigir senha forte


def strong_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True


# Login do usuário
username = input("Digite seu nome de usuário: ")
password = getpass.getpass("Digite sua senha: ")

if username in users:
    stored_password = users[username]

    # Verifica a senha com os três sistemas de segurança
    if sha256(password) == stored_password or encrypt_with_salt(password) == stored_password or (strong_password(password) and password == stored_password):
        print("Login bem sucedido!")
    else:
        print("Senha incorreta.")
else:
    print("Usuário não encontrado.")
