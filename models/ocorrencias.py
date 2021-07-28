from utils.modulos import *


class Ocorrencias:

    def __init__(self, master=None, app=None):
        img_pesquisar = ImageTk.PhotoImage(Image.open('imagens/imgPesquisar.png').resize((28, 28), Image.ANTIALIAS))
        imgbtn2 = PhotoImage(file='imagens/imgVoltar.png')  # imagem do botão Voltar
        imgbtn4 = PhotoImage(file='imagens/imgSalvar.png')  # imagem do botão Salvar
        imgbtn8 = PhotoImage(file='imagens/imgAdicionar.png')  # imagem do botão Nova Ocorrência

        self.app = app
        self.__frameOcorrencias = Frame(master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')

        self.__lblCaso = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblCaso['text'] = 'N° do Caso'
        self.__lblCaso['font'] = 'Serif', '12', 'bold'
        self.__lblCaso.place(x=100, y=20)

        self.__txtCaso = Entry(self.__frameOcorrencias, width=10)
        self.__txtCaso.place(x=210, y=20)

        self.__lblAutor = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblAutor['text'] = 'Autor'
        self.__lblAutor['font'] = 'Serif', '12', 'bold'
        self.__lblAutor.place(x=140, y=60)

        self.__txtAutor = Entry(self.__frameOcorrencias, width=80, state='readonly')
        self.__txtAutor.place(x=210, y=60)

        self.__lblReu = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblReu['text'] = 'Réu'
        self.__lblReu['font'] = 'Serif', '12', 'bold'
        self.__lblReu.place(x=160, y=90)

        self.__txtReu = Entry(self.__frameOcorrencias, width=80, state='readonly')
        self.__txtReu.place(x=210, y=90)

        self.__lblAdvExterno = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblAdvExterno['text'] = 'Adv Externo'
        self.__lblAdvExterno['font'] = 'Serif', '12', 'bold'
        self.__lblAdvExterno.place(x=90, y=120)

        self.__txtAdvExterno = Entry(self.__frameOcorrencias, width=80, state='readonly')
        self.__txtAdvExterno.place(x=210, y=120)

        self.__lblTipoAcao = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblTipoAcao['font'] = 'Serif', '12', 'bold'
        self.__lblTipoAcao['text'] = 'Tipo Ação'
        self.__lblTipoAcao.place(x=110, y=150)

        self.__txtTipoAcao = Entry(self.__frameOcorrencias, width=80, state='readonly')
        self.__txtTipoAcao.place(x=210, y=150)

        self.__lblProcessso = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblProcessso['text'] = 'Processo'
        self.__lblProcessso['font'] = 'Serif', '12', 'bold'
        self.__lblProcessso.place(x=120, y=180)

        self.__txtProcesso = Entry(self.__frameOcorrencias, width=80, state='readonly')
        self.__txtProcesso.place(x=210, y=180)

        self.__lblUfMunicipio = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblUfMunicipio['text'] = 'UF - Município'
        self.__lblUfMunicipio['font'] = 'Serif', '12', 'bold'
        self.__lblUfMunicipio.place(x=60, y=210)

        self.__txtUfMunicipio = Entry(self.__frameOcorrencias, width=80, state='readonly')
        self.__txtUfMunicipio.place(x=210, y=210)

        self.__lblDataOcorrencia = Label(self.__frameOcorrencias, text='Data', bg='LightSteelBlue3')
        self.__lblDataOcorrencia['font'] = 'Serif', '12'
        self.__lblDataOcorrencia.place(x=160, y=240)

        self.__txtDataOcorrencia = Entry(self.__frameOcorrencias, width=10)
        self.__txtDataOcorrencia.place(x=210, y=240)

        self.__lblDescricao = Label(self.__frameOcorrencias, text='Descrição', bg='LightSteelBlue3')
        self.__lblDescricao['font'] = 'Serif', '12'
        self.__lblDescricao.place(x=110, y=285)

        self.__txtDescricao = Text(self.__frameOcorrencias, width=53, height=3)
        self.__txtDescricao.place(x=210, y=270)

        self.__lblValor = Label(self.__frameOcorrencias, text='Valor R$', bg='LightSteelBlue3')
        self.__lblValor['font'] = 'Serif', '12'
        self.__lblValor.place(x=130, y=335)

        self.__txtValor = Entry(self.__frameOcorrencias, width=15)
        self.__txtValor.place(x=210, y=335)

        self.__lblValorAtual = Label(self.__frameOcorrencias, text='Valor Atual R$', bg='LightSteelBlue3')
        self.__lblValorAtual['font'] = 'Serif', '12'
        self.__lblValorAtual.place(x=380, y=335)

        self.__txtValorAtual = Entry(self.__frameOcorrencias, width=15)
        self.__txtValorAtual.place(x=515, y=335)

        self.__btnAddOcorrencia = Button(self.__frameOcorrencias,
                                         text='Adicionar Ocorrência',
                                         compound=TOP,
                                         relief='flat',
                                         bg='LightSteelBlue3')
        self.__btnAddOcorrencia['image'] = imgbtn8
        self.__btnAddOcorrencia.image = imgbtn8
        self.__btnAddOcorrencia['command'] = lambda: self.insert_ocorrencia()

        self.__btnSalvar = Button(self.__frameOcorrencias,
                                  text='Salvar Ocorrência',
                                  compound=TOP,
                                  relief='flat',
                                  bg='LightSteelBlue3')
        self.__btnSalvar['image'] = imgbtn4
        self.__btnSalvar.image = imgbtn4
        self.__btnSalvar['command'] = lambda: self.update_ocorrencia()

        self.__btnVoltar = Button(self.__frameOcorrencias,
                                  text='Voltar',
                                  compound=TOP,
                                  relief='flat',
                                  bg='LightSteelBlue3')
        self.__btnVoltar['image'] = imgbtn2
        self.__btnVoltar.image = imgbtn2
        self.__btnVoltar['command'] = lambda: self.voltar()

        self.__btnPesquisar = Button(self.__frameOcorrencias,
                                     image=img_pesquisar,
                                     compound=TOP,
                                     relief='flat',
                                     bg='LightSteelBlue3',
                                     highlightthickness=False)
        self.__btnPesquisar.image = img_pesquisar
        self.__btnPesquisar['command'] = ''
        self.__btnPesquisar.place(x=300, y=15)

    @property
    def num_caso(self):
        return self.__txtCaso

    @num_caso.setter
    def num_caso(self, valor):
        self.__txtCaso.insert(END, valor)

    @property
    def autor(self):
        return self.__txtAutor.get()

    @autor.setter
    def autor(self, valor):
        self.__txtAutor.insert(END, valor)

    @property
    def num_processo(self):
        return self.__txtProcesso.get()

    @num_processo.setter
    def num_processo(self, valor):
        self.__txtProcesso.insert(END, valor)

    @property
    def reu(self):
        return self.__txtReu.get()

    @reu.setter
    def reu(self, valor):
        self.__txtReu.insert(END, valor)

    @property
    def tipo_acao(self):
        return self.__txtTipoAcao.get()

    @tipo_acao.setter
    def tipo_acao(self, valor):
        self.__txtTipoAcao.insert(END, valor)

    @property
    def adv_externo(self):
        return self.__txtAdvExterno.get()

    @adv_externo.setter
    def adv_externo(self, valor):
        self.__txtAdvExterno.insert(END, valor)

    @property
    def uf_municipio(self):
        return self.__txtUfMunicipio.get()

    @uf_municipio.setter
    def uf_municipio(self, valor):
        self.__txtUfMunicipio.insert(END, valor)

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
        try:
            insert('ocorrencias', int(self.app.caso), self.data_ocorrencia, self.descricao, self.valor, self.vr_atual)
            messagebox.showinfo('Informação', 'Ocorrência adicionada com sucesso.')
            limpar(self.__frameOcorrencias)

        except OperationalError:
            messagebox.showerror('Erro', 'Só é possível adicionar ocorrências à processos existentes.')

    def update_ocorrencia(self):
        caso = self.num_caso.get().split(' ')[2]
        rid = search('ocorrencias', parms='id', clause=f'where caso={caso}')[0][0]
        update(rid, 'ocorrencias',
               data=self.data_ocorrencia,
               descricao=self.descricao,
               valor=self.valor,
               vr_atual=self.vr_atual)

        messagebox.showinfo('Informação', 'Registro alterado com Sucesso!')
        self.iniciar_pagina()

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

    def iniciar_pagina(self):
        self.__frameOcorrencias.pack(side=BOTTOM, fill=X, pady=1)
        self.__btnAddOcorrencia.place(x=350, y=370, relwidth=0.15)
        self.__btnVoltar.place(x=510, y=370, relwidth=0.15)
        self.__btnSalvar.place_forget()
        self.preencher()

    def ocultar_pagina(self):
        self.__frameOcorrencias.pack_forget()

    def voltar(self):
        self.ocultar_pagina()
        self.app.ocultar_pagina()
        self.app.iniciar_pagina(novo=False)

    def trocar_botoes(self):
        if not self.__btnSalvar.place_info():
            self.__btnAddOcorrencia.place_forget()
            self.__btnVoltar.place_forget()
            self.__btnSalvar.place(x=400, y=390)
