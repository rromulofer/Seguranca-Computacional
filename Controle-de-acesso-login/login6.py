# Neste código, eu criei uma função login que é chamada quando o botão de login é clicado.
# Ela obtém o nome de usuário e a senha que foram digitados nos campos de entrada e verifica
# se eles estão corretos. Se estiverem corretos, ela exibe uma caixa de mensagem de sucesso
# e fecha a janela. Caso contrário, ela exibe uma caixa de mensagem de erro e verifica a força
# da senha usando a função check_password_strength.

# Eu também criei uma janela principal usando o tkinter, que contém dois campos de entrada
# para o nome de usuário e senha e um botão de login

import tkinter as tk
from tkinter import messagebox
import getpass

# Dicionário com usuários e senhas
users = {
    "user1": "123",
    "user2": "123",
    "user3": "123"
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

# Função que é chamada quando o botão de login é clicado


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Checa se o usuário e senha estão corretos
    if username in users and users[username] == password:
        messagebox.showinfo("Login successful", "Welcome, " + username + "!")
        root.destroy()  # Fecha a janela
    else:
        messagebox.showerror("Login failed", "Invalid username or password.")

        # Checa a força da senha
        if check_password_strength(password):
            messagebox.showwarning("Password strength",
                                   "Your password is strong!")
        else:
            messagebox.showwarning(
                "Password strength", "Your password should contain at least one uppercase letter, one number, and one symbol.")


# Cria a janela principal
root = tk.Tk()
root.title("Login")

# Cria os widgets
label_username = tk.Label(root, text="Username:")
entry_username = tk.Entry(root)
label_password = tk.Label(root, text="Password:")
entry_password = tk.Entry(root, show="*")
button_login = tk.Button(root, text="Login", command=login)

# Posiciona os widgets na janela
label_username.grid(row=0, column=0, padx=5, pady=5)
entry_username.grid(row=0, column=1, padx=5, pady=5)
label_password.grid(row=1, column=0, padx=5, pady=5)
entry_password.grid(row=1, column=1, padx=5, pady=5)
button_login.grid(row=2, column=1, padx=5, pady=5)

# Inicia o loop principal da janela
root.mainloop()
