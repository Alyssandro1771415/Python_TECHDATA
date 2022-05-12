import tkinter.messagebox
from tkinter import *
from funções import funções_config, janelas
from tkinter import ttk
import mysql.connector
import time
import os


def format_cpf(event=None):
    text = et_identificador.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    et_identificador.delete(0, "end")
    et_identificador.insert(0, new_text)


# Tela principal.
Tela_login = Tk()
Tela_login.title('Login.')
funções_config.full(Tela_login)
Tela_login.iconbitmap("funções/imagens/TECHDT.ico")
Tela_login.config(bg='cyan')

# Frame de cadastro.

frame2 = Frame(Tela_login, width=650, height=700, relief='raised', borderwidth=6, pady=10, padx=10)
frame2.pack(anchor=N)

cabeca = Label(frame2, text='LOGIN', width=10, font=('argparse', 25))
cabeca.grid(column=0, row=0, pady=20, columnspan=2)

Login2 = Label(frame2, text='LOGIN:', padx=5, pady=5)
Login2.grid(column=0, row=1, pady=5, padx=5, sticky='W')
et_login2 = Entry(frame2, width=30, border=3)
et_login2.grid(column=1, row=1)

Senha2 = Label(frame2, text='PASSWORD:', padx=5, pady=5)
Senha2.grid(column=0, row=2, pady=4, padx=5, sticky='W')
et_senha2 = Entry(frame2, width=30, border=3, show='*')
et_senha2.grid(column=1, row=2)

NewWindow = Button(frame2, text='Janela 1', width=10, height=2, command=lambda: funções_config.validate(et_login2.get(),
                                                                                                        et_senha2.get(),
                                                                                                        Tela_login))
NewWindow.grid(columnspan=2, row=4)

frame = Frame(Tela_login, width=650, height=700, relief='raised', borderwidth=6, pady=10, padx=10)
frame.pack(anchor=N)

cabeca = Label(frame, text='CADASTRO', width=10, font=('argparse', 25))
cabeca.grid(column=0, row=0, pady=20, columnspan=2)

identificador = Label(frame, text='CFP/CNPJ/SETOR:', padx=5, pady=5)
identificador.grid(column=0, row=1, pady=5, padx=5, sticky='W')
et_identificador = Entry(frame, width=30, border=3)
et_identificador.bind("<KeyRelease>", format_cpf)
et_identificador.grid(column=1, row=1)

Login = Label(frame, text='LOGIN:', padx=5, pady=5)
Login.grid(column=0, row=2, pady=5, padx=5, sticky='W')
et_login = Entry(frame, width=30, border=3)
et_login.grid(column=1, row=2)

Email = Label(frame, text='EMAIL:', padx=5, pady=5)
Email.grid(column=0, row=3, pady=5, padx=5, sticky='W')
et_email = Entry(frame, width=30, border=3)
et_email.grid(column=1, row=3)

Senha = Label(frame, text='PASSWORD:', padx=5, pady=5)
Senha.grid(column=0, row=4, pady=4, padx=5, sticky='W')
et_senha = Entry(frame, width=30, border=3, show='*')
et_senha.grid(column=1, row=4)

senha_confirm = Label(frame, text='CONFIRM PASSWORD:', padx=5, pady=5)
senha_confirm.grid(column=0, row=5, pady=5, padx=5, sticky='W')
et_confirma = Entry(frame, width=30, border=3, show='*')
et_confirma.grid(column=1, row=5)


mostrar = Button(frame, text='Mostrar', command=lambda:[et_senha.config(show=''), et_confirma.config(show='')])
mostrar.grid(column=3, row=4)
mostrar1 = Button(frame, text='Esconder', command=lambda:[et_senha.config(show='*'), et_confirma.config(show='*')])
mostrar1.grid(column=3, row=5)

botao = Button(frame, text='CADASTRAR', border=3, command=lambda: funções_config.novo_user(et_identificador.get(),
                                                                                           et_login.get(),
                                                                                           et_email.get(),
                                                                                           et_senha.get()))
botao.grid(column=0, row=6, columnspan=2)

Tela_login.mainloop()