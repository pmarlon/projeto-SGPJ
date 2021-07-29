from utils.modulos import *


class Pesquisar:

    def __init__(self, master=None, app=None):
        img_pesquisar = PhotoImage(file='imagens/imgPesquisar.png')  # imagem do botão Pesquisar
        img_listar = PhotoImage(file='imagens/imgListarDoc')  # imagem do botão Listar
        imgbtn6 = PhotoImage(file='imagens/imgEditar.png')  # imagem do botão Editar
        imgbtn7 = PhotoImage(file='imagens/imgExcluirRegistro.png')  # imagem do botão Excluir

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

        self.__btnPesquisar = criar_botao(self.__tbProcessos, 'Pesquisar', img_pesquisar, '', 300, 350)

        self.__btnListar = criar_botao(self.__tbProcessos, 'Listar', img_listar,
                                       lambda: self.listar_processos(), 410, 350)

        self.__btnEditar = criar_botao(self.__tbProcessos, 'Editar', imgbtn6,
                                       lambda: self.editar(self.app.frameProcessos, self.__tvProcessos, 'processos'),
                                       520, 350)

        self.__btnExcluir = criar_botao(self.__tbProcessos, 'Excluir', imgbtn7,
                                        lambda: deletar(self.__tvProcessos, 'processos'), 630, 350)

        # Aba Pesquisar Ocorrências
        self.__tbOcorrencias = Frame(self.__notebook, bg='LightSteelBlue3')
        self.__notebook.add(self.__tbOcorrencias,
                            text='Pesquisar Ocorrências')

        self.__lblTitulo = Label(self.__tbOcorrencias, text='Pesquisar Ocorrências', bg='LightSteelBlue3')
        self.__lblTitulo['font'] = 'Serif', '16', 'bold'
        self.__lblTitulo.place(x=320, y=10)

        self.__lblCaso = Label(self.__tbOcorrencias, text='Caso', bg='LightSteelBlue3')
        self.__lblCaso['font'] = 'Serif', '12'
        self.__lblCaso.place(x=100, y=80)

        self.__txtCaso = Entry(self.__tbOcorrencias, width=20)
        self.__txtCaso.place(x=150, y=80)

        self.__lblProcesso = Label(self.__tbOcorrencias, text='Processo', bg='LightSteelBlue3')
        self.__lblProcesso['font'] = 'Serif', '12'
        self.__lblProcesso.place(x=340, y=80)

        self.__txtProcesso = Entry(self.__tbOcorrencias, width=20)
        self.__txtProcesso.place(x=430, y=80)

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

        self.__btnPesquisar = criar_botao(self.__tbOcorrencias, 'Pesquisar', img_pesquisar, '', 200, 350)

        self.__btnListar = criar_botao(self.__tbOcorrencias, 'Listar', img_listar,
                                       lambda: self.listar_ocorrencias(), 310, 350)

        self.__btnEditar = criar_botao(self.__tbOcorrencias, 'Editar', imgbtn6,
                                       lambda: self.editar(self.app.frameOcorrencias,
                                                           self.__tvOcorrencias,
                                                           'ocorrencias'),
                                       420, 350)

        self.__btnExcluir = criar_botao(self.__tbOcorrencias, 'Excluir', imgbtn7,
                                        lambda: deletar(self.__tvOcorrencias, 'ocorrencias'), 530, 350)

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

        self.__btnPesquisar = criar_botao(self.__tbConsultas, 'Pesquisar', img_pesquisar, '', 250, 360)

        self.__btnListar = criar_botao(self.__tbConsultas, 'Listar', img_listar,
                                       lambda: self.listar_consultas(), 360, 360)

        self.__btnEditar = criar_botao(self.__tbConsultas, 'Editar', imgbtn6,
                                       lambda: self.editar(self.app.frameConsultas, self.__tvConsultas, 'consultas'),
                                       470, 360)

        self.__btnExcluir = criar_botao(self.__tbConsultas, 'Excluir', imgbtn7,
                                        lambda: deletar(self.__tvConsultas, 'consultas'), 580, 360)

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
                                      values=(consulta[1], consulta[3], consulta[5], consulta[10],
                                              consulta[6], consulta[11], consulta[7]))

    def iniciar_pagina(self):
        self.ocultar_pagina()
        limpar(self.__framePesquisar, self.__tvConsultas)
        limpar(self.__framePesquisar, self.__tvProcessos)
        limpar(self.__framePesquisar, self.__tvOcorrencias)
        self.__framePesquisar.pack(side=BOTTOM, fill=X, pady=1)

    def ocultar_pagina(self):
        self.__framePesquisar.pack_forget()

    def editar(self, frame, tv, tabela):
        try:

            rid = get_id(tv, tabela)
            if tabela == 'ocorrencias':
                values = search('processos', parms='processos.autor,processos.processo, processos.reu, '
                                                   'processos.tipo_acao, processos.adv_externo, '
                                                   'processos.uf_municipio, ocorrencias.*',
                                clause='inner join ocorrencias on ocorrencias.caso = processos.caso')[0]
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
