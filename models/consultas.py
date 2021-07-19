from utils.modulos import *


class Consultas:

    def __init__(self, master=None, app=None):
        imgbtn4 = PhotoImage(file='imagens/imgSalvar.png')  # imagem do botão Salvar Registro
        imgbtn5 = PhotoImage(file='imagens/imgCalendario.png')  # imagem do botão Calendario
        self.master = master
        self.app = app
        self.__frameConsultas = Frame(self.master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')

        self.__lblConsulta = Label(self.__frameConsultas, text='Consulta', bg='LightSteelBlue3')
        self.__lblConsulta['font'] = 'Serif', '12'
        self.__lblConsulta.place(x=75, y=20)

        self.__txtConsulta = Entry(self.__frameConsultas, width=8)
        self.__txtConsulta.place(x=160, y=20)

        self.__lblRef = Label(self.__frameConsultas, text='REF', bg='LightSteelBlue3')
        self.__lblRef['font'] = 'Serif', '12'
        self.__lblRef.place(x=110, y=50)

        self.__txtRef = Entry(self.__frameConsultas, width=40)
        self.__txtRef.place(x=160, y=50)

        self.__lblPrioridade = Label(self.__frameConsultas, text='Prioridade', bg='LightSteelBlue3')
        self.__lblPrioridade['font'] = 'Serif', '12'
        self.__lblPrioridade.place(x=500, y=50)

        self.__txtPrioridade = ttk.Combobox(self.__frameConsultas, values=['ALTA', 'MÉDIA', 'BAIXA'], width=10)
        self.__txtPrioridade['justify'] = 'center'
        self.__txtPrioridade.place(x=595, y=50)

        self.__lblEsperado = Label(self.__frameConsultas, text='Esperado', bg='LightSteelBlue3')
        self.__lblEsperado['font'] = 'Serif', '12'
        self.__lblEsperado.place(x=705, y=50)

        self.__txtEsperado = Entry(self.__frameConsultas, width=10)
        self.__txtEsperado.place(x=790, y=50)

        self.__btnSelecionarData = Button(self.__frameConsultas,
                                          image=imgbtn5,
                                          relief='flat',
                                          bg='LightSteelBlue3',
                                          highlightthickness=0)
        self.__btnSelecionarData.image = imgbtn5
        self.__btnSelecionarData['command'] = lambda: Calendario(self.__frameConsultas)
        self.__btnSelecionarData.place(x=880, y=48)

        self.__lblOrigem = Label(self.__frameConsultas, text='Origem', bg='LightSteelBlue3')
        self.__lblOrigem['font'] = 'Serif', '12'
        self.__lblOrigem.place(x=80, y=80)

        self.__txtOrigem = Entry(self.__frameConsultas, width=65)
        self.__txtOrigem.place(x=160, y=80)

        self.__lblEntrada = Label(self.__frameConsultas, text='Entrada', bg='LightSteelBlue3')
        self.__lblEntrada['font'] = 'Serif', '12'
        self.__lblEntrada.place(x=710, y=80)

        self.__txtEntrada = Entry(self.__frameConsultas, width=10)
        self.__txtEntrada.place(x=790, y=80)

        self.__btnSelecionarData = Button(self.__frameConsultas,
                                          image=imgbtn5,
                                          relief='flat',
                                          bg='LightSteelBlue3',
                                          highlightthickness=0)
        self.__btnSelecionarData.image = imgbtn5
        self.__btnSelecionarData['command'] = lambda: Calendario(self.__frameConsultas)
        self.__btnSelecionarData.place(x=880, y=78)

        self.__lblAssunto = Label(self.__frameConsultas, text='Assunto', bg='LightSteelBlue3')
        self.__lblAssunto['font'] = 'Serif', '12'
        self.__lblAssunto.place(x=80, y=110)

        self.__txtAssunto = Text(self.__frameConsultas, width=93, height=3)
        self.__txtAssunto.place(x=160, y=110)

        self.__lblInteressado = Label(self.__frameConsultas, text='Interessado', bg='LightSteelBlue3')
        self.__lblInteressado['font'] = 'Serif', '12'
        self.__lblInteressado.place(x=50, y=175)

        self.__txtInteressado = Entry(self.__frameConsultas, width=93)
        self.__txtInteressado.place(x=160, y=175)

        self.__lblAdvCojur = Label(self.__frameConsultas, text='Advogado Cojur', bg='LightSteelBlue3')
        self.__lblAdvCojur['font'] = 'Serif', '12'
        self.__lblAdvCojur.place(x=10, y=205)

        self.__txtAdvCojur = Entry(self.__frameConsultas, width=93)
        self.__txtAdvCojur.place(x=160, y=205)

        self.__lblDestino = Label(self.__frameConsultas, text='Destino', bg='LightSteelBlue3')
        self.__lblDestino['font'] = 'Serif', '12'
        self.__lblDestino.place(x=80, y=235)

        self.__txtDestino = Entry(self.__frameConsultas, width=65)
        self.__txtDestino.place(x=160, y=235)

        self.__lblSaida = Label(self.__frameConsultas, text='Saída', bg='LightSteelBlue3')
        self.__lblSaida['font'] = 'Serif', '12'
        self.__lblSaida.place(x=730, y=235)

        self.__txtSaida = Entry(self.__frameConsultas, width=10)
        self.__txtSaida.place(x=790, y=235)

        self.__btnSelecionarData = Button(self.__frameConsultas,
                                          image=imgbtn5,
                                          relief='flat',
                                          bg='LightSteelBlue3',
                                          highlightthickness=0)
        self.__btnSelecionarData.image = imgbtn5
        self.__btnSelecionarData['command'] = lambda: Calendario(self.__frameConsultas)
        self.__btnSelecionarData.place(x=880, y=233)

        self.__lblEmendaResult = Label(self.__frameConsultas, text='Emenda/Resultado', bg='LightSteelBlue3')
        self.__lblEmendaResult['font'] = 'Serif', '12'
        self.__lblEmendaResult.place(x=5, y=265)

        self.__txtEmendaResult = Text(self.__frameConsultas, width=93, height=5)
        self.__txtEmendaResult.place(x=160, y=265)

        self.__btnSalvarRegistro = Button(self.__frameConsultas,
                                          text='Salvar Registro',
                                          compound=TOP,
                                          relief='flat',
                                          bg='LightSteelBlue3')
        self.__btnSalvarRegistro['image'] = imgbtn4
        self.__btnSalvarRegistro.image = imgbtn4
        self.__btnSalvarRegistro['command'] = lambda: self.insert_consulta()
        self.__btnSalvarRegistro.place(x=450, y=375)

    @property
    def consulta(self):
        return self.__txtConsulta.get()

    @property
    def ref(self):
        return self.__txtRef.get()

    @property
    def prioridade(self):
        return self.__txtPrioridade.get()

    @property
    def esperado(self):
        return self.__txtEsperado.get()

    @property
    def origem(self):
        return self.__txtOrigem.get()

    @property
    def entrada(self):
        return self.__txtEntrada.get()

    @property
    def assunto(self):
        return self.__txtAssunto.get(1.0, END)

    @property
    def interessado(self):
        return self.__txtInteressado.get()

    @property
    def adv_cojur(self):
        return self.__txtAdvCojur.get()

    @property
    def destino(self):
        return self.__txtDestino.get()

    @property
    def saida(self):
        return self.__txtSaida.get()

    @property
    def emenda_result(self):
        return self.__txtEmendaResult.get(1.0, END)

    def insert_consulta(self):
        insert('consultas', int(self.consulta), self.ref, self.prioridade, self.esperado, self.entrada,
               self.origem, self.assunto, self.interessado, self.emenda_result, self.saida, self.destino)

    def iniciar_pagina(self):
        self.ocultar_pagina()
        self.__frameConsultas.pack(side=BOTTOM, fill=X, pady=1)

    def ocultar_pagina(self):
        self.__frameConsultas.pack_forget()
