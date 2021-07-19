from utils.modulos import *


class AddAdvogado:
    def __init__(self, master=None, app=None):

        imgbtn11 = PhotoImage(file='imagens/imgAddAdv.png')  # imagem do botão Adicionar
        imgbtn12 = PhotoImage(file='imagens/imgRmvAdv.png')  # imagem do botão Remover
        imgbtn13 = PhotoImage(file='imagens/imgListarAdv.png')  # imagem do botão Listar
        imgbtn14 = PhotoImage(file='imagens/imgEditarAdv.png')  # imagem do botão Editar
        imgbtn15 = PhotoImage(file='imagens/imgFechar.png')  # imagem do botão Editar

        self.janela = False

        if app is not None:
            self.master = master
            self.app = app

        else:
            self.master = Toplevel(master)

        self.__frameAdvogados = Frame(self.master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')

        self.__lblAdvNome = Label(self.__frameAdvogados, text='Nome', bg='LightSteelBlue3')
        self.__lblAdvNome['font'] = 'Serif', '12'
        self.__lblAdvNome.place(x=35, y=20)

        self.__txtAdvNome = Entry(self.__frameAdvogados, width=80)
        self.__txtAdvNome.place(x=100, y=20)

        self.__lblAdvEndereco = Label(self.__frameAdvogados, text='Endereço', bg='LightSteelBlue3')
        self.__lblAdvEndereco['font'] = 'Serif', '12'
        self.__lblAdvEndereco.place(x=10, y=50)

        self.__txtAdvEndereco = Entry(self.__frameAdvogados, width=80)
        self.__txtAdvEndereco.place(x=100, y=50)

        self.__lblAdvCidadeUf = Label(self.__frameAdvogados, text='Cidade/UF', bg='LightSteelBlue3')
        self.__lblAdvCidadeUf['font'] = 'Serif', '12'
        self.__lblAdvCidadeUf.place(x=10, y=80)

        self.__txtAdvCidadeUf = Entry(self.__frameAdvogados, width=40)
        self.__txtAdvCidadeUf.place(x=100, y=80)

        self.__lblAdvCep = Label(self.__frameAdvogados, text='CEP', bg='LightSteelBlue3')
        self.__lblAdvCep['font'] = 'Serif', '12'
        self.__lblAdvCep.place(x=450, y=80)

        self.__txtAdvCep = Entry(self.__frameAdvogados, width=30)
        self.__txtAdvCep.place(x=500, y=80)

        self.__lblAdvFax = Label(self.__frameAdvogados, text='FAX', bg='LightSteelBlue3')
        self.__lblAdvFax['font'] = 'Serif', '12'
        self.__lblAdvFax.place(x=50, y=110)

        self.__txtAdvFax = Entry(self.__frameAdvogados, width=30)
        self.__txtAdvFax.place(x=100, y=110)

        self.__lblAdvTel = Label(self.__frameAdvogados, text='Tel. Comercial', bg='LightSteelBlue3')
        self.__lblAdvTel['font'] = 'Serif', '12'
        self.__lblAdvTel.place(x=370, y=110)

        self.__txtAdvTel = Entry(self.__frameAdvogados, width=30)
        self.__txtAdvTel.place(x=500, y=110)

        self.__lblAdvEmail = Label(self.__frameAdvogados, text='Email', bg='LightSteelBlue3')
        self.__lblAdvEmail['font'] = 'Serif', '12'
        self.__lblAdvEmail.place(x=30, y=140)

        self.__txtAdvEmail = Entry(self.__frameAdvogados, width=80)
        self.__txtAdvEmail.place(x=100, y=140)

        self.__lblAdvOAB = Label(self.__frameAdvogados, text='N° OAB', bg='LightSteelBlue3')
        self.__lblAdvOAB['font'] = 'Serif', '12'
        self.__lblAdvOAB.place(x=30, y=170)

        self.__txtAdvOAB = Entry(self.__frameAdvogados, width=30)
        self.__txtAdvOAB.place(x=100, y=170)

        self.__lblAdvCPF = Label(self.__frameAdvogados, text='CPF', bg='LightSteelBlue3')
        self.__lblAdvCPF['font'] = 'Serif', '12'
        self.__lblAdvCPF.place(x=450, y=170)

        self.__txtAdvCPF = Entry(self.__frameAdvogados, width=30)
        self.__txtAdvCPF.place(x=500, y=170)

        self.__colunas = ('#1', '#2', '#3', '#4', '#5')
        self.__tvOcorrencias = ttk.Treeview(self.__frameAdvogados, columns=self.__colunas, selectmode='browse',
                                            height=5)

        self.__tvOcorrencias.heading('#0', text='')
        self.__tvOcorrencias.heading('#1', text='Nome')
        self.__tvOcorrencias.heading('#2', text='Endereço')
        self.__tvOcorrencias.heading('#3', text='CPF')
        self.__tvOcorrencias.heading('#4', text='OAB')
        self.__tvOcorrencias.heading('#5', text='Telefone/FAX')

        self.__tvOcorrencias.column('#0', width=0, stretch=NO)
        self.__tvOcorrencias.column('#1', width=200, anchor='center')
        self.__tvOcorrencias.column('#2', width=200, anchor='center')
        self.__tvOcorrencias.column('#3', width=100, anchor='center')
        self.__tvOcorrencias.column('#4', width=100, anchor='center')
        self.__tvOcorrencias.column('#5', width=150, anchor='center')

        self.__tvOcorrencias.place(x=20, y=220)

        self.__btnAddAdv = Button(self.__frameAdvogados,
                                  text='Adicionar',
                                  image=imgbtn11,
                                  compound=TOP,
                                  relief='flat')
        self.__btnAddAdv['bg'] = 'LightSteelBlue3'
        self.__btnAddAdv['command'] = lambda: self.insert_adv()
        self.__btnAddAdv.image = imgbtn11
        self.__btnAddAdv.place(x=80, y=350, relwidth=0.15)

        self.__btnEditarAdv = Button(self.__frameAdvogados,
                                     text='Editar',
                                     image=imgbtn14,
                                     compound=TOP,
                                     relief='flat')
        self.__btnEditarAdv['bg'] = 'LightSteelBlue3'
        self.__btnEditarAdv['command'] = ''
        self.__btnEditarAdv.image = imgbtn14
        self.__btnEditarAdv.place(x=210, y=350, relwidth=0.15)

        self.__btnRmvAdv = Button(self.__frameAdvogados,
                                  text='Remover',
                                  image=imgbtn12,
                                  compound=TOP,
                                  relief='flat')
        self.__btnRmvAdv['bg'] = 'LightSteelBlue3'
        self.__btnRmvAdv['command'] = ''
        self.__btnRmvAdv.image = imgbtn12
        self.__btnRmvAdv.place(x=340, y=350, relwidth=0.15)

        self.__btnListarAdv = Button(self.__frameAdvogados,
                                     text='Listar Advogados',
                                     image=imgbtn13,
                                     compound=TOP,
                                     relief='flat')
        self.__btnListarAdv['bg'] = 'LightSteelBlue3'
        self.__btnListarAdv['command'] = ''
        self.__btnListarAdv.image = imgbtn13
        self.__btnListarAdv.place(x=470, y=350)

        self.__btnFechar = Button(self.__frameAdvogados,
                                  text='Fechar',
                                  image=imgbtn15,
                                  compound=TOP,
                                  relief='flat')
        self.__btnFechar['bg'] = 'LightSteelBlue3'
        self.__btnFechar['command'] = lambda: self.master.destroy()
        self.__btnFechar.image = imgbtn15

    @property
    def adv_nome(self):
        return self.__txtAdvNome.get()

    @property
    def adv_endereco(self):
        return self.__txtAdvEndereco.get()

    @property
    def adv_cidade(self):
        return self.__txtAdvCidadeUf.get()

    @property
    def adv_cep(self):
        return self.__txtAdvCep.get()

    @property
    def adv_fax(self):
        return self.__txtAdvFax.get()

    @property
    def adv_telefone(self):
        return self.__txtAdvTel.get()

    @property
    def adv_email(self):
        return self.__txtAdvEmail.get()

    @property
    def adv_oab(self):
        return self.__txtAdvOAB.get()

    @property
    def adv_cpf(self):
        return self.__txtAdvCPF.get()

    def insert_adv(self):
        insert('advogados', self.adv_nome, self.adv_endereco, self.adv_cidade, self.adv_cep,
               self.adv_telefone, self.adv_fax, self.adv_email, self.adv_oab, self.adv_cpf)
        if self.janela:
            self.master.destroy()
            messagebox.showinfo('Importante!', 'Operação Realizada com Sucesso.')
            self.app.iniciar_pagina()

    def iniciar_pagina(self):
        self.janela = False
        self.__frameAdvogados['padx'] = 80
        self.__frameAdvogados.pack(side=BOTTOM, fill=X, pady=1)

    def ocultar_pagina(self):
        self.__frameAdvogados.pack_forget()

    def iniciar_janela(self, app):
        self.janela = True
        self.app = app
        self.master.geometry('800x450+250+185')
        self.master.resizable(width=False, height=False)
        self.master['bg'] = 'LightSteelBlue3'
        self.__frameAdvogados.pack(side=BOTTOM, fill=X, pady=1)
        self.__btnFechar.place(x=620, y=350, relwidth=0.15)
