from SGPJ.utils.modulos import *


class Ocorrencias:

    def __init__(self, master=None, app=None):
        imgbtn2 = PhotoImage(file='imagens/imgVoltar.png')  # imagem do botão Voltar
        imgbtn5 = PhotoImage(file='imagens/imgCalendario.png')  # imagem do botão Calendario
        imgbtn8 = PhotoImage(file='imagens/imgAdicionar.png')  # imagem do botão Nova Ocorrência

        self.app = app
        self.__frameOcorrencias = Frame(master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')

        num_caso = StringVar()
        tipo_acao = StringVar()
        uf_municipio = StringVar()
        autor = StringVar()
        reu = StringVar()
        num_processo = StringVar()
        adv_externo = StringVar()

        num_caso.set('CASO N° 12345')  # wee
        self.__lblCaso = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblCaso['textvariable'] = num_caso
        self.__lblCaso['font'] = 'Serif', '12', 'bold'
        self.__lblCaso.place(x=400, y=20)

        autor.set('Autor: NEYMAR DA SILVA JUNIOR')
        self.__lblAutor = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblAutor['textvariable'] = autor
        self.__lblAutor['font'] = 'Serif', '12', 'bold'
        self.__lblAutor.place(x=210, y=60)

        num_processo.set('Processo: 7000/2020')
        self.__lblProcessso = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblProcessso['textvariable'] = num_processo
        self.__lblProcessso['font'] = 'Serif', '12', 'bold'
        self.__lblProcessso.place(x=210, y=90)

        reu.set('Réu: BRUNA MARQUEZINE')
        self.__lblReu = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblReu['textvariable'] = reu
        self.__lblReu['font'] = 'Serif', '12', 'bold'
        self.__lblReu.place(x=210, y=120)

        tipo_acao.set('Tipo Ação: EXECUÇÃO')  # wee
        self.__lblTipoAcao = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblTipoAcao['font'] = 'Serif', '12', 'bold'
        self.__lblTipoAcao['textvariable'] = tipo_acao
        self.__lblTipoAcao.place(x=210, y=150)

        adv_externo.set('Adv Externo: PATRIC MARLON J. DA SILVA FONSECA')
        self.__lblAdvExterno = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblAdvExterno['textvariable'] = adv_externo
        self.__lblAdvExterno['font'] = 'Serif', '12', 'bold'
        self.__lblAdvExterno.place(x=210, y=180)

        uf_municipio.set('UF - Município: RJ - Rio de Janeiro')
        self.__lblUfMunicipio = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblUfMunicipio['textvariable'] = uf_municipio
        self.__lblUfMunicipio['font'] = 'Serif', '12', 'bold'
        self.__lblUfMunicipio.place(x=210, y=210)

        self.__lblDataOcorrencia = Label(self.__frameOcorrencias, text='Data', bg='LightSteelBlue3')
        self.__lblDataOcorrencia['font'] = 'Serif', '12'
        self.__lblDataOcorrencia.place(x=210, y=240)

        self.__txtDataOcorrencia = Entry(self.__frameOcorrencias, width=10)
        self.__txtDataOcorrencia.place(x=300, y=240)

        self.__btnSelecionarData = Button(self.__frameOcorrencias,
                                          image=imgbtn5,
                                          relief='flat',
                                          bg='LightSteelBlue3',
                                          highlightthickness=0)
        self.__btnSelecionarData.image = imgbtn5
        self.__btnSelecionarData['command'] = lambda: Calendario(self.__frameOcorrencias)
        self.__btnSelecionarData.place(x=272, y=238)

        self.__lblDescricao = Label(self.__frameOcorrencias, text='Descrição', bg='LightSteelBlue3')
        self.__lblDescricao['font'] = 'Serif', '12'
        self.__lblDescricao.place(x=210, y=270)

        self.__txtDescricao = Text(self.__frameOcorrencias, width=53, height=3)
        self.__txtDescricao.place(x=300, y=270)

        self.__lblValor = Label(self.__frameOcorrencias, text='Valor R$', bg='LightSteelBlue3')
        self.__lblValor['font'] = 'Serif', '12'
        self.__lblValor.place(x=210, y=335)

        self.__txtValor = Entry(self.__frameOcorrencias, width=15)
        self.__txtValor.place(x=300, y=335)

        self.__lblValorAtual = Label(self.__frameOcorrencias, text='Valor Atual R$', bg='LightSteelBlue3')
        self.__lblValorAtual['font'] = 'Serif', '12'
        self.__lblValorAtual.place(x=470, y=335)

        self.__txtValorAtual = Entry(self.__frameOcorrencias, width=15)
        self.__txtValorAtual.place(x=605, y=335)

        self.__btnAddOcorrencia = Button(self.__frameOcorrencias,
                                         text='Adicionar Ocorrência',
                                         compound=TOP,
                                         relief='flat',
                                         bg='LightSteelBlue3')
        self.__btnAddOcorrencia['image'] = imgbtn8
        self.__btnAddOcorrencia.image = imgbtn8
        self.__btnAddOcorrencia['command'] = ''
        self.__btnAddOcorrencia.place(x=350, y=370, relwidth=0.15)

        self.__btnVoltar = Button(self.__frameOcorrencias,
                                  text='Voltar',
                                  compound=TOP,
                                  relief='flat',
                                  bg='LightSteelBlue3')
        self.__btnVoltar['image'] = imgbtn2
        self.__btnVoltar.image = imgbtn2
        self.__btnVoltar['command'] = lambda: self.voltar()
        self.__btnVoltar.place(x=510, y=370, relwidth=0.15)

    def iniciar_pagina(self):
        self.__frameOcorrencias.pack(side=BOTTOM, fill=X, pady=1)

    def ocultar_pagina(self):
        self.__frameOcorrencias.pack_forget()

    def voltar(self):
        self.ocultar_pagina()
        self.app.ocultar_pagina()
        self.app.iniciar_pagina()
