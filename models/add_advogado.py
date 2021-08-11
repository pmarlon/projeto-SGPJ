from utils.modulos import *


class AddAdvogado:
    def __init__(self, master=None, app=None, janela=None):

        img_salvar = PhotoImage(data=base64.b64decode(img_salvar_base64))  # imagem do botão Salvar Registro
        img_adicionar = PhotoImage(data=base64.b64decode(img_add_adv_base64))  # imagem do botão Add Advogado
        img_remover = PhotoImage(data=base64.b64decode(img_remover_adv_base64))  # imagem do botão Remover
        img_listar = PhotoImage(data=base64.b64decode(img_listar_adv_base64))  # imagem do botão Listar
        img_editar = PhotoImage(data=base64.b64decode(img_editar_adv_base64))  # imagem do botão Editar
        img_fechar = PhotoImage(data=base64.b64decode(img_fechar_base64))  # imagem do botão Fechar
        img_cancelar = PhotoImage(data=base64.b64decode(img_cancelar_base64))  # imagem do botão Cancelar

        self.app = app
        if janela:
            self.master = Toplevel(master)
        else:
            self.master = master

        self.__frameAdvogados = Frame(self.master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')

        self.__lblAdvNome = Label(self.__frameAdvogados, text='Nome', bg='LightSteelBlue3')
        self.__lblAdvNome['font'] = 'Serif', '12'
        self.__lblAdvNome.place(x=35, y=20)

        self.__txtAdvNome = Entry(self.__frameAdvogados)
        vcmd = self.__txtAdvNome.register(func=self.valida_auto_complete)
        self.__txtAdvNome['validate'] = 'key'
        self.__txtAdvNome['validatecommand'] = (vcmd, '%P', 'nome')
        self.__txtAdvNome.place(x=100, y=20, relwidth=0.85)

        self.__lblAdvEndereco = Label(self.__frameAdvogados, text='Endereço', bg='LightSteelBlue3')
        self.__lblAdvEndereco['font'] = 'Serif', '12'
        self.__lblAdvEndereco.place(x=10, y=50)

        self.__txtAdvEndereco = Entry(self.__frameAdvogados)
        self.__txtAdvEndereco.place(x=100, y=50, relwidth=0.85)

        self.__lblAdvCidadeUf = Label(self.__frameAdvogados, text='Cidade/UF', bg='LightSteelBlue3')
        self.__lblAdvCidadeUf['font'] = 'Serif', '12'
        self.__lblAdvCidadeUf.place(x=10, y=80)

        self.__txtAdvCidadeUf = Entry(self.__frameAdvogados)
        self.__txtAdvCidadeUf.place(x=100, y=80, relwidth=0.45)

        self.__lblAdvCep = Label(self.__frameAdvogados, text='CEP', bg='LightSteelBlue3')
        self.__lblAdvCep['font'] = 'Serif', '12'
        self.__lblAdvCep.place(relx=0.62, y=80)

        self.__txtAdvCep = Entry(self.__frameAdvogados)
        self.__txtAdvCep.place(relx=0.675, y=80, relwidth=0.3)

        self.__lblAdvFax = Label(self.__frameAdvogados, text='FAX', bg='LightSteelBlue3')
        self.__lblAdvFax['font'] = 'Serif', '12'
        self.__lblAdvFax.place(x=50, y=110)

        self.__txtAdvFax = Entry(self.__frameAdvogados)
        self.__txtAdvFax.place(x=100, y=110, relwidth=0.3)

        self.__lblAdvTel = Label(self.__frameAdvogados, text='Tel. Comercial', bg='LightSteelBlue3')
        self.__lblAdvTel['font'] = 'Serif', '12'
        self.__lblAdvTel.place(relx=0.51, y=110)

        self.__txtAdvTel = Entry(self.__frameAdvogados)
        self.__txtAdvTel.place(relx=0.675, y=110, relwidth=0.3)

        self.__lblAdvEmail = Label(self.__frameAdvogados, text='Email', bg='LightSteelBlue3')
        self.__lblAdvEmail['font'] = 'Serif', '12'
        self.__lblAdvEmail.place(x=30, y=140)

        self.__txtAdvEmail = Entry(self.__frameAdvogados)
        self.__txtAdvEmail.place(x=100, y=140, relwidth=0.85)

        self.__lblAdvOAB = Label(self.__frameAdvogados, text='N° OAB', bg='LightSteelBlue3')
        self.__lblAdvOAB['font'] = 'Serif', '12'
        self.__lblAdvOAB.place(x=30, y=170)

        self.__txtAdvOAB = Entry(self.__frameAdvogados)
        vcmd = self.__txtAdvOAB.register(func=self.valida_auto_complete)
        self.__txtAdvOAB['validate'] = 'key'
        self.__txtAdvOAB['validatecommand'] = (vcmd, '%P', 'oab')
        self.__txtAdvOAB.place(x=100, y=170, relwidth=0.3)

        self.__lblAdvCPF = Label(self.__frameAdvogados, text='CPF', bg='LightSteelBlue3')
        self.__lblAdvCPF['font'] = 'Serif', '12'
        self.__lblAdvCPF.place(relx=0.62, y=170)

        self.__txtAdvCPF = Entry(self.__frameAdvogados)
        vcmd = self.__txtAdvCPF.register(func=self.valida_auto_complete)
        self.__txtAdvCPF['validate'] = 'key'
        self.__txtAdvCPF['validatecommand'] = (vcmd, '%P', 'cpf')
        self.__txtAdvCPF.place(relx=0.675, y=170, relwidth=0.3)

        self.__colunas = ('#1', '#2', '#3', '#4', '#5')
        self.__tvAdvogados = ttk.Treeview(self.__frameAdvogados, columns=self.__colunas, selectmode='browse',
                                          height=5)

        self.__tvAdvogados.heading('#0', text='')
        self.__tvAdvogados.heading('#1', text='Nome')
        self.__tvAdvogados.heading('#2', text='Endereço')
        self.__tvAdvogados.heading('#3', text='CPF')
        self.__tvAdvogados.heading('#4', text='OAB')
        self.__tvAdvogados.heading('#5', text='Telefone/FAX')

        self.__tvAdvogados.column('#0', width=0, stretch=NO)
        self.__tvAdvogados.column('#1', width=200, anchor='n')
        self.__tvAdvogados.column('#2', width=150, anchor='center')
        self.__tvAdvogados.column('#3', width=150, anchor='center')
        self.__tvAdvogados.column('#4', width=100, anchor='center')
        self.__tvAdvogados.column('#5', width=150, anchor='center')

        self.__tvAdvogados.place(x=20, y=220)

        self.__btnSalvar = Button(self.__frameAdvogados,
                                  text='Salvar',
                                  image=img_salvar,
                                  compound=TOP,
                                  relief='flat')
        self.__btnSalvar['bg'] = 'LightSteelBlue3'
        self.__btnSalvar['command'] = lambda: self.update_adv()
        self.__btnSalvar.image = img_salvar

        self.__btnAddAdv = Button(self.__frameAdvogados,
                                  text='Adicionar',
                                  image=img_adicionar,
                                  compound=TOP,
                                  relief='flat')
        self.__btnAddAdv['bg'] = 'LightSteelBlue3'
        self.__btnAddAdv['command'] = lambda: self.insert_adv()
        self.__btnAddAdv.image = img_adicionar
        self.__btnAddAdv.place(x=80, y=350, relwidth=0.15)

        self.__btnEditarAdv = Button(self.__frameAdvogados,
                                     text='Editar',
                                     image=img_editar,
                                     compound=TOP,
                                     relief='flat')
        self.__btnEditarAdv['bg'] = 'LightSteelBlue3'
        self.__btnEditarAdv['command'] = lambda: self.editar()
        self.__btnEditarAdv.image = img_editar

        self.__btnRmvAdv = Button(self.__frameAdvogados,
                                  text='Remover',
                                  image=img_remover,
                                  compound=TOP,
                                  relief='flat')
        self.__btnRmvAdv['bg'] = 'LightSteelBlue3'
        self.__btnRmvAdv['command'] = lambda: self.deletar()
        self.__btnRmvAdv.image = img_remover
        self.__btnRmvAdv.place(x=340, y=350, relwidth=0.15)

        self.__btnListarAdv = Button(self.__frameAdvogados,
                                     text='Listar Advogados',
                                     image=img_listar,
                                     compound=TOP,
                                     relief='flat')
        self.__btnListarAdv['bg'] = 'LightSteelBlue3'
        self.__btnListarAdv['command'] = lambda: self.listar()
        self.__btnListarAdv.image = img_listar
        self.__btnListarAdv.place(x=470, y=350)

        self.__btnFechar = Button(self.__frameAdvogados,
                                  text='Fechar',
                                  image=img_fechar,
                                  compound=TOP,
                                  relief='flat')
        self.__btnFechar['bg'] = 'LightSteelBlue3'
        self.__btnFechar['command'] = lambda: self.master.destroy()
        self.__btnFechar.image = img_fechar

        self.__btnCancelar = Button(self.__frameAdvogados,
                                    image=img_cancelar,
                                    text='Cancelar',
                                    compound=TOP,
                                    relief='flat',
                                    bg='LightSteelBlue3')
        self.__btnCancelar.image = img_cancelar
        self.__btnCancelar['command'] = lambda: self.command_cancelar()

    @property
    def adv_nome(self):
        return self.__txtAdvNome.get().upper()

    @property
    def adv_endereco(self):
        return self.__txtAdvEndereco.get().upper()

    @property
    def adv_cidade(self):
        return self.__txtAdvCidadeUf.get().upper()

    @property
    def adv_cep(self):
        return self.__txtAdvCep.get().upper()

    @property
    def adv_fax(self):
        return self.__txtAdvFax.get()

    @property
    def adv_telefone(self):
        return self.__txtAdvTel.get()

    @property
    def adv_email(self):
        return self.__txtAdvEmail.get().upper()

    @property
    def adv_oab(self):
        return self.__txtAdvOAB.get()

    @property
    def adv_cpf(self):
        return self.__txtAdvCPF.get()

    def insert_adv(self):
        try:
            self.validar()
        except ValueError:
            messagebox.showwarning('Atenção', 'Verifique os campos marcados em vermelho e tente novamente.',
                                   parent=self.master)
        else:
            try:

                insert('advogados', self.adv_nome, self.adv_endereco, self.adv_cidade, self.adv_cep,
                       self.adv_telefone, self.adv_fax, self.adv_email, self.adv_oab, self.adv_cpf)
                messagebox.showinfo('Informação', 'Advogado cadastrado com sucesso.', parent=self.master)
                if str(self.master.winfo_class()) == 'Toplevel':
                    self.app.atualizar_advogados()
                    self.master.destroy()
                else:
                    self.iniciar_pagina()

            except IntegrityError:
                messagebox.showwarning('Atenção', 'Já existe um cadastro com o CPF ou N° OAB digitados.',
                                       parent=self.master)

    def listar(self):
        self.__tvAdvogados.delete(*self.__tvAdvogados.get_children())
        advogados = view('advogados')
        for advogado in advogados:
            self.__tvAdvogados.insert('', END, iid=None,
                                      values=(advogado[1], advogado[2], advogado[9],
                                              advogado[8], f'{advogado[6]} / {advogado[5]}'))

    def deletar(self):

        try:
            rid = get_id(self.__tvAdvogados, 'advogados')

        except IndexError:
            messagebox.showerror('Atenção', 'Você precisa selecionar um registro.', parent=self.master)
        except TypeError:
            messagebox.showerror('Erro', 'Algo deu errado...', parent=self.master)
        except OperationalError:
            messagebox.showerror('Erro', 'Algo deu errado...', parent=self.master)
        else:
            if messagebox.askyesno('Atenção', 'Deseja mesmo excluir o registro?', parent=self.master):
                delete(rid, 'advogados')
                messagebox.showinfo('Informação', 'Registro excluído com sucesso.', parent=self.master)
                self.listar()

    def editar(self):
        try:
            self.preencher()
        except ValueError:
            messagebox.showerror('Atenção', 'Ocorreu um erro...', parent=self.master)
        except IndexError:
            messagebox.showerror('Atenção', 'Você precisa selecionar um registro.', parent=self.master)
        else:
            self.__btnEditarAdv.place_forget()
            self.__btnRmvAdv.place_forget()
            self.__btnAddAdv.place_forget()
            self.__btnListarAdv.place_forget()
            self.__txtAdvCPF['state'] = 'readonly'
            self.__txtAdvOAB['state'] = 'readonly'
            self.__btnSalvar.place(x=210, y=350, relwidth=0.15)
            self.__btnCancelar.place(x=340, y=350, relwidth=0.15)
            if str(self.master.winfo_class()) == 'Toplevel':
                self.__btnFechar.place(x=470, y=350, relwidth=0.15)

    def update_adv(self):
        try:
            self.validar()
        except ValueError:
            messagebox.showwarning('Atenção', 'Verifique os campos marcados em vermelho e tente novamente.',
                                   parent=self.master)
        else:
            cpf = self.__txtAdvCPF.get()
            rid = search('advogados', parms='id', clause=f'where cpf={cpf}')[0][0]

            update(rid, 'advogados',
                   nome=self.adv_nome,
                   endereco=self.adv_endereco,
                   cidade_uf=self.adv_cidade,
                   cep=self.adv_cep,
                   fone_com=self.adv_telefone,
                   fax=self.adv_fax,
                   email=self.adv_email)

            messagebox.showinfo('Informação', 'Registro alterado com Sucesso!', parent=self.master)

            self.__txtAdvCPF['state'] = 'normal'
            self.__txtAdvOAB['state'] = 'normal'
            limpar(self.__frameAdvogados, self.__tvAdvogados)
            self.listar()
            self.command_cancelar()

    def preencher(self):
        try:

            rid = get_id(self.__tvAdvogados, 'advogados')
            values = search('advogados', clause=f'where id={rid}')[0]
        except OperationalError:
            raise ValueError
        else:
            limpar(self.__frameAdvogados, self.__tvAdvogados)
            self.listar()
            cont = 0

            for child in self.__frameAdvogados.winfo_children():
                # Captura o nome da classe de cada elemento
                widget_class = child.__class__.__name__
                # Se a classe for Entry preenche o campo com valor
                if widget_class == 'Entry':
                    cont += 1
                    child.insert(END, values[cont])

    def valida_auto_complete(self, entrada, campo):
        self.__tvAdvogados.delete(*self.__tvAdvogados.get_children())
        if entrada:
            auto_complete(entrada, 'advogados', campo, self.__tvAdvogados)
            return True

        elif entrada == '':
            return True
        else:
            return False

    def iniciar_pagina(self):

        self.__txtAdvCPF['state'] = 'normal'
        self.__txtAdvOAB['state'] = 'normal'
        limpar(self.__frameAdvogados, self.__tvAdvogados)
        self.__frameAdvogados['padx'] = 80
        self.__btnSalvar.place_forget()
        self.__btnEditarAdv.place(x=210, y=350, relwidth=0.15)
        self.__frameAdvogados.pack(side=BOTTOM, fill=X, pady=1)

    def ocultar_pagina(self):
        self.__frameAdvogados.pack_forget()

    def iniciar_janela(self, app):
        self.app = app
        self.master.geometry('800x450+250+185')
        self.master.resizable(width=False, height=False)
        self.master['bg'] = 'LightSteelBlue3'
        self.__txtAdvCPF['state'] = 'normal'
        self.__txtAdvOAB['state'] = 'normal'
        limpar(self.__frameAdvogados, self.__tvAdvogados)

        self.__btnSalvar.place_forget()
        self.__btnEditarAdv.place(x=210, y=350, relwidth=0.15)
        self.__frameAdvogados.pack(side=BOTTOM, fill=X, pady=1)
        self.__btnFechar.place(x=620, y=350, relwidth=0.15)

    def command_cancelar(self):
        self.__txtAdvCPF['state'] = 'normal'
        self.__txtAdvOAB['state'] = 'normal'
        limpar(self.__frameAdvogados, self.__tvAdvogados)
        self.__btnSalvar.place_forget()
        self.__btnCancelar.place_forget()
        self.__btnAddAdv.place(x=80, y=350, relwidth=0.15)
        self.__btnEditarAdv.place(x=210, y=350, relwidth=0.15)
        self.__btnRmvAdv.place(x=340, y=350, relwidth=0.15)
        self.__btnListarAdv.place(x=470, y=350)

        if str(self.master.winfo_class()) == 'Toplevel':
            self.__btnFechar.place_forget()
            self.__btnFechar.place(x=620, y=350, relwidth=0.15)

    def validar(self):
        valid = []

        for child in self.__frameAdvogados.winfo_children():
            child_class = child.__class__.__name__

            if child_class == 'Entry':
                if validar_vazio(child.get()) and validar_space(child.get()):
                    child['background'] = '#fff'
                    valid.append(True)
                else:
                    child['background'] = 'Indian Red'
                    valid.append(False)

        if validar_str(self.adv_nome) and validar_int(self.adv_cpf) and validar_int(self.adv_oab) \
                and validar_int(self.adv_cep):
            valid.append(True)
        else:
            if not validar_str(self.adv_nome):
                self.__txtAdvNome['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtAdvNome['background'] = '#fff'
                valid.append(True)
            if not validar_int(self.adv_cpf) or len(self.adv_cpf) != 11:
                self.__txtAdvCPF['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtAdvCPF['background'] = '#fff'
                valid.append(True)
            if not validar_int(self.adv_oab):
                self.__txtAdvOAB['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtAdvOAB['background'] = '#fff'
                valid.append(True)

            if not validar_int(self.adv_cep):
                self.__txtAdvCep['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtAdvCep['background'] = '#fff'
                valid.append(True)

        if False not in valid:
            return True
        else:
            raise ValueError
