from random import randint

from utils.modulos import *


class Processos:
    # Cadastro de processos
    def __init__(self, master=None, app=None):
        img_escolher = PhotoImage(data=base64.b64decode(img_escolher_base64))  # imagem do botão Escolher Advogado
        img_salvar = PhotoImage(data=base64.b64decode(img_salvar_base64))  # imagem do botão Salvar Registro
        img_adicionar = PhotoImage(data=base64.b64decode(img_add_registro_base64))  # imagem do botão Add Registro
        img_cancelar = PhotoImage(data=base64.b64decode(img_cancelar_base64))  # imagem do botão Cancelar
        img_calendario = PhotoImage(data=base64.b64decode(img_calendario_base64))  # imagem do botão calendário

        self.app = app
        self.master = master
        self.__frameProcessos = Frame(self.master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')

        self.__lblCaso = Label(self.__frameProcessos, bg='LightSteelBlue3')
        self.__lblCaso['text'] = 'Caso N° '
        self.__lblCaso['font'] = 'Serif', '12', 'bold'
        self.__lblCaso.place(x=10, y=20)

        self.__txtCaso = Entry(self.__frameProcessos, width=5, justify='center', font='Serif 12 bold')
        self.__txtCaso.place(x=90, y=20)

        self.__lblAutor = Label(self.__frameProcessos, text='Autor', bg='LightSteelBlue3')
        self.__lblAutor['font'] = 'Serif', '12'
        self.__lblAutor.place(x=155, y=20)

        self.__txtAutor = Entry(self.__frameProcessos)
        self.__txtAutor.place(x=210, y=20, relwidth=0.674)

        self.__lblReu = Label(self.__frameProcessos, text='Réu', bg='LightSteelBlue3')
        self.__lblReu['font'] = 'Serif', '12'
        self.__lblReu.place(x=160, y=50)

        self.__txtReu = Entry(self.__frameProcessos)
        self.__txtReu.place(x=210, y=50, relwidth=0.674)

        self.__lblAdvExterno = Label(self.__frameProcessos, text='Adv Externo', bg='LightSteelBlue3')
        self.__lblAdvExterno['font'] = 'Serif', '12'
        self.__lblAdvExterno.place(x=100, y=80)

        self.__txtAdvExterno = ttk.Combobox(self.__frameProcessos, values=[])
        self.__txtAdvExterno['justify'] = 'left'
        self.__txtAdvExterno.place(x=210, y=80, relwidth=0.65)

        self.__btnAddAdv = Button(self.__frameProcessos,
                                  relief='flat',
                                  bg='LightSteelBlue3',
                                  highlightthickness=0)
        self.__btnAddAdv['command'] = lambda: self.command_advogados()
        self.__btnAddAdv['image'] = img_escolher
        self.__btnAddAdv.image = img_escolher
        self.__btnAddAdv.place(relx=0.87, rely=0.17)

        self.__lblAdvAdverso = Label(self.__frameProcessos, text='Adv Adverso', bg='LightSteelBlue3')
        self.__lblAdvAdverso['font'] = 'Serif', '12'
        self.__lblAdvAdverso.place(x=100, y=110)

        self.__txtAdvAdverso = Entry(self.__frameProcessos)
        self.__txtAdvAdverso.place(x=210, y=110, relwidth=0.674)

        self.__lblEndParteAdversa = Label(self.__frameProcessos, text='Endereço parte Adversa', bg='LightSteelBlue3')
        self.__lblEndParteAdversa['font'] = 'Serif', '12'
        self.__lblEndParteAdversa.place(x=10, y=140)

        self.__txtEndParteAdversa = Entry(self.__frameProcessos)
        self.__txtEndParteAdversa.place(x=210, y=140, relwidth=0.674)

        self.__lblTipoAcao = Label(self.__frameProcessos, text='Tipo Ação', bg='LightSteelBlue3')
        self.__lblTipoAcao['font'] = 'Serif', '12'
        self.__lblTipoAcao.place(x=120, y=170)

        self.__txtTipoAcao = ttk.Combobox(self.__frameProcessos, values=['CONHECIMENTO', 'CAUTELAR', 'EXECUÇÃO'])
        self.__txtTipoAcao['justify'] = 'center'
        self.__txtTipoAcao.place(x=210, y=170)

        self.__lblNumProcesso = Label(self.__frameProcessos, text='Processo', bg='LightSteelBlue3')
        self.__lblNumProcesso['font'] = 'Serif', '12'
        self.__lblNumProcesso.place(x=450, y=170)

        self.__txtNumProcesso = Entry(self.__frameProcessos)
        self.__txtNumProcesso.place(x=530, y=170, relwidth=0.34)

        self.__lblVaraTribunal = Label(self.__frameProcessos, text='Vara/Tribunal', bg='LightSteelBlue3')
        self.__lblVaraTribunal['font'] = 'Serif', '12'
        self.__lblVaraTribunal.place(x=90, y=200)

        self.__txtVaraTribunal = Entry(self.__frameProcessos, width=40)
        self.__txtVaraTribunal.place(x=210, y=200)

        self.__lblPosFeito = Label(self.__frameProcessos, text='Pos Feito', bg='LightSteelBlue3')
        self.__lblPosFeito['font'] = 'Serif', '12'
        self.__lblPosFeito.place(relx=0.625, y=200)

        self.__txtPosFeito = Entry(self.__frameProcessos)
        self.__txtPosFeito.place(relx=0.714, y=200, relwidth=0.18)

        self.__lblUfMunicipio = Label(self.__frameProcessos, text='UF - Município', bg='LightSteelBlue3')
        self.__lblUfMunicipio['font'] = 'Serif', '12'
        self.__lblUfMunicipio.place(x=80, y=230)

        self.__txtUfMunicipio = Entry(self.__frameProcessos, width=40)
        self.__txtUfMunicipio.place(x=210, y=230)

        self.__lblVrCausa = Label(self.__frameProcessos, text='Valor Causa R$', bg='LightSteelBlue3')
        self.__lblVrCausa['font'] = 'Serif', '12'
        self.__lblVrCausa.place(relx=0.57, y=230)

        self.__txtVrCausa = Entry(self.__frameProcessos)
        self.__txtVrCausa.place(relx=0.714, y=230, relwidth=0.18)

        self.__lblSitAtual = Label(self.__frameProcessos, text='Situação Atual', bg='LightSteelBlue3')
        self.__lblSitAtual['font'] = 'Serif', '12'
        self.__lblSitAtual.place(x=80, y=260)

        self.__txtSitAtual = ttk.Combobox(self.__frameProcessos, values=['FASE DE MOVIMENTAÇÃO', 'FASE DE DOCUMENTAÇÃO',
                                                                         'FASE DE COMUNICAÇÃO', 'FASE DE EXECUÇÃO'],
                                          width=25)
        self.__txtSitAtual['justify'] = 'center'
        self.__txtSitAtual.place(x=210, y=260)

        self.__lblVrAtual = Label(self.__frameProcessos, text='Valor Atual R$', bg='LightSteelBlue3')
        self.__lblVrAtual['font'] = 'Serif', '12'
        self.__lblVrAtual.place(relx=0.58, y=260)

        self.__txtVrAtual = Entry(self.__frameProcessos)
        self.__txtVrAtual.place(relx=0.714, y=260, relwidth=0.18)

        self.__lblDataInicio = Label(self.__frameProcessos, text='Inicio', bg='LightSteelBlue3')
        self.__lblDataInicio['font'] = 'Serif', '12'
        self.__lblDataInicio.place(x=150, y=290)

        self.__txtDataInicio = Entry(self.__frameProcessos)
        self.__txtDataInicio.place(x=210, y=290, relwidth=0.09)

        self.__lblDataFim = Label(self.__frameProcessos, text='Fim', bg='LightSteelBlue3')
        self.__lblDataFim['font'] = 'Serif', '12'
        self.__lblDataFim.place(x=385, y=290)

        self.__txtDataFim = Entry(self.__frameProcessos)
        self.__txtDataFim.place(x=430, y=290, relwidth=0.09)

        self.__lblPerda = Label(self.__frameProcessos, text='Perda', bg='LightSteelBlue3')
        self.__lblPerda['font'] = 'Serif', '12'
        self.__lblPerda.place(relx=0.65, y=290)

        self.__txtPerda = Entry(self.__frameProcessos)
        self.__txtPerda.place(relx=0.714, y=290, relwidth=0.18)

        self.__lblPedido = Label(self.__frameProcessos, text='Pedido', bg='LightSteelBlue3')
        self.__lblPedido['font'] = 'Serif', '12'
        self.__lblPedido.place(x=145, y=320)

        self.__txtPedido = Text(self.__frameProcessos, width=30, height=3)
        self.__txtPedido.place(x=210, y=320)

        self.__lblObs = Label(self.__frameProcessos, text='Observações', bg='LightSteelBlue3')
        self.__lblObs['font'] = 'Serif', '12'
        self.__lblObs.place(relx=0.575, y=320)

        self.__txtObs = Text(self.__frameProcessos, height=3)
        self.__txtObs.place(relx=0.694, y=320, relwidth=0.2)

        self.__btnAddRegistro = Button(self.__frameProcessos,
                                       text='Adicionar Registro',
                                       compound=TOP,
                                       relief='flat',
                                       bg='LightSteelBlue3')
        self.__btnAddRegistro['image'] = img_adicionar
        self.__btnAddRegistro.image = img_adicionar
        self.__btnAddRegistro['command'] = lambda: self.insert_processo()
        self.__btnAddRegistro.place(x=400, y=390)

        self.__btnSalvarRegistro = Button(self.__frameProcessos,
                                          text='Salvar Registro',
                                          compound=TOP,
                                          relief='flat',
                                          bg='LightSteelBlue3')
        self.__btnSalvarRegistro['image'] = img_salvar
        self.__btnSalvarRegistro.image = img_salvar
        self.__btnSalvarRegistro['command'] = lambda: self.update_processo()

        self.__btnCancelar = Button(self.__frameProcessos,
                                    image=img_cancelar,
                                    text='Cancelar',
                                    compound=TOP,
                                    relief='flat',
                                    bg='LightSteelBlue3')
        self.__btnCancelar.image = img_cancelar
        self.__btnCancelar['command'] = lambda: self.iniciar_pagina()

        self.__btnCalendario = Button(self.__frameProcessos,
                                      image=img_calendario,
                                      relief='flat',
                                      bg='LightSteelBlue3',
                                      highlightthickness=0
                                      )
        self.__btnCalendario.image = img_calendario
        self.__btnCalendario['command'] = lambda: Calendario(self.__frameProcessos,
                                                             self.__txtDataInicio,
                                                             relx=self.__txtDataInicio.winfo_rootx(),
                                                             rely=self.__txtDataInicio.winfo_rooty())
        self.__btnCalendario.place(relx=0.31, rely=0.62)

        self.__btnCalendario = Button(self.__frameProcessos,
                                      image=img_calendario,
                                      relief='flat',
                                      bg='LightSteelBlue3',
                                      highlightthickness=0
                                      )
        self.__btnCalendario.image = img_calendario
        self.__btnCalendario['command'] = lambda: Calendario(self.__frameProcessos,
                                                             self.__txtDataFim,
                                                             relx=self.__txtDataFim.winfo_rootx(),
                                                             rely=self.__txtDataFim.winfo_rooty())
        self.__btnCalendario.place(relx=0.541, rely=0.62)

    @property
    def caso(self):

        return self.__txtCaso.get()

    @caso.setter
    def caso(self, valor):
        self.__txtCaso.insert(0, valor)

    @property
    def autor(self):
        return self.__txtAutor.get()

    @autor.setter
    def autor(self, valor):
        self.__txtAutor.insert(0, valor)

    @property
    def reu(self):
        return self.__txtReu.get()

    @reu.setter
    def reu(self, valor):
        self.__txtReu.insert(0, valor)

    @property
    def adv_externo(self):
        return self.__txtAdvExterno.get()

    @adv_externo.setter
    def adv_externo(self, valor):
        self.__txtAdvExterno.insert(0, valor)

    @property
    def adv_adverso(self):
        return self.__txtAdvAdverso.get()

    @adv_adverso.setter
    def adv_adverso(self, valor):
        self.__txtAdvAdverso.insert(0, valor)

    @property
    def end_parte_adv(self):
        return self.__txtEndParteAdversa.get()

    @end_parte_adv.setter
    def end_parte_adv(self, valor):
        self.__txtEndParteAdversa.insert(0, valor)

    @property
    def tipo_acao(self):
        return self.__txtTipoAcao.get()

    @tipo_acao.setter
    def tipo_acao(self, valor):
        self.__txtTipoAcao.insert(0, valor)

    @property
    def processo(self):
        return self.__txtNumProcesso.get()

    @processo.setter
    def processo(self, valor):
        self.__txtNumProcesso.insert(0, valor)

    @property
    def vara_tribunal(self):
        return self.__txtVaraTribunal.get()

    @vara_tribunal.setter
    def vara_tribunal(self, valor):
        self.__txtVaraTribunal.insert(0, valor)

    @property
    def pos_feito(self):
        return self.__txtPosFeito.get()

    @pos_feito.setter
    def pos_feito(self, valor):
        self.__txtPosFeito.insert(0, valor)

    @property
    def uf_municipio(self):
        return self.__txtUfMunicipio.get()

    @uf_municipio.setter
    def uf_municipio(self, valor):
        self.__txtUfMunicipio.insert(0, valor)

    @property
    def vr_causa(self):
        return self.__txtVrCausa.get()

    @vr_causa.setter
    def vr_causa(self, valor):
        self.__txtVrCausa.insert(0, valor)

    @property
    def situacao(self):
        return self.__txtSitAtual.get()

    @situacao.setter
    def situacao(self, valor):
        self.__txtSitAtual.insert(0, valor)

    @property
    def vr_atual(self):
        return self.__txtVrAtual.get()

    @vr_atual.setter
    def vr_atual(self, valor):
        self.__txtVrAtual.insert(0, valor)

    @property
    def inicio(self):
        return self.__txtDataInicio.get()

    @inicio.setter
    def inicio(self, valor):
        self.__txtDataInicio.insert(0, valor)

    @property
    def fim(self):
        return self.__txtDataFim.get()

    @fim.setter
    def fim(self, valor):
        self.__txtDataFim.insert(0, valor)

    @property
    def perda(self):
        return self.__txtPerda.get()

    @perda.setter
    def perda(self, valor):
        self.__txtPerda.insert(0, valor)

    @property
    def pedido(self):
        return self.__txtPedido.get(1.0, END)

    @pedido.setter
    def pedido(self, valor):
        self.__txtPedido.insert(1.0, valor)

    @property
    def observacao(self):
        return self.__txtObs.get(1.0, END)

    @observacao.setter
    def observacao(self, valor):
        self.__txtObs.insert(1.0, valor)

    @property
    def advogados(self):
        return self.__txtAdvExterno.get()

    @advogados.setter
    def advogados(self, valor):
        self.__txtAdvExterno['values'] = valor

    def insert_processo(self):
        try:
            self.validar()
        except ValueError:
            messagebox.showwarning('Atenção', 'Verifique os campos marcados em vermelho e tente novamente.')
        else:
            try:
                insert('processos', self.caso, self.autor, self.reu, self.adv_externo, self.adv_adverso,
                       self.processo, self.inicio, self.vr_causa, self.tipo_acao, self.vara_tribunal, self.uf_municipio,
                       self.situacao, self.pos_feito, self.observacao, self.vr_atual, self.pedido, self.fim, self.perda,
                       self.end_parte_adv)
                messagebox.showinfo('Informação', 'Processo adicionado com sucesso.')
                self.iniciar_pagina()
            except IntegrityError:
                messagebox.showwarning('Atenção', 'Já existe um caso com este número.')
            except OperationalError:
                messagebox.showerror('Atenção', 'Ocorreu um erro...')

    def update_processo(self):
        try:
            self.validar()
        except ValueError:
            messagebox.showwarning('Atenção', 'Verifique os campos marcados em vermelho e tente novamente.')
        else:
            caso = self.caso
            rid = search('processos', parms='id', clause=f'where caso={caso}')[0][0]
            update(rid, 'processos',
                   autor=self.autor,
                   reu=self.reu,
                   adv_externo=self.adv_externo,
                   adv_adverso=self.adv_adverso,
                   processo=self.processo,
                   inicio=self.inicio,
                   vr_causa=self.vr_causa,
                   tipo_acao=self.tipo_acao,
                   vara_tribunal=self.vara_tribunal,
                   uf_municipio=self.uf_municipio,
                   situacao=self.situacao,
                   pos_feito=self.pos_feito,
                   observacao=self.observacao,
                   valor_atual=self.vr_atual,
                   pedido=self.pedido,
                   fim=self.fim,
                   perda=self.perda,
                   end_parte_adv=self.end_parte_adv
                   )
            messagebox.showinfo('Informação', 'Registro alterado com Sucesso!')
            self.iniciar_pagina()

    def preencher(self, values=None):
        self.__txtCaso['state'] = 'normal'
        limpar(self.__frameProcessos)

        if values:
            self.caso = values[1]
            self.autor = values[2]
            self.reu = values[3]
            self.__txtAdvExterno.set(values[4])
            self.adv_adverso = values[5]
            self.processo = values[6]
            self.inicio = values[7]
            self.vr_causa = values[8]
            self.tipo_acao = values[9]
            self.vara_tribunal = values[10]
            self.uf_municipio = values[11]
            self.situacao = values[12]
            self.pos_feito = values[13]
            self.observacao = values[14]
            self.vr_atual = values[15]
            self.pedido = values[16]
            self.fim = values[17]
            self.perda = values[18]
            self.end_parte_adv = values[19]
        self.__txtCaso['state'] = 'readonly'

    def iniciar_pagina(self, novo=True):
        self.ocultar_pagina()
        self.__txtCaso['state'] = 'normal'
        limpar(self.__frameProcessos)
        self.atualizar_advogados()
        self.__frameProcessos.pack(side=BOTTOM, fill=X, pady=1)
        self.__btnSalvarRegistro.place_forget()
        self.__btnCancelar.place_forget()
        self.__btnAddRegistro.place(x=400, y=390)
        if novo:
            self.novo_caso()
        self.__txtCaso['state'] = 'readonly'

    def atualizar_advogados(self):
        advogados = [advogado for advogado in search('advogados', parms='nome')]
        advogados = [advogado[0] for advogado in advogados]
        self.advogados = advogados

    def novo_caso(self):
        casos = search('processos', parms='caso')
        casos = [caso[0] for caso in casos]
        novo_caso = None
        while novo_caso is None:
            num = randint(1, 9999)
            if num not in casos:
                novo_caso = num
        self.caso = novo_caso

    def ocultar_pagina(self):
        self.__frameProcessos.pack_forget()

    def command_advogados(self):
        from models.add_advogado import AddAdvogado
        add_advogado = AddAdvogado(self.master, self, True)
        add_advogado.iniciar_janela(self)

    def trocar_botoes(self):
        if not self.__btnSalvarRegistro.place_info():
            self.__btnAddRegistro.place_forget()
            self.__btnSalvarRegistro.place(x=350, y=390)
            self.__btnCancelar.place(x=500, y=390, relwidth=0.13)

    def validar(self):
        valid = []

        for child in self.__frameProcessos.winfo_children():
            child_class = child.__class__.__name__

            if child_class == 'Entry':
                if validar_vazio(child.get()) and validar_space(child.get()):
                    child['background'] = '#fff'
                    valid.append(True)
                else:
                    child['background'] = 'Indian Red'
                    valid.append(False)
            elif child_class == 'Combobox':
                if validar_vazio(child.get()) and validar_space(child.get()):
                    style = ttk.Style()
                    style.configure("w.TCombobox", fieldbackground='#fff')
                    child['style'] = 'w.TCombobox'
                    valid.append(True)
                else:
                    style = ttk.Style()
                    style.configure("r.TCombobox", selectbackground='Indian Red')
                    child['style'] = 'r.TCombobox'
                    valid.append(False)

            elif child_class == 'Text':
                if validar_vazio(child.get(1.0, END)) and validar_space(child.get(1.0, END)):
                    child['background'] = '#fff'
                    valid.append(True)
                else:
                    child['background'] = 'Indian Red'
                    valid.append(False)

        if (validar_str(self.autor)) and (validar_str(self.reu)) and (validar_str(self.adv_externo)) and \
                (validar_str(self.adv_adverso)) and (validar_processo(self.processo)) and \
                (validar_float(self.vr_causa)) and (validar_float(self.vr_atual)) and \
                (validar_data(self.inicio)) and (validar_data(self.fim)):
            valid.append(True)
        else:
            if not validar_str(self.autor):
                self.__txtAutor['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtAutor['background'] = '#fff'
                valid.append(True)
            if not validar_str(self.reu):
                self.__txtReu['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtReu['background'] = '#fff'
                valid.append(True)
            if not validar_str(self.adv_externo):
                style = ttk.Style()
                style.theme_use('alt')
                style.configure("r.TCombobox", fieldbackground='Indian Red')
                self.__txtAdvExterno['style'] = 'r.TCombobox'
                valid.append(False)
            else:
                style = ttk.Style()
                style.theme_use('alt')
                style.configure("w.TCombobox", fieldbackground='#fff')
                self.__txtAdvExterno['style'] = 'w.TCombobox'
                valid.append(True)
            if not validar_str(self.adv_adverso):
                self.__txtAdvAdverso['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtAdvAdverso['background'] = '#fff'
                valid.append(True)
            if not validar_processo(self.processo):
                self.__txtNumProcesso['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtNumProcesso['background'] = '#fff'
                valid.append(True)

            if not validar_float(self.vr_causa):
                self.__txtVrCausa['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtVrCausa['background'] = '#fff'
                valid.append(True)

            if not validar_float(self.vr_atual):
                self.__txtVrAtual['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtVrAtual['background'] = '#fff'
                valid.append(True)

            if not validar_data(self.inicio):
                self.__txtDataInicio['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtDataInicio['background'] = '#fff'
                valid.append(True)
            if not validar_data(self.fim):
                self.__txtDataFim['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtDataFim['background'] = '#fff'
                valid.append(True)

        if False not in valid:
            return True
        else:
            raise ValueError
