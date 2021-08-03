from utils.modulos import *


class Consultas:

    def __init__(self, master=None, app=None):
        imgbtn4 = PhotoImage(file='imagens/imgSalvar.png')  # imagem do botão Salvar Registro
        imgbtn8 = PhotoImage(file='imagens/imgAdicionar.png')  # imagem do botão Adicionar Registro
        img_cancelar = PhotoImage(file='imagens/imgCancelar.png')  # imagem do botão Cancelar
        img_calendario = PhotoImage(file='imagens/imgCalendario.png')  # imagem do botão calendário

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
        self.__lblEsperado.place(x=720, y=50)

        self.__txtEsperado = Entry(self.__frameConsultas, width=10)
        self.__txtEsperado.place(x=810, y=50)

        self.__lblOrigem = Label(self.__frameConsultas, text='Origem', bg='LightSteelBlue3')
        self.__lblOrigem['font'] = 'Serif', '12'
        self.__lblOrigem.place(x=80, y=80)

        self.__txtOrigem = Entry(self.__frameConsultas, width=66)
        self.__txtOrigem.place(x=160, y=80)

        self.__lblEntrada = Label(self.__frameConsultas, text='Entrada', bg='LightSteelBlue3')
        self.__lblEntrada['font'] = 'Serif', '12'
        self.__lblEntrada.place(x=730, y=80)

        self.__txtEntrada = Entry(self.__frameConsultas, width=10)
        self.__txtEntrada.place(x=810, y=80)

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
        self.__lblSaida.place(x=750, y=235)

        self.__txtSaida = Entry(self.__frameConsultas, width=10)
        self.__txtSaida.place(x=810, y=235)

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
        self.__btnSalvarRegistro['command'] = lambda: self.update_consulta()

        self.__btnAddRegistro = Button(self.__frameConsultas,
                                       text='Adicionar Registro',
                                       compound=TOP,
                                       relief='flat',
                                       bg='LightSteelBlue3')
        self.__btnAddRegistro['image'] = imgbtn8
        self.__btnAddRegistro.image = imgbtn8
        self.__btnAddRegistro['command'] = lambda: self.insert_consulta()

        self.__btnCancelar = Button(self.__frameConsultas,
                                    image=img_cancelar,
                                    text='Cancelar',
                                    compound=TOP,
                                    relief='flat',
                                    bg='LightSteelBlue3')
        self.__btnCancelar.image = img_cancelar
        self.__btnCancelar['command'] = lambda: self.iniciar_pagina()

        self.__btnCalendario = Button(self.__frameConsultas,
                                      image=img_calendario,
                                      relief='flat',
                                      bg='LightSteelBlue3',
                                      highlightthickness=0
                                      )
        self.__btnCalendario.image = img_calendario
        self.__btnCalendario['command'] = lambda: Calendario(self.__frameConsultas,
                                                             self.__txtEsperado.winfo_name())
        self.__btnCalendario.place(x=897, y=48)

        self.__btnCalendario = Button(self.__frameConsultas,
                                      image=img_calendario,
                                      relief='flat',
                                      bg='LightSteelBlue3',
                                      highlightthickness=0
                                      )
        self.__btnCalendario.image = img_calendario
        self.__btnCalendario['command'] = lambda: Calendario(self.__frameConsultas,
                                                             self.__txtEntrada.winfo_name())
        self.__btnCalendario.place(x=897, y=78)

        self.__btnCalendario = Button(self.__frameConsultas,
                                      image=img_calendario,
                                      relief='flat',
                                      bg='LightSteelBlue3',
                                      highlightthickness=0
                                      )
        self.__btnCalendario.image = img_calendario
        self.__btnCalendario['command'] = lambda: Calendario(self.__frameConsultas,
                                                             self.__txtSaida.winfo_name())
        self.__btnCalendario.place(x=897, y=232)

    @property
    def consulta(self):
        return self.__txtConsulta.get()

    @consulta.setter
    def consulta(self, valor):
        self.__txtConsulta.insert(END, valor)

    @property
    def ref(self):
        return self.__txtRef.get()

    @ref.setter
    def ref(self, valor):
        self.__txtRef.insert(END, valor)

    @property
    def prioridade(self):
        return self.__txtPrioridade.get()

    @prioridade.setter
    def prioridade(self, valor):
        self.__txtPrioridade.insert(END, valor)

    @property
    def esperado(self):
        return self.__txtEsperado.get()

    @esperado.setter
    def esperado(self, valor):
        self.__txtEsperado.insert(END, valor)

    @property
    def origem(self):
        return self.__txtOrigem.get()

    @origem.setter
    def origem(self, valor):
        self.__txtOrigem.insert(END, valor)

    @property
    def entrada(self):
        return self.__txtEntrada.get()

    @entrada.setter
    def entrada(self, valor):
        self.__txtEntrada.insert(END, valor)

    @property
    def assunto(self):
        return self.__txtAssunto.get(1.0, END)

    @assunto.setter
    def assunto(self, valor):
        self.__txtAssunto.insert(END, valor)

    @property
    def interessado(self):
        return self.__txtInteressado.get()

    @interessado.setter
    def interessado(self, valor):
        self.__txtInteressado.insert(END, valor)

    @property
    def adv_cojur(self):
        return self.__txtAdvCojur.get()

    @adv_cojur.setter
    def adv_cojur(self, valor):
        self.__txtAdvCojur.insert(END, valor)

    @property
    def destino(self):
        return self.__txtDestino.get()

    @destino.setter
    def destino(self, valor):
        self.__txtDestino.insert(END, valor)

    @property
    def saida(self):
        return self.__txtSaida.get()

    @saida.setter
    def saida(self, valor):
        self.__txtSaida.insert(END, valor)

    @property
    def emenda_result(self):
        return self.__txtEmendaResult.get(1.0, END)

    @emenda_result.setter
    def emenda_result(self, valor):
        self.__txtEmendaResult.insert(END, valor)

    def insert_consulta(self):
        try:
            insert('consultas', self.consulta, self.ref, self.prioridade, self.esperado, self.entrada, self.origem,
                   self.assunto, self.interessado, self.adv_cojur, self.emenda_result, self.saida, self.destino)
            messagebox.showinfo('Informação', 'Consulta adicionada com sucesso.')
            self.iniciar_pagina()
        except OperationalError:
            messagebox.showerror('Atenção', 'Ocorreu um erro...')
        except IntegrityError:
            messagebox.showwarning('Atenção', 'Já existe uma consulta com este número.')

    def update_consulta(self):
        consulta = self.consulta
        rid = search('consultas', parms='id', clause=f'WHERE consulta={consulta}')[0][0]

        update(rid, 'consultas',
               ref=self.ref,
               prioridade=self.prioridade,
               esperado=self.esperado,
               entrada=self.entrada,
               origem=self.origem,
               assunto=self.assunto,
               interessado=self.interessado,
               adv_cojur=self.adv_cojur,
               emenda=self.emenda_result,
               saida=self.saida,
               destino=self.destino
               )
        messagebox.showinfo('Informação', 'Registro alterado com Sucesso!')
        self.iniciar_pagina()

    def preencher(self, values):

        limpar(self.__frameConsultas)

        self.consulta = values[1]
        self.ref = values[2]
        self.prioridade = values[3]
        self.esperado = values[4]
        self.entrada = values[5]
        self.origem = values[6]
        self.assunto = values[7]
        self.interessado = values[8]
        self.adv_cojur = values[9]
        self.emenda_result = values[10]
        self.saida = values[11]
        self.destino = values[12]

        self.__txtConsulta['state'] = 'readonly'

    def trocar_botoes(self):
        if not self.__btnSalvarRegistro.place_info():
            self.__btnAddRegistro.place_forget()
            self.__btnCancelar.place(x=500, y=375, relwidth=0.13)
            self.__btnSalvarRegistro.place(x=350, y=375)

    def iniciar_pagina(self):
        self.ocultar_pagina()
        self.__txtConsulta['state'] = 'normal'
        limpar(self.__frameConsultas)
        self.__frameConsultas.pack(side=BOTTOM, fill=X, pady=1)
        self.__btnAddRegistro.place(x=450, y=375)
        self.__btnCancelar.place_forget()
        self.__btnSalvarRegistro.place_forget()

    def ocultar_pagina(self):
        self.__frameConsultas.pack_forget()
