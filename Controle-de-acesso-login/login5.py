# Neste código, o usuário precisa digitar o nome de usuário e a senha. 
# A senha não aparece na tela enquanto o usuário digita, graças ao uso 
# do módulo getpass. Se o nome de usuário e a senha estiverem corretos,
# o programa exibe "Login successful!" e sai do loop. Caso contrário, 
# ele exibe "Invalid username or password.".

# Além disso, eu criei a função check_password_strength para checar a 
# força da senha. Ela recebe uma senha como argumento e retorna True 
# se a senha contiver pelo menos uma letra maiúscula, um número e um 
# símbolo, ou False caso contrário. Se a senha não for forte o suficiente,
#  o programa exibe "Your password should contain at least one uppercase letter, 
# one number, and one symbol.".

import getpass

# Dicionário com usuários e senhas
users = {
    "user1": "P@ssw0rd!",
    "user2": "12345#abcDEF",
    "user3": "MyS3cr3tP@ss!"
}

# Função para checar a força da senha
def check_password_strength(password):
    has_uppercase = False
    has_number = False
    has_symbol = False
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_number = True
        elif not char.isalnum():
            has_symbol = True
    
    return has_uppercase and has_number and has_symbol

# Loop de login
while True:
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    # Checa se o usuário e senha estão corretos
    if username in users and users[username] == password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password.")

    # Checa a força da senha
    if check_password_strength(password):
        print("Your password is strong!")
    else:
        print("Your password should contain at least one uppercase letter, one number, and one symbol.")