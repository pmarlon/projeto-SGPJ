from utils.modulos import *


class Ocorrencias:

    def __init__(self, master=None, app=None):
        imgbtn2 = PhotoImage(file='imagens/imgVoltar.png')  # imagem do botão Voltar
        imgbtn5 = PhotoImage(file='imagens/imgCalendario.png')  # imagem do botão Calendario
        imgbtn8 = PhotoImage(file='imagens/imgAdicionar.png')  # imagem do botão Nova Ocorrência

        self.app = app
        self.__frameOcorrencias = Frame(master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')

        self.__num_caso = StringVar()
        self.__tipo_acao = StringVar()
        self.__uf_municipio = StringVar()
        self.__autor = StringVar()
        self.__reu = StringVar()
        self.__num_processo = StringVar()
        self.__adv_externo = StringVar()

        self.__lblCaso = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblCaso['textvariable'] = self.num_caso
        self.__lblCaso['font'] = 'Serif', '12', 'bold'
        self.__lblCaso.place(x=400, y=20)

        self.__lblAutor = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblAutor['textvariable'] = self.autor
        self.__lblAutor['font'] = 'Serif', '12', 'bold'
        self.__lblAutor.place(x=210, y=60)

        self.__lblProcessso = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblProcessso['textvariable'] = self.num_processo
        self.__lblProcessso['font'] = 'Serif', '12', 'bold'
        self.__lblProcessso.place(x=210, y=90)

        self.__lblReu = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblReu['textvariable'] = self.reu
        self.__lblReu['font'] = 'Serif', '12', 'bold'
        self.__lblReu.place(x=210, y=120)

        self.__lblTipoAcao = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblTipoAcao['font'] = 'Serif', '12', 'bold'
        self.__lblTipoAcao['textvariable'] = self.tipo_acao
        self.__lblTipoAcao.place(x=210, y=150)

        self.__lblAdvExterno = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblAdvExterno['textvariable'] = self.adv_externo
        self.__lblAdvExterno['font'] = 'Serif', '12', 'bold'
        self.__lblAdvExterno.place(x=210, y=180)

        self.__lblUfMunicipio = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblUfMunicipio['textvariable'] = self.uf_municipio
        self.__lblUfMunicipio['font'] = 'Serif', '12', 'bold'
        self.__lblUfMunicipio.place(x=210, y=210)

        self.__lblDataOcorrencia = Label(self.__frameOcorrencias, text='Data', bg='LightSteelBlue3')
        self.__lblDataOcorrencia['font'] = 'Serif', '12'
        self.__lblDataOcorrencia.place(x=210, y=240)

        self.__txtDataOcorrencia = Entry(self.__frameOcorrencias, width=10)
        self.__txtDataOcorrencia.place(x=300, y=240)

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
        self.__btnAddOcorrencia['command'] = lambda: self.insert_ocorrencia()

        self.__btnVoltar = Button(self.__frameOcorrencias,
                                  text='Voltar',
                                  compound=TOP,
                                  relief='flat',
                                  bg='LightSteelBlue3')
        self.__btnVoltar['image'] = imgbtn2
        self.__btnVoltar.image = imgbtn2
        self.__btnVoltar['command'] = lambda: self.voltar()

    @property
    def num_caso(self):
        return self.__num_caso

    @num_caso.setter
    def num_caso(self, valor):
        self.__num_caso.set(f'Caso N° {valor}')

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, valor):
        self.__autor.set(f'Autor: {valor}')

    @property
    def num_processo(self):
        return self.__num_processo

    @num_processo.setter
    def num_processo(self, valor):
        self.__num_processo.set(f'Processo:{valor}')

    @property
    def reu(self):
        return self.__reu

    @reu.setter
    def reu(self, valor):
        self.__reu.set(f'Réu: {valor}')

    @property
    def tipo_acao(self):
        return self.__tipo_acao

    @tipo_acao.setter
    def tipo_acao(self, valor):
        self.__tipo_acao.set(f'Tipo da Ação: {valor}')

    @property
    def adv_externo(self):
        return self.__adv_externo

    @adv_externo.setter
    def adv_externo(self, valor):
        self.__adv_externo.set(f'Advogado Externo: {valor}')

    @property
    def uf_municipio(self):
        return self.__uf_municipio

    @uf_municipio.setter
    def uf_municipio(self, valor):
        self.__uf_municipio.set(f'Uf - Município: {valor}')

    @property
    def data_ocorrencia(self):
        return self.__txtDataOcorrencia.get()

    @data_ocorrencia.setter
    def data_ocorrencia(self, valor):
        self.__txtDataOcorrencia.insert(END, valor)

    @property
    def descricao(self):
        return self.__txtDescricao.get(1.0, END)

    @descricao.setter
    def descricao(self, valor):
        self.__txtDescricao.insert(END, valor)

    @property
    def valor(self):
        return self.__txtValor.get()

    @valor.setter
    def valor(self, valor):
        self.__txtValor.insert(END, valor)

    @property
    def vr_atual(self):
        return self.__txtValorAtual.get()

    @vr_atual.setter
    def vr_atual(self, valor):
        self.__txtValorAtual.insert(END, valor)

    def insert_ocorrencia(self):
        insert('ocorrencias', int(self.app.caso), self.data_ocorrencia, self.descricao, self.valor, self.vr_atual)

    def preencher(self, values=None):
        limpar(self.__frameOcorrencias)
        if values:
            self.num_caso = values[7]
            self.autor = values[0]
            self.num_processo = values[1]
            self.reu = values[2]
            self.tipo_acao = values[3]
            self.adv_externo = values[4]
            self.uf_municipio = values[5]
            self.data_ocorrencia = values[8]
            self.descricao = values[9]
            self.valor = values[10]
            self.vr_atual = values[11]

        else:
            # Recebe os Dados diretamente do "app" que nesse caso é Processos e mostra na página
            self.num_caso = self.app.caso
            self.autor = self.app.autor
            self.num_processo = self.app.processo
            self.reu = self.app.reu
            self.tipo_acao = self.app.tipo_acao
            self.adv_externo = self.app.adv_externo
            self.uf_municipio = self.app.uf_municipio

    def iniciar_pagina(self):
        self.__frameOcorrencias.pack(side=BOTTOM, fill=X, pady=1)
        self.__btnAddOcorrencia.place(x=350, y=370, relwidth=0.15)
        self.__btnVoltar.place(x=510, y=370, relwidth=0.15)
        self.preencher()

    def ocultar_pagina(self):
        self.__frameOcorrencias.pack_forget()

    def voltar(self):
        self.ocultar_pagina()
        self.app.ocultar_pagina()
        self.app.iniciar_pagina(novo=False)
