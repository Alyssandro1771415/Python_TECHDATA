import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import *
import mysql.connector
import janelas
import time
import os


# Tela de cadastramento de projetos.


# Tela cheia.
def full(parametro):
    parametro.state('zoomed')


# conexão ao banco mysql (Dados na treeview).
def databank(treeview):
    try:
        con = mysql.connector.connect(host='localhost', database='projetos', user='root', password='')
        consulta = "select * from projeto order by id"
        cursor = con.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        for v in linhas:
            treeview.insert("", "end", values=v)
        con.close()
        cursor.close()
    except:
        messagebox.showerror(title='Database error.',
                             message='Erro ao tentar estabelecer conexão com o banco de dados.', icon='error')


# Inserindo novos dados no banco.
def new_datas(v0, v1, v2, v3, v4, v5, v6):
    try:
        con = mysql.connector.connect(host='localhost', database='projetos', user='root', password='')
        inserir = f"""INSERT INTO projeto
                       (ID, project, starter_date, end_date, recu_valuer, liquid_valuer, project_doc) 
                       VALUES 
                       ('{v0}', '{v1}', '{v2}', '{v3}', '{v4}', '{v5}', '{v6}')"""
        cursor = con.cursor()
        cursor.execute(inserir)
        con.commit()
        con.close()
        cursor.close()
    except:
        messagebox.showerror(title='Erro de dados.',
                             message='Os dados fornecidos estão incompatíveis, verifique-os e tente novamente.',
                             icon='error')


# Atualizar treeview.
def atualizar(treeview):
    try:
        treeview.delete(*treeview.get_children())

        con = mysql.connector.connect(host='localhost', database='projetos', user='root', password='')
        consulta = "select * from projeto order by id"
        cursor = con.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        for v in linhas:
            treeview.insert("", "end", values=v)
        con.close()
        cursor.close()
    except:
        messagebox.showerror(title='Database error.', message='Erro! verifique se o banco de dados MySQL está ativo.')


# Deletar da treeview.
def deletar(treeview):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="projetos"
    )

    item = treeview.selection()

    valor = treeview.item(item, "values")[0]

    mycursor = mydb.cursor()

    sql = f"DELETE FROM projeto WHERE id = '{valor}';"

    consulta = "select * from projeto order by id"

    mycursor.execute(sql)

    mydb.commit()

    treeview.delete(*treeview.get_children())

    mycursor.execute(consulta)

    linhas = mycursor.fetchall()

    for v in linhas:
        treeview.insert("", "end", values=v)
    mydb.close()

    mycursor.close()


# Atualiza cadstro já existente.
def a_cadastro(ID, P, S_D, E_D, R_V, L_V, P_D):
    conx = mysql.connector.connect(host='localhost', database='projetos', user='root', password='')

    cursor = conx.cursor()

    comando = f"""UPDATE projeto 
    set project = '{P}', starter_date = '{S_D}', end_date = '{E_D}', recu_valuer = '{R_V}', liquid_valuer = '{L_V}', 
    project_doc = '{P_D}' 
    WHERE id = '{ID}';"""

    cursor.execute(comando)

    conx.commit()

    conx.close()

    cursor.close()


# Pesquisar cadstros na treeview.
def pesquisar(treeview, entry):
    try:
        treeview.delete(*treeview.get_children())

        con = mysql.connector.connect(host='localhost', database='projetos', user='root', password='')
        consulta = f"""select * from projeto
        where project like '{entry.get()}%';"""
        cursor = con.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        for v in linhas:
            treeview.insert("", "end", values=v)
        con.close()
        cursor.close()
    except:
        messagebox.showerror(title='Database error.', message='Erro! verifique se o banco de dados MySQL está ativo.')


# Arquivo a uppar.
def dev_arc(lista):
    doc = askopenfilename()
    lista.clear()
    lista.append(doc)


# tela de hisórico de gastos.
def novo_user(d_v, lg, em, sn):
    con = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')
    inserir = f"""INSERT INTO cadastros
                (digito_verificador, LOGIN, EMAIL, SENHA) 
                VALUES 
                ('{d_v}', '{lg}', '{em}', '{sn}')"""
    cursor = con.cursor()
    cursor.execute(inserir)
    con.commit()
    con.close()
    cursor.close()


def validate(login, senha, tela):
    con = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')
    consulta = "select LOGIN, SENHA from cadastros"
    cursor = con.cursor()
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    try:
        for v in linhas:
            if v[0] == login and v[1] == senha:
                janelas.janela1(tela)
    except:
        messagebox.showerror(title='Erro de login.', message='Login ou senha incorretos.', icon='error')
    con.close()
    cursor.close()
