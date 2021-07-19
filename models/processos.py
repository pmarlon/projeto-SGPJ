from utils.modulos import *


class Processos:
    # Cadastro de processos
    def __init__(self, master=None, app=None):
        imgbtn1 = PhotoImage(file='imagens/imgObservar.png')  # imagem do botão Ocorrências
        imgbtn3 = PhotoImage(file='imagens/imgEscolherAdv.png')  # imagem do botão Escolher Advogado
        imgbtn4 = PhotoImage(file='imagens/imgSalvar.png')  # imagem do botão Salvar Registro
        imgbtn5 = PhotoImage(file='imagens/imgCalendario.png')  # imagem do botão Calendario

        self.app = app
        self.master = master
        self.__frameProcessos = Frame(self.master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')
        self.num_caso = StringVar()

        self.__lblCaso = Label(self.__frameProcessos, bg='LightSteelBlue3', relief='groove')
        self.__lblCaso['textvariable'] = self.num_caso
        self.__lblCaso['font'] = 'Serif', '12', 'bold'
        self.__lblCaso.place(x=10, y=20)

        self.__lblAutor = Label(self.__frameProcessos, text='Autor', bg='LightSteelBlue3')
        self.__lblAutor['font'] = 'Serif', '12'
        self.__lblAutor.place(x=150, y=20)

        self.__txtAutor = Entry(self.__frameProcessos, width=80)
        self.__txtAutor.place(x=210, y=20)

        self.__lblReu = Label(self.__frameProcessos, text='Réu', bg='LightSteelBlue3')
        self.__lblReu['font'] = 'Serif', '12'
        self.__lblReu.place(x=160, y=50)

        self.__txtReu = Entry(self.__frameProcessos, width=80)
        self.__txtReu.place(x=210, y=50)

        self.__lblAdvExterno = Label(self.__frameProcessos, text='Adv Externo', bg='LightSteelBlue3')
        self.__lblAdvExterno['font'] = 'Serif', '12'
        self.__lblAdvExterno.place(x=100, y=80)

        self.__txtAdvExterno = ttk.Combobox(self.__frameProcessos, values=[],
                                            width=74)
        self.__txtAdvExterno['justify'] = 'left'
        self.__txtAdvExterno.place(x=210, y=80)

        self.__btnAddAdv = Button(self.__frameProcessos,
                                  relief='flat',
                                  bg='LightSteelBlue3',
                                  highlightthickness=0)
        self.__btnAddAdv['command'] = lambda: self.command_advogados()
        self.__btnAddAdv['image'] = imgbtn3
        self.__btnAddAdv.image = imgbtn3
        self.__btnAddAdv.place(x=825, y=80)

        self.__lblAdvAdverso = Label(self.__frameProcessos, text='Adv Adverso', bg='LightSteelBlue3')
        self.__lblAdvAdverso['font'] = 'Serif', '12'
        self.__lblAdvAdverso.place(x=100, y=110)

        self.__txtAdvAdverso = Entry(self.__frameProcessos, width=80)
        self.__txtAdvAdverso.place(x=210, y=110)

        self.__lblEndParteAdversa = Label(self.__frameProcessos, text='Endereço parte Adversa', bg='LightSteelBlue3')
        self.__lblEndParteAdversa['font'] = 'Serif', '12'
        self.__lblEndParteAdversa.place(x=10, y=140)

        self.__txtEndParteAdversa = Entry(self.__frameProcessos, width=80)
        self.__txtEndParteAdversa.place(x=210, y=140)

        self.__lblTipoAcao = Label(self.__frameProcessos, text='Tipo Ação', bg='LightSteelBlue3')
        self.__lblTipoAcao['font'] = 'Serif', '12'
        self.__lblTipoAcao.place(x=120, y=170)

        self.__txtTipoAcao = ttk.Combobox(self.__frameProcessos, values=['CONHECIMENTO', 'CAUTELAR', 'EXECUÇÃO'])
        self.__txtTipoAcao['justify'] = 'center'
        self.__txtTipoAcao.place(x=210, y=170)

        self.__lblNumProcesso = Label(self.__frameProcessos, text='Processo', bg='LightSteelBlue3')
        self.__lblNumProcesso['font'] = 'Serif', '12'
        self.__lblNumProcesso.place(x=450, y=170)

        self.__txtNumProcesso = Entry(self.__frameProcessos, width=40)
        self.__txtNumProcesso.place(x=530, y=170)

        self.__lblVaraTribunal = Label(self.__frameProcessos, text='Vara/Tribunal', bg='LightSteelBlue3')
        self.__lblVaraTribunal['font'] = 'Serif', '12'
        self.__lblVaraTribunal.place(x=90, y=200)

        self.__txtVaraTribunal = Entry(self.__frameProcessos, width=45)
        self.__txtVaraTribunal.place(x=210, y=200)

        self.__lblPosFeito = Label(self.__frameProcessos, text='Pos Feito', bg='LightSteelBlue3')
        self.__lblPosFeito['font'] = 'Serif', '12'
        self.__lblPosFeito.place(x=590, y=200)

        self.__txtPosFeito = ttk.Combobox(self.__frameProcessos, values=['AUTOR'])
        self.__txtPosFeito['justify'] = 'center'
        self.__txtPosFeito.place(x=680, y=200)

        self.__lblUfMunicipio = Label(self.__frameProcessos, text='UF - Município', bg='LightSteelBlue3')
        self.__lblUfMunicipio['font'] = 'Serif', '12'
        self.__lblUfMunicipio.place(x=80, y=230)

        self.__txtUfMunicipio = Entry(self.__frameProcessos, width=40)
        self.__txtUfMunicipio.place(x=210, y=230)

        self.__lblVrCausa = Label(self.__frameProcessos, text='Valor Causa', bg='LightSteelBlue3')
        self.__lblVrCausa['font'] = 'Serif', '12'
        self.__lblVrCausa.place(x=570, y=230)

        self.__txtVrCausa = Entry(self.__frameProcessos, width=21)
        self.__txtVrCausa.place(x=680, y=230)

        self.__lblSitAtual = Label(self.__frameProcessos, text='Situação Atual', bg='LightSteelBlue3')
        self.__lblSitAtual['font'] = 'Serif', '12'
        self.__lblSitAtual.place(x=80, y=260)

        self.__txtSitAtual = ttk.Combobox(self.__frameProcessos, values=['FASE DE MOVIMENTAÇÃO', 'FASE DE DOCUMENTAÇÃO',
                                                                         'FASE DE COMUNICAÇÃO', 'FASE DE EXECUÇÃO'],
                                          width=25)
        self.__txtSitAtual['justify'] = 'center'
        self.__txtSitAtual.place(x=210, y=260)

        self.__lblVrAtual = Label(self.__frameProcessos, text='Valor Atual', bg='LightSteelBlue3')
        self.__lblVrAtual['font'] = 'Serif', '12'
        self.__lblVrAtual.place(x=575, y=260)

        self.__txtVrAtual = Entry(self.__frameProcessos, width=21)
        self.__txtVrAtual.place(x=680, y=260)

        self.__lblDataInicio = Label(self.__frameProcessos, text='Inicio', bg='LightSteelBlue3')
        self.__lblDataInicio['font'] = 'Serif', '12'
        self.__lblDataInicio.place(x=150, y=290)

        self.__txtDataInicio = Entry(self.__frameProcessos, width=10)
        self.__txtDataInicio.place(x=210, y=290)

        self.__btnSelecionarData = Button(self.__frameProcessos,
                                          image=imgbtn5,
                                          relief='flat',
                                          bg='LightSteelBlue3',
                                          highlightthickness=0)
        self.__btnSelecionarData.image = imgbtn5
        self.__btnSelecionarData['command'] = lambda: Calendario(self.__frameProcessos)
        self.__btnSelecionarData.place(x=297, y=288)

        self.__lblDataFim = Label(self.__frameProcessos, text='Fim', bg='LightSteelBlue3')
        self.__lblDataFim['font'] = 'Serif', '12'
        self.__lblDataFim.place(x=385, y=290)

        self.__txtDataFim = Entry(self.__frameProcessos, width=10)
        self.__txtDataFim.place(x=430, y=290)

        self.__btnSelecionarData = Button(self.__frameProcessos,
                                          image=imgbtn5,
                                          relief='flat',
                                          bg='LightSteelBlue3',
                                          highlightthickness=0)
        self.__btnSelecionarData.image = imgbtn5
        self.__btnSelecionarData['command'] = lambda: Calendario(self.__frameProcessos)
        self.__btnSelecionarData.place(x=517 , y=288)

        self.__lblPerda = Label(self.__frameProcessos, text='Perda', bg='LightSteelBlue3')
        self.__lblPerda['font'] = 'Serif', '12'
        self.__lblPerda.place(x=620, y=290)

        self.__txtPerda = Entry(self.__frameProcessos, width=21)
        self.__txtPerda.place(x=680, y=290)

        self.__lblPedido = Label(self.__frameProcessos, text='Pedido', bg='LightSteelBlue3')
        self.__lblPedido['font'] = 'Serif', '12'
        self.__lblPedido.place(x=145, y=320)

        self.__txtPedido = Text(self.__frameProcessos, width=30, height=3)
        self.__txtPedido.place(x=210, y=320)

        self.__lblObs = Label(self.__frameProcessos, text='Observações', bg='LightSteelBlue3')
        self.__lblObs['font'] = 'Serif', '12'
        self.__lblObs.place(x=495, y=320)

        self.__txtObs = Text(self.__frameProcessos, width=30, height=3)
        self.__txtObs.place(x=608, y=320)

        self.__btnSalvarRegistro = Button(self.__frameProcessos,
                                          text='Salvar Registro',
                                          compound=TOP,
                                          relief='flat',
                                          bg='LightSteelBlue3')
        self.__btnSalvarRegistro['image'] = imgbtn4
        self.__btnSalvarRegistro.image = imgbtn4
        self.__btnSalvarRegistro['command'] = lambda: self.insert_processo()
        self.__btnSalvarRegistro.place(x=400, y=390)

        self.__btnOcorrencias = Button(self.__frameProcessos,
                                       text='Ocorrências',
                                       compound=TOP,
                                       relief='flat',
                                       bg='LightSteelBlue3')
        self.__btnOcorrencias['image'] = imgbtn1
        self.__btnOcorrencias.image = imgbtn1
        self.__btnOcorrencias['command'] = lambda: app.switch_frame(self.ocorrencias)
        self.__btnOcorrencias.place(x=550, y=390)

        self.ocorrencias = Ocorrencias(self.master, self)

    @property
    def caso(self):
        return self.num_caso.get().split(' ')[2]

    @property
    def autor(self):
        return self.__txtAutor.get()

    @property
    def reu(self):
        return self.__txtReu.get()

    @property
    def adv_externo(self):
        return self.__txtAdvExterno.get()

    @property
    def adv_adverso(self):
        return self.__txtAdvAdverso.get()

    @property
    def end_parte_adv(self):
        return self.__txtEndParteAdversa.get()

    @property
    def tipo_acao(self):
        return self.__txtTipoAcao.get()

    @property
    def processo(self):
        return self.__txtNumProcesso.get()

    @property
    def vara_tribunal(self):
        return self.__txtVaraTribunal.get()

    @property
    def pos_feito(self):
        return self.__txtPosFeito.get()

    @property
    def uf_municipio(self):
        return self.__txtUfMunicipio.get()

    @property
    def vr_causa(self):
        return self.__txtVrCausa.get()

    @property
    def situacao(self):
        return self.__txtSitAtual.get()

    @property
    def vr_atual(self):
        return self.__txtVrAtual.get()

    @property
    def inicio(self):
        return self.__txtDataInicio.get()

    @property
    def fim(self):
        return self.__txtDataFim.get()

    @property
    def perda(self):
        return self.__txtPerda.get()

    @property
    def pedido(self):
        return self.__txtPedido.get(1.0, END)

    @property
    def observacao(self):
        return self.__txtObs.get(1.0, END)

    @property
    def advogados(self):
        return self.__txtAdvExterno.get()

    @advogados.setter
    def advogados(self, valor):
        self.__txtAdvExterno['values'] = valor

    def insert_processo(self):
        insert('processos', int(self.caso), self.autor, self.reu, self.adv_externo, self.adv_adverso, self.processo,
               self.inicio, self.vr_causa, self.tipo_acao, self.vara_tribunal, self.uf_municipio, self.situacao,
               self.pos_feito, self.observacao, self.vr_atual, self.pedido, self.fim, self.perda, self.end_parte_adv)

    def iniciar_pagina(self):
        self.ocultar_pagina()
        self.__frameProcessos.pack(side=BOTTOM, fill=X, pady=1)
        self.num_caso.set(f'Caso N° {randint(1, 20)}')
        advogados = [advogado for advogado in search('advogados', parms='nome')]
        advogados = [advogado[0] for advogado in advogados]
        self.advogados = advogados

    def ocultar_pagina(self):
        self.ocorrencias.ocultar_pagina()
        self.__frameProcessos.pack_forget()

    def command_advogados(self):
        advogados = AddAdvogado(self.master, None)
        advogados.iniciar_janela(self)

    def iniciar_botoes(self):
        self.ocultar_botoes()
        self.__btnOcorrencias.place(x=700, y=390)
        self.__btnSalvarRegistro.place(x=250, y=390)

    def ocultar_botoes(self):
        self.__btnSalvarRegistro.place_forget()
        self.__btnOcorrencias.place_forget()

