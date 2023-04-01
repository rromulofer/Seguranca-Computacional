# Este exemplo usa a biblioteca hashlib para gerar um hash da senha 
# inserida pelo usuário, em vez de armazenar a senha em texto simples. 
# Em seguida, verifica se o nome de usuário e a senha correspondem aos 
# valores definidos como válidos. Em seguida, há três verificações de 
# segurança adicionais:

# Limite de tentativas de login: se o usuário inserir o nome de usuário 
# ou a senha incorretos três vezes seguidas, o programa exibirá uma mensagem 
# de erro e encerrará.
# Comprimento mínimo da senha: a senha deve ter pelo menos 8 caracteres. 
# Se o usuário inserir uma senha com menos de 8 caracteres, o programa

# Importar biblioteca para geração de hash de senha
import hashlib

# Definir nome de usuário e senha válidos
valid_username = "romulo"
valid_password = "Romulo@123"

# Solicitar entrada do usuário
username = input("Digite seu nome de usuário: ")
password = input("Digite sua senha: ")

# Gerar hash da senha inserida pelo usuário
hash_object = hashlib.sha256(password.encode())
hashed_password = hash_object.hexdigest()

# Verificar se o nome de usuário e a senha estão corretos
if username == valid_username and hashed_password == hashlib.sha256(valid_password.encode()).hexdigest():
    print("Login bem sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")

# Verificação de segurança 1: Limitar tentativas de login
attempts = 0
while attempts < 3:
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")
    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.hexdigest()

    if username == valid_username and hashed_password == hashlib.sha256(valid_password.encode()).hexdigest():
        print("Login bem sucedido!")
        break
    else:
        print("Nome de usuário ou senha incorretos.")
        attempts += 1
else:
    print("Você excedeu o número máximo de tentativas.")

# Verificação de segurança 2: Verificar comprimento da senha
while True:
    password = input("Digite uma senha com pelo menos 8 caracteres: ")
    if len(password) >= 8:
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()

        if username == valid_username and hashed_password == hashlib.sha256(valid_password.encode()).hexdigest():
            print("Login bem sucedido!")
            break
        else:
            print("Nome de usuário ou senha incorretos.")
    else:
        print("A senha deve ter pelo menos 8 caracteres.")

# Verificação de segurança 3: Verificar se a senha contém caracteres especiais
special_characters = "!@#$%^&*()_+-=[]{}|;':\"<>,.?/~`"
while True:
    password = input("Digite uma senha com pelo menos 8 caracteres e pelo menos um caractere especial: ")
    if len(password) >= 8 and any(char in special_characters for char in password):
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()

        if username == valid_username and hashed_password == hashlib.sha256(valid_password.encode()).hexdigest():
            print("Login bem sucedido!")
            break
        else:
            print("Nome de usuário ou senha incorretos.")
    else:
        print("A senha deve ter pelo menos 8 caracteres e pelo menos um caractere especial.")