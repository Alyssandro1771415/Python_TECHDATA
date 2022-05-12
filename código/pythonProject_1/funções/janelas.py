from tkinter import *
from tkinter import ttk
import mysql.connector
from funções import funções_config
import os


def janela1(tela):
    tela.destroy()

    janela1 = Tk()
    janela1.title('TECHDATA')
    janela1.iconbitmap("funções/imagens/TECHDT.ico")
    funções_config.full(janela1)
    img = PhotoImage(file="funções/imagens/images.png")
    imgbg = Label(janela1, image=img)
    imgbg.place(x=0, y=0)

    lb = Label(janela1, text='Projeto:', foreground='white', bg='#000c24', font=4)
    lb.grid(column=0, sticky='W', padx=2)
    et = Entry(janela1, width=60, border=3)
    et.grid(column=0, row=0, pady=5, padx=60, sticky='W')

    bt = Button(janela1, width=10, height=1, text='Pesquisar', command=lambda: funções_config.pesquisar(tv, et))
    bt.grid(row=1, sticky='W', padx=5, pady=5)

    # Frame da TreeView
    FR = Frame(janela1, relief="raised", borderwidth=3, width=600, height=600, border=3)
    FR.grid(column=0, row=2)

    tv = ttk.Treeview(FR, columns=(
        'id', 'project', 'starter_date', 'end_date', 'recu_valuer', 'liquid_valuer', 'project_doc'),
                      show='headings', height=13)

    tv.column('id', minwidth=0, width=165)
    tv.column('project', minwidth=0, width=165)
    tv.column('starter_date', minwidth=0, width=165)
    tv.column('end_date', minwidth=0, width=165)
    tv.column('recu_valuer', minwidth=0, width=165)
    tv.column('liquid_valuer', minwidth=0, width=165)
    tv.column('project_doc', minwidth=0, width=165)

    tv.heading('id', text='ID')
    tv.heading('project', text='PROJECT')
    tv.heading('starter_date', text='STARTER DATE')
    tv.heading('end_date', text='END DATE')
    tv.heading('recu_valuer', text='RECU VALUER')
    tv.heading('liquid_valuer', text='LIQUID VALUER')
    tv.heading('project_doc', text='PROJECT_DOC')
    tv.grid(column=0, row=0, pady=5, padx=100)

    # Botão de atalizar, deletar a treeview.
    BT = Button(FR, text='Atualizar', width=10, height=1, command=lambda: funções_config.atualizar(tv))
    BT.grid(column=0, row=1, padx=5, pady=5, sticky='W')

    BT1 = Button(FR, text='Deletar', width=10, height=1, command=lambda: funções_config.deletar(tv))
    BT1.grid(column=0, row=1, padx=5, pady=5)

    BT2 = Button(FR, text='Histórico', width=10, height=1, command=lambda: janela2(janela1))
    BT2.grid(column=0, row=1, padx=5, pady=5, sticky='E')

    # Frame de inserção de novos clientes.
    FR2 = Frame(janela1, relief="raised", borderwidth=6, width=600, height=300, border=5)
    FR2.grid(column=0, row=3, pady=30, padx=30)

    lb0 = Label(FR2, text='ID cad/att:', foreground='green')
    lb0.grid(row=0, column=0, sticky='W', pady=5)
    et0 = Entry(FR2, width=45, border=3, foreground='Blue2')
    et0.grid(row=0, column=1, pady=5)

    lb1 = Label(FR2, text='PROJECT:')
    lb1.grid(row=1, column=0, sticky='W', pady=5)
    et1 = Entry(FR2, width=45, border=3)
    et1.grid(row=1, column=1, pady=5)

    lb2 = Label(FR2, text='STARTER_DATE:')
    lb2.grid(row=2, column=0, sticky='W', pady=5)
    et2 = Entry(FR2, width=45, border=3)
    et2.insert(0, "2000-01-01")
    et2.grid(row=2, column=1, pady=5)

    lb3 = Label(FR2, text='END_DATE:')
    lb3.grid(row=3, column=0, sticky='W', pady=5)
    et3 = Entry(FR2, width=45, border=3)
    et3.insert(0, "2000-01-01")
    et3.grid(row=3, column=1, pady=5)

    lb4 = Label(FR2, text='RECU_VALUER:')
    lb4.grid(row=4, column=0, sticky='W', pady=5)
    et4 = Entry(FR2, width=45, border=3)
    et4.grid(row=4, column=1, pady=5)

    lb5 = Label(FR2, text='LIQUID VALUER:')
    lb5.grid(row=5, column=0, sticky='W', pady=5)
    et5 = Entry(FR2, width=45, border=3)
    et5.grid(row=5, column=1, pady=5)

    lb6 = Label(FR2, text='PROJECT_DOC')
    lb6.grid(row=6, column=0, sticky='W', pady=5)

    arc = []

    UL = Button(FR2, width=30, border=3, text='UPLOAD', command=lambda: funções_config.dev_arc(arc))
    UL.grid(row=6, column=1, pady=5)

    bt1 = Button(FR2, height=1, width=15, text='Cadastrar', command=lambda: funções_config.new_datas(et0.get(),
                                                                                                     et1.get(),
                                                                                                     et2.get(),
                                                                                                     et3.get(),
                                                                                                     et4.get(),
                                                                                                     et5.get(),
                                                                                                     arc[0]))

    bt1.grid(row=8, columnspan=2, pady=5, padx=5, sticky='W')

    bt2 = Button(FR2, height=1, width=15, text='Atualizar cadastro',
                 command=lambda: funções_config.a_cadastro(et0.get(), et1.get(), et2.get(), et3.get(), et4.get(),
                                                           et5.get(), arc[0]))

    bt2.grid(row=8, columnspan=2, pady=5, padx=5, sticky='E')

    # Dados do banco escolhido na treeview.
    funções_config.databank(tv)

    janela1.mainloop()


def janela2(janela):
    janela.destroy()

    janela2 = Tk()
    janela2.title('TECHDATA')
    funções_config.full(janela2)
    janela2.iconbitmap("funções/imagens/TECHDT.ico")

    FR = Frame(janela2, relief="raised", borderwidth=3, width=600, height=500)
    FR.pack(side=TOP)

    tv = ttk.Treeview(FR, columns=('ID foreign', 'VALOR DA COMPRA', 'TIPO DE PRODUTO', 'NOTAS DA COMPRA'),
                      show='headings')
    tv.heading('ID foreign', text="ID foreign")
    tv.heading('VALOR DA COMPRA', text='VALOR DA COMPRA')
    tv.heading('TIPO DE PRODUTO', text='TIPO DE PRODUTO')
    tv.heading('NOTAS DA COMPRA', text='NOTAS DA COMPRA')

    tv.pack(side=TOP)

    janela2.mainloop()