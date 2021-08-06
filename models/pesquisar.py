from utils.modulos import *


class Pesquisar:

    def __init__(self, master=None, app=None):
        img_pesquisar = PhotoImage(data=base64.b64decode(img_pesquisar_base64))  # imagem do botão Pesquisar
        img_listar = PhotoImage(data=base64.b64decode(img_listar_doc_base64))  # imagem do botão Listar
        img_calendario = PhotoImage(data=base64.b64decode(img_calendario_base64))  # imagem do botão calendário
        img_editar = PhotoImage(data=base64.b64decode(img_editar_doc_base64))  # imagem do botão Editar
        img_excluir = PhotoImage(data=base64.b64decode(img_excluir_doc_base64))  # imagem do botão Excluir

        self.master = master
        self.app = app
        self.__framePesquisar = Frame(self.master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')

        # Define o Estilo dos Notebook
        style = ttk.Style()
        style.configure("TNotebook", background='LightSteelBlue3')
        style.configure("TNotebook.Tab", background='LightSteelBlue3')

        # Cria um Notebook
        self.__notebook = ttk.Notebook(self.__framePesquisar, height=500)
        self.__notebook.pack(side=BOTTOM, fill=X)

        # Abas do Notebook
        # Aba Pesquisar Processos
        self.__tbProcessos = Frame(self.__notebook, bg='LightSteelBlue3')
        self.__notebook.add(self.__tbProcessos,
                            text='Pesquisar Processos')

        self.__lblTitulo = Label(self.__tbProcessos, text='Pesquisar Processos', bg='LightSteelBlue3')
        self.__lblTitulo['font'] = 'Serif', '16', 'bold'
        self.__lblTitulo.place(x=325, y=10)

        self.__lblCaso = Label(self.__tbProcessos, text='N° do Caso', bg='LightSteelBlue3')
        self.__lblCaso['font'] = 'Serif', '12'
        self.__lblCaso.place(x=100, y=50)

        self.__txtCaso = Entry(self.__tbProcessos, width=20)
        self.__txtCaso.place(x=210, y=50)

        self.__lblProcesso = Label(self.__tbProcessos, text='N° do Processo', bg='LightSteelBlue3')
        self.__lblProcesso['font'] = 'Serif', '12'
        self.__lblProcesso.place(x=430, y=50)

        self.__txtProcesso = Entry(self.__tbProcessos, width=35)
        self.__txtProcesso.place(x=570, y=50)

        self.__lblAutor = Label(self.__tbProcessos, text='Autor', bg='LightSteelBlue3')
        self.__lblAutor['font'] = 'Serif', '12'
        self.__lblAutor.place(x=150, y=80)

        self.__txtAutor = Entry(self.__tbProcessos, width=80)
        self.__txtAutor.place(x=210, y=80)

        self.__lblAdvExterno = Label(self.__tbProcessos, text='Adv Externo', bg='LightSteelBlue3')
        self.__lblAdvExterno['font'] = 'Serif', '12'
        self.__lblAdvExterno.place(x=100, y=110)

        self.__txtAdvExterno = ttk.Combobox(self.__tbProcessos, values=['ANTÔNIO DOS ANZÓIS'],
                                            width=79)
        self.__txtAdvExterno['justify'] = 'left'
        self.__txtAdvExterno.place(x=210, y=110)

        self.__lblDataInicio = Label(self.__tbProcessos, text='Inicio', bg='LightSteelBlue3')
        self.__lblDataInicio['font'] = 'Serif', '12'
        self.__lblDataInicio.place(x=150, y=140)

        self.__txtDataInicio = Entry(self.__tbProcessos, width=10)
        self.__txtDataInicio.place(x=210, y=140)

        self.__lblDataFim = Label(self.__tbProcessos, text='Fim', bg='LightSteelBlue3')
        self.__lblDataFim['font'] = 'Serif', '12'
        self.__lblDataFim.place(x=340, y=140)

        self.__txtDataFim = Entry(self.__tbProcessos, width=10)
        self.__txtDataFim.place(x=380, y=140)

        self.__lblVaraTribunal = Label(self.__tbProcessos, text='Vara/Tribunal', bg='LightSteelBlue3')
        self.__lblVaraTribunal['font'] = 'Serif', '12'
        self.__lblVaraTribunal.place(x=500, y=140)

        self.__txtVaraTribunal = Entry(self.__tbProcessos, width=28)
        self.__txtVaraTribunal.place(x=630, y=140)

        self.__colunas = ('#1', '#2', '#3', '#4', '#5')
        self.__tvProcessos = ttk.Treeview(self.__tbProcessos, columns=self.__colunas, selectmode='browse', height=5)

        self.__tvProcessos.heading('#0', text='')
        self.__tvProcessos.heading('#1', text='N° Caso')
        self.__tvProcessos.heading('#2', text='N° Processo')
        self.__tvProcessos.heading('#3', text='Autor')
        self.__tvProcessos.heading('#4', text='Réu')
        self.__tvProcessos.heading('#5', text='Situação Atual')

        self.__tvProcessos.column('#0', width=0, stretch=NO)
        self.__tvProcessos.column('#1', width=70, anchor='center')
        self.__tvProcessos.column('#2', width=100, anchor='center')
        self.__tvProcessos.column('#3', width=200, anchor='center')
        self.__tvProcessos.column('#4', width=200, anchor='center')
        self.__tvProcessos.column('#5', width=150, anchor='center')
        self.__tvProcessos.column('#5', width=180, anchor='n')

        self.__tvProcessos.place(x=105, y=200)

        self.__btnPesquisar = criar_botao(self.__tbProcessos, 'Pesquisar', img_pesquisar,
                                          lambda: self.pesquisar_processos(), 300, 350)

        self.__btnListar = criar_botao(self.__tbProcessos, 'Listar', img_listar,
                                       lambda: self.listar_processos(), 410, 350)

        self.__btnEditar = criar_botao(self.__tbProcessos, 'Editar', img_editar,
                                       lambda: self.editar(self.app.frameProcessos, self.__tvProcessos, 'processos'),
                                       520, 350)

        self.__btnExcluir = criar_botao(self.__tbProcessos, 'Excluir', img_excluir,
                                        lambda: deletar(self.__tvProcessos, 'processos'), 630, 350)

        self.__btnCalendario = Button(self.__tbProcessos,
                                      image=img_calendario,
                                      relief='flat',
                                      bg='LightSteelBlue3',
                                      highlightthickness=0
                                      )
        self.__btnCalendario.image = img_calendario
        self.__btnCalendario['command'] = lambda: Calendario(self.__tbProcessos,
                                                             self.__txtDataInicio,
                                                             relx=self.__txtDataInicio.winfo_rootx(),
                                                             rely=self.__txtDataInicio.winfo_rooty())
        self.__btnCalendario.place(x=297, y=138)

        self.__btnCalendario = Button(self.__tbProcessos,
                                      image=img_calendario,
                                      relief='flat',
                                      bg='LightSteelBlue3',
                                      highlightthickness=0
                                      )
        self.__btnCalendario.image = img_calendario
        self.__btnCalendario['command'] = lambda: Calendario(self.__tbProcessos,
                                                             self.__txtDataFim,
                                                             relx=self.__txtDataFim.winfo_rootx(),
                                                             rely=self.__txtDataFim.winfo_rooty())
        self.__btnCalendario.place(x=467, y=138)

        # Aba Pesquisar Ocorrências
        self.__tbOcorrencias = Frame(self.__notebook, bg='LightSteelBlue3')
        self.__notebook.add(self.__tbOcorrencias,
                            text='Pesquisar Ocorrências')

        self.__lblTitulo = Label(self.__tbOcorrencias, text='Pesquisar Ocorrências', bg='LightSteelBlue3')
        self.__lblTitulo['font'] = 'Serif', '16', 'bold'
        self.__lblTitulo.place(x=320, y=10)

        self.__lblCasoOcorrencia = Label(self.__tbOcorrencias, text='Caso', bg='LightSteelBlue3')
        self.__lblCasoOcorrencia['font'] = 'Serif', '12'
        self.__lblCasoOcorrencia.place(x=100, y=80)

        self.__txtCasoOcorrencia = Entry(self.__tbOcorrencias, width=20)
        self.__txtCasoOcorrencia.place(x=150, y=80)

        self.__lblValorOcorrencia = Label(self.__tbOcorrencias, text='Valor', bg='LightSteelBlue3')
        self.__lblValorOcorrencia['font'] = 'Serif', '12'
        self.__lblValorOcorrencia.place(x=370, y=80)

        self.__txtValorOcorrencia = Entry(self.__tbOcorrencias, width=20)
        self.__txtValorOcorrencia.place(x=430, y=80)

        self.__lblDataOcorrencia = Label(self.__tbOcorrencias, text='Data', bg='LightSteelBlue3')
        self.__lblDataOcorrencia['font'] = 'Serif', '12'
        self.__lblDataOcorrencia.place(x=620, y=80)

        self.__txtDataOcorrencia = Entry(self.__tbOcorrencias, width=10)
        self.__txtDataOcorrencia.place(x=670, y=80)

        self.__colunas = ('#1', '#2', '#3', '#4', '#5')
        self.__tvOcorrencias = ttk.Treeview(self.__tbOcorrencias, columns=self.__colunas, selectmode='browse',
                                            height=8)

        self.__tvOcorrencias.heading('#0', text='')
        self.__tvOcorrencias.heading('#1', text='Caso')
        self.__tvOcorrencias.heading('#2', text='Data')
        self.__tvOcorrencias.heading('#3', text='Descrição')
        self.__tvOcorrencias.heading('#4', text='Valor')
        self.__tvOcorrencias.heading('#5', text='Valor Atual')

        self.__tvOcorrencias.column('#0', width=0, stretch=NO)
        self.__tvOcorrencias.column('#1', width=100, anchor='center')
        self.__tvOcorrencias.column('#2', width=100, anchor='center')
        self.__tvOcorrencias.column('#3', width=300, anchor='center')
        self.__tvOcorrencias.column('#4', width=150, anchor='center')
        self.__tvOcorrencias.column('#5', width=150, anchor='center')

        self.__tvOcorrencias.place(x=80, y=150)

        self.__btnPesquisar = criar_botao(self.__tbOcorrencias, 'Pesquisar', img_pesquisar,
                                          lambda: self.pesquisar_ocorrencias(), 200, 350)

        self.__btnListar = criar_botao(self.__tbOcorrencias, 'Listar', img_listar,
                                       lambda: self.listar_ocorrencias(), 310, 350)

        self.__btnEditar = criar_botao(self.__tbOcorrencias, 'Editar', img_editar,
                                       lambda: self.editar(self.app.frameOcorrencias,
                                                           self.__tvOcorrencias,
                                                           'ocorrencias'),
                                       420, 350)

        self.__btnExcluir = criar_botao(self.__tbOcorrencias, 'Excluir', img_excluir,
                                        lambda: deletar(self.__tvOcorrencias, 'ocorrencias'), 530, 350)

        self.__btnCalendario = Button(self.__tbOcorrencias,
                                      image=img_calendario,
                                      relief='flat',
                                      bg='LightSteelBlue3',
                                      highlightthickness=0
                                      )
        self.__btnCalendario.image = img_calendario
        self.__btnCalendario['command'] = lambda: Calendario(self.__tbOcorrencias,
                                                             self.__txtDataOcorrencia,
                                                             relx=self.__txtDataOcorrencia.winfo_rootx(),
                                                             rely=self.__txtDataOcorrencia.winfo_rooty())

        self.__btnCalendario.place(x=757, y=78)

        # Aba Pesquisar Consultas
        self.__tbConsultas = Frame(self.__notebook, bg='LightSteelBlue3')
        self.__notebook.add(self.__tbConsultas,
                            text='Pesquisar Consultas')

        self.__lblTitulo = Label(self.__tbConsultas, text='Pesquisar Consultas', bg='LightSteelBlue3')
        self.__lblTitulo['font'] = 'Serif', '16', 'bold'
        self.__lblTitulo.place(x=325, y=10)

        self.__lblConsulta = Label(self.__tbConsultas, text='Consulta', bg='LightSteelBlue3')
        self.__lblConsulta['font'] = 'Serif', '12'
        self.__lblConsulta.place(x=225, y=80)

        self.__txtConsulta = Entry(self.__tbConsultas, width=11)
        self.__txtConsulta.place(x=310, y=80)

        self.__lblPrioridade = Label(self.__tbConsultas, text='Prioridade', bg='LightSteelBlue3')
        self.__lblPrioridade['font'] = 'Serif', '12'
        self.__lblPrioridade.place(x=430, y=80)

        self.__txtPrioridade = ttk.Combobox(self.__tbConsultas, values=['ALTA', 'MÉDIA', 'BAIXA'], width=10)
        self.__txtPrioridade['justify'] = 'center'
        self.__txtPrioridade.place(x=523, y=80)

        self.__lblEntrada = Label(self.__tbConsultas, text='Entrada', bg='LightSteelBlue3')
        self.__lblEntrada['font'] = 'Serif', '12'
        self.__lblEntrada.place(x=230, y=110)

        self.__txtEntrada = Entry(self.__tbConsultas, width=10)
        self.__txtEntrada.place(x=310, y=110)

        self.__lblSaida = Label(self.__tbConsultas, text='Saída', bg='LightSteelBlue3')
        self.__lblSaida['font'] = 'Serif', '12'
        self.__lblSaida.place(x=460, y=110)

        self.__txtSaida = Entry(self.__tbConsultas, width=10)
        self.__txtSaida.place(x=521, y=110)

        self.__colunas = ('#1', '#2', '#3', '#4', '#5', '#6', '#7')
        self.__tvConsultas = ttk.Treeview(self.__tbConsultas, columns=self.__colunas, selectmode='browse',
                                          height=8)

        self.__tvConsultas.heading('#0', text='')
        self.__tvConsultas.heading('#1', text='Consulta')
        self.__tvConsultas.heading('#2', text='Prioridade')
        self.__tvConsultas.heading('#3', text='Entrada')
        self.__tvConsultas.heading('#4', text='Saída')
        self.__tvConsultas.heading('#5', text='Origem')
        self.__tvConsultas.heading('#6', text='Destino')
        self.__tvConsultas.heading('#7', text='Assunto')

        self.__tvConsultas.column('#0', width=0, stretch=NO)
        self.__tvConsultas.column('#1', width=100, anchor='center')
        self.__tvConsultas.column('#2', width=100, anchor='center')
        self.__tvConsultas.column('#3', width=100, anchor='center')
        self.__tvConsultas.column('#4', width=100, anchor='center')
        self.__tvConsultas.column('#5', width=150, anchor='center')
        self.__tvConsultas.column('#6', width=150, anchor='center')
        self.__tvConsultas.column('#7', width=200, anchor='center')

        self.__tvConsultas.place(x=25, y=160)

        self.__btnPesquisar = criar_botao(self.__tbConsultas, 'Pesquisar', img_pesquisar,
                                          lambda: self.pesquisar_consultas(), 250, 360)

        self.__btnListar = criar_botao(self.__tbConsultas, 'Listar', img_listar,
                                       lambda: self.listar_consultas(), 360, 360)

        self.__btnEditar = criar_botao(self.__tbConsultas, 'Editar', img_editar,
                                       lambda: self.editar(self.app.frameConsultas, self.__tvConsultas, 'consultas'),
                                       470, 360)

        self.__btnExcluir = criar_botao(self.__tbConsultas, 'Excluir', img_excluir,
                                        lambda: deletar(self.__tvConsultas, 'consultas'), 580, 360)

        self.__btnCalendario = Button(self.__tbConsultas,
                                      image=img_calendario,
                                      relief='flat',
                                      bg='LightSteelBlue3',
                                      highlightthickness=0
                                      )
        self.__btnCalendario.image = img_calendario
        self.__btnCalendario['command'] = lambda: Calendario(self.__tbConsultas,
                                                             self.__txtEntrada,
                                                             relx=self.__txtEntrada.winfo_rootx(),
                                                             rely=self.__txtEntrada.winfo_rooty())
        self.__btnCalendario.place(x=397, y=108)

        self.__btnCalendario = Button(self.__tbConsultas,
                                      image=img_calendario,
                                      relief='flat',
                                      bg='LightSteelBlue3',
                                      highlightthickness=0
                                      )
        self.__btnCalendario.image = img_calendario
        self.__btnCalendario['command'] = lambda: Calendario(self.__tbConsultas,
                                                             self.__txtSaida,
                                                             relx=self.__txtSaida.winfo_rootx(),
                                                             rely=self.__txtSaida.winfo_rooty())
        self.__btnCalendario.place(x=607, y=108)

    @property
    def caso(self):
        return self.__txtCaso.get()

    @property
    def processo(self):
        return self.__txtProcesso.get()

    @property
    def autor(self):
        return self.__txtAutor.get()

    @property
    def adv_externo(self):
        return self.__txtAdvExterno.get()

    @adv_externo.setter
    def adv_externo(self, valor):
        self.__txtAdvExterno['values'] = valor

    @property
    def inicio(self):
        return self.__txtDataInicio.get()

    @property
    def fim(self):
        return self.__txtDataFim.get()

    @property
    def vara_tribunal(self):
        return self.__txtVaraTribunal.get()

    @property
    def caso_ocorrencia(self):
        return self.__txtCasoOcorrencia.get()

    @property
    def valor_ocorrencia(self):
        return self.__txtValorOcorrencia.get()

    @property
    def data_ocorrencia(self):
        return self.__txtDataOcorrencia.get()

    @property
    def consulta(self):
        return self.__txtConsulta.get()

    @property
    def prioridade(self):
        return self.__txtPrioridade.get()

    @property
    def entrada(self):
        return self.__txtEntrada.get()

    @property
    def saida(self):
        return self.__txtSaida.get()

    def listar_processos(self):
        self.__tvProcessos.delete(*self.__tvProcessos.get_children())
        processos = view('processos')
        for processo in processos:
            self.__tvProcessos.insert('', END, iid=None,
                                      values=(processo[1], processo[6],
                                              processo[2], processo[3], processo[12]))

    def listar_ocorrencias(self):
        self.__tvOcorrencias.delete(*self.__tvOcorrencias.get_children())
        ocorrencias = view('ocorrencias')
        for ocorrencia in ocorrencias:
            self.__tvOcorrencias.insert('', END, iid=None,
                                        values=(ocorrencia[1], ocorrencia[2],
                                                ocorrencia[3], ocorrencia[4], ocorrencia[5]))

    def listar_consultas(self):
        self.__tvConsultas.delete(*self.__tvConsultas.get_children())
        consultas = view('consultas')
        for consulta in consultas:
            self.__tvConsultas.insert('', END, iid=None,
                                      values=(consulta[1], consulta[3], consulta[5], consulta[11],
                                              consulta[6], consulta[12], consulta[7]))

    def pesquisar_processos(self):
        self.__tvProcessos.delete(*self.__tvProcessos.get_children())

        if (self.caso != '') and (self.processo != '') and (self.autor != '') and (self.adv_externo != '') and \
                (self.inicio != '') and (self.fim != '') and (self.vara_tribunal != ''):

            processos = search('processos', clause=f'where caso="{self.caso}" and processo="{self.processo}" and '
                                                   f'autor="{self.autor}" and adv_externo="{self.adv_externo}" and '
                                                   f'inicio="{self.inicio}" and fim="{self.fim}" and '
                                                   f'vara_tribunal="{self.vara_tribunal}"')

        elif (self.caso != '') or (self.processo != '') or (self.autor != '') or (self.adv_externo != '') or \
                (self.inicio != '') or (self.fim != '') or (self.vara_tribunal != ''):
            processos = search('processos', clause=f'where caso="{self.caso}" or processo="{self.processo}" or '
                                                   f'autor="{self.autor}" or adv_externo="{self.adv_externo}" or '
                                                   f'inicio="{self.inicio}" or fim="{self.fim}" or '
                                                   f'vara_tribunal="{self.vara_tribunal}"')

        elif (self.caso != '') and ((self.processo != '') or (self.autor != '') or (self.adv_externo != '') or
                                    (self.inicio != '') or (self.fim != '') or (self.vara_tribunal != '')):

            processos = search('processos', clause=f'where caso="{self.caso}" and (processo="{self.processo}" or '
                                                   f'autor="{self.autor}" or adv_externo="{self.adv_externo}" or '
                                                   f'inicio="{self.inicio}" or fim="{self.fim}" or '
                                                   f'vara_tribunal="{self.vara_tribunal}")')

        elif (self.processo != '') and (self.autor != '') and (self.adv_externo != '') and \
                (self.inicio != '') and (self.fim != '') and (self.vara_tribunal != ''):
            processos = search('processos', clause=f'where processo="{self.processo}" and '
                                                   f'autor="{self.autor}" and adv_externo="{self.adv_externo}" and '
                                                   f'inicio="{self.inicio}" and fim="{self.fim}" and '
                                                   f'vara_tribunal="{self.vara_tribunal}"')

        elif (self.processo != '') and ((self.autor != '') or (self.adv_externo != '') or
                                        (self.inicio != '') or (self.fim != '') or (self.vara_tribunal != '')):
            processos = search('processos', clause=f'where processo="{self.processo}" and  '
                                                   f'(autor="{self.autor}" or adv_externo="{self.adv_externo}" or '
                                                   f'inicio="{self.inicio}" or fim="{self.fim}" or '
                                                   f'vara_tribunal="{self.vara_tribunal}")')

        elif (self.autor != '') and (self.adv_externo != '') and \
                (self.inicio != '') and (self.fim != '') and (self.vara_tribunal != ''):
            processos = search('processos', clause=f'where autor="{self.autor}" and adv_externo="{self.adv_externo}" '
                                                   f'and inicio="{self.inicio}" and fim="{self.fim}" and '
                                                   f'vara_tribunal="{self.vara_tribunal}"')

        elif (self.autor != '') and ((self.adv_externo != '') or (self.inicio != '') or (self.fim != '')
                                     or (self.vara_tribunal != '')):
            processos = search('processos', clause=f'where autor="{self.autor}" and (adv_externo="{self.adv_externo}" '
                                                   f'or inicio="{self.inicio}" or fim="{self.fim}" or '
                                                   f'vara_tribunal="{self.vara_tribunal}")')

        elif (self.adv_externo != '') and (self.inicio != '') and (self.fim != '') and (self.vara_tribunal != ''):
            processos = search('processos', clause=f'where adv_externo="{self.adv_externo}" and inicio="{self.inicio}"'
                                                   f' and fim="{self.fim}" and vara_tribunal="{self.vara_tribunal}"')

        elif (self.adv_externo != '') and ((self.inicio != '') or (self.fim != '') or (self.vara_tribunal != '')):
            processos = search('processos', clause=f'where adv_externo="{self.adv_externo}" and (inicio="{self.inicio}"'
                                                   f' or fim="{self.fim}" or vara_tribunal="{self.vara_tribunal}")')

        elif (self.inicio != '') and (self.fim != '') and (self.vara_tribunal != ''):
            processos = search('processos', clause=f'where inicio="{self.inicio}" and fim="{self.fim}" and '
                                                   f'vara_tribunal="{self.vara_tribunal}"')

        elif (self.inicio != '') and ((self.fim != '') or (self.vara_tribunal != '')):
            processos = search('processos', clause=f'where inicio="{self.inicio}" and (fim="{self.fim}" or '
                                                   f'vara_tribunal="{self.vara_tribunal}")')

        elif (self.fim != '') and (self.vara_tribunal != ''):
            processos = search('processos', clause=f'where fim="{self.fim}" and vara_tribunal="{self.vara_tribunal}"')

        try:
            if len(processos) == 0:
                messagebox.showwarning('Atenção', 'Nenhum Registro encontrado.')
            else:
                for processo in processos:
                    self.__tvProcessos.insert('', END, iid=None,
                                              values=(processo[1], processo[6],
                                                      processo[2], processo[3], processo[12]))
        except UnboundLocalError:
            pass

    def pesquisar_ocorrencias(self):

        self.__tvOcorrencias.delete(*self.__tvOcorrencias.get_children())

        if (self.caso_ocorrencia != '') and (self.valor_ocorrencia != '') and (self.data_ocorrencia != ''):
            ocorrencias = search('ocorrencias', clause=f'where caso="{self.caso_ocorrencia}" and '
                                                       f'valor="{self.valor_ocorrencia}" and '
                                                       f'data="{self.data_ocorrencia}"')

        elif (self.caso_ocorrencia != '') or (self.valor_ocorrencia != '') or (self.data_ocorrencia != ''):
            ocorrencias = search('ocorrencias', clause=f'where caso="{self.caso_ocorrencia}" or '
                                                       f'valor="{self.valor_ocorrencia}" or '
                                                       f'data="{self.data_ocorrencia}"')

        elif (self.caso_ocorrencia != '') and ((self.valor_ocorrencia != '') or (self.data_ocorrencia != '')):
            ocorrencias = search('ocorrencias', clause=f'where caso="{self.caso_ocorrencia}" and '
                                                       f'(valor="{self.valor_ocorrencia}" or '
                                                       f'data="{self.data_ocorrencia}")')
        try:

            if len(ocorrencias) == 0:
                messagebox.showwarning('Atenção', 'Nenhum Registro encontrado.')
            else:
                for ocorrencia in ocorrencias:
                    self.__tvOcorrencias.insert('', END, iid=None,
                                                values=(ocorrencia[1], ocorrencia[2],
                                                        ocorrencia[3], ocorrencia[4], ocorrencia[5]))
        except UnboundLocalError:
            pass

    def pesquisar_consultas(self):
        self.__tvConsultas.delete(*self.__tvConsultas.get_children())
        if (self.consulta != '') and (self.prioridade != '') and (self.entrada != '') and (self.saida != ''):
            consultas = search('consultas',
                               clause=f'where consulta="{self.consulta}" and prioridade="{self.prioridade}" and '
                                      f'entrada="{self.entrada}" and saida="{self.saida}"')

        elif (self.consulta != '') or (self.prioridade != '') or (self.entrada != '') or (self.saida != ''):
            consultas = search('consultas',
                               clause=f'where consulta="{self.consulta}" or prioridade="{self.prioridade}" or '
                                      f'entrada="{self.entrada}" or saida="{self.saida}"')

        elif (self.consulta != '') and ((self.prioridade != '') or (self.entrada != '') or (self.saida != '')):
            consultas = search('consultas',
                               clause=f'where consulta="{self.consulta}" and (prioridade="{self.prioridade}" or '
                                      f'entrada="{self.entrada}" or saida="{self.saida}")')

        elif (self.prioridade != '') and (self.entrada != '') and (self.saida != ''):
            consultas = search('consultas',
                               clause=f'where prioridade="{self.prioridade}" and '
                                      f'entrada="{self.entrada}" and saida="{self.saida}"')

        elif (self.prioridade != '') and ((self.entrada != '') or (self.saida != '')):
            consultas = search('consultas',
                               clause=f'where prioridade="{self.prioridade}" and '
                                      f'(entrada="{self.entrada}" or saida="{self.saida}")')

        elif (self.entrada != '') and (self.saida != ''):
            consultas = search('consultas',
                               clause=f'where entrada="{self.entrada}" and saida="{self.saida}"')

        try:

            if len(consultas) == 0:
                messagebox.showwarning('Atenção', 'Nenhum Registro encontrado.')
            else:
                for consulta in consultas:
                    self.__tvConsultas.insert('', END, iid=None,
                                              values=(consulta[1], consulta[3], consulta[5], consulta[11],
                                                      consulta[6], consulta[12], consulta[7]))

        except UnboundLocalError:
            pass

    def iniciar_pagina(self):
        self.ocultar_pagina()
        limpar(self.__tbProcessos, self.__tvProcessos)
        limpar(self.__tbConsultas, self.__tvConsultas)
        limpar(self.__tbOcorrencias, self.__tvOcorrencias)
        self.atualizar__advogados()
        self.__framePesquisar.pack(side=BOTTOM, fill=X, pady=1)

    def ocultar_pagina(self):
        self.__framePesquisar.pack_forget()

    def atualizar__advogados(self):
        advogados = [advogado for advogado in search('advogados', parms='nome')]
        advogados = [advogado[0] for advogado in advogados]
        self.adv_externo = advogados

    def editar(self, frame, tv, tabela):
        try:

            rid = get_id(tv, tabela)
            if tabela == 'ocorrencias':
                values = search('processos as p, ocorrencias as o', parms='p.autor,p.processo, p.reu, '
                                                                          'p.tipo_acao, p.adv_externo, '
                                                                          'p.uf_municipio, o.*',
                                clause=f'where  p.caso = o.caso and o.id="{rid}"')[0]

            else:
                values = search(tabela, clause=f'where id={rid}')[0]

        except OperationalError:
            messagebox.showerror('Atenção', 'Ocorreu um erro...')
        except IndexError:
            messagebox.showerror('Atenção', 'Você precisa selecionar um registro.')
        else:
            self.app.switch_frame(frame)
            frame.trocar_botoes()
            frame.preencher(values)
