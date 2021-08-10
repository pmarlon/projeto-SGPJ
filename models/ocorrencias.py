from utils.modulos import *


class Ocorrencias:

    def __init__(self, master=None, app=None):
        img_pesquisar = ImageTk.PhotoImage(data=base64.b64decode(img_pesquisar_menor_base64))
        img_salvar = PhotoImage(data=base64.b64decode(img_salvar_base64))  # imagem do botão Salvar Registro
        img_adicionar = PhotoImage(data=base64.b64decode(img_add_registro_base64))  # imagem do botão Add Registro
        img_cancelar = PhotoImage(data=base64.b64decode(img_cancelar_base64))  # imagem do botão Cancelar
        img_calendario = PhotoImage(data=base64.b64decode(img_calendario_base64))  # imagem do botão calendário

        self.app = app
        self.__frameOcorrencias = Frame(master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')

        self.__id = None

        self.__lblCaso = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblCaso['text'] = 'N° do Caso'
        self.__lblCaso['font'] = 'Serif', '12', 'bold'
        self.__lblCaso.place(x=100, y=20)

        self.__txtCaso = Entry(self.__frameOcorrencias)
        self.__txtCaso.place(relx=0.22, y=20, relwidth=0.09)

        self.__lblAutor = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblAutor['text'] = 'Autor'
        self.__lblAutor['font'] = 'Serif', '12', 'bold'
        self.__lblAutor.place(x=140, y=60)

        self.__txtAutor = Entry(self.__frameOcorrencias, state='readonly')
        self.__txtAutor.place(relx=0.22, y=60, relwidth=0.675)

        self.__lblReu = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblReu['text'] = 'Réu'
        self.__lblReu['font'] = 'Serif', '12', 'bold'
        self.__lblReu.place(x=160, y=90)

        self.__txtReu = Entry(self.__frameOcorrencias, state='readonly')
        self.__txtReu.place(relx=0.22, y=90, relwidth=0.675)

        self.__lblAdvExterno = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblAdvExterno['text'] = 'Adv Externo'
        self.__lblAdvExterno['font'] = 'Serif', '12', 'bold'
        self.__lblAdvExterno.place(x=90, y=120)

        self.__txtAdvExterno = Entry(self.__frameOcorrencias, state='readonly')
        self.__txtAdvExterno.place(relx=0.22, y=120, relwidth=0.675)

        self.__lblTipoAcao = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblTipoAcao['font'] = 'Serif', '12', 'bold'
        self.__lblTipoAcao['text'] = 'Tipo Ação'
        self.__lblTipoAcao.place(x=110, y=150)

        self.__txtTipoAcao = Entry(self.__frameOcorrencias, state='readonly')
        self.__txtTipoAcao.place(relx=0.22, y=150, relwidth=0.675)

        self.__lblProcessso = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblProcessso['text'] = 'Processo'
        self.__lblProcessso['font'] = 'Serif', '12', 'bold'
        self.__lblProcessso.place(x=120, y=180)

        self.__txtProcesso = Entry(self.__frameOcorrencias, state='readonly')
        self.__txtProcesso.place(relx=0.22, y=180, relwidth=0.675)

        self.__lblUfMunicipio = Label(self.__frameOcorrencias, bg='LightSteelBlue3')
        self.__lblUfMunicipio['text'] = 'UF - Município'
        self.__lblUfMunicipio['font'] = 'Serif', '12', 'bold'
        self.__lblUfMunicipio.place(x=60, y=210)

        self.__txtUfMunicipio = Entry(self.__frameOcorrencias, state='readonly')
        self.__txtUfMunicipio.place(relx=0.22, y=210, relwidth=0.675)

        self.__lblDataOcorrencia = Label(self.__frameOcorrencias, text='Data', bg='LightSteelBlue3')
        self.__lblDataOcorrencia['font'] = 'Serif', '12'
        self.__lblDataOcorrencia.place(x=160, y=240)

        self.__txtDataOcorrencia = Entry(self.__frameOcorrencias)
        self.__txtDataOcorrencia.place(relx=0.22, y=240, relwidth=0.09)

        self.__lblDescricao = Label(self.__frameOcorrencias, text='Descrição', bg='LightSteelBlue3')
        self.__lblDescricao['font'] = 'Serif', '12'
        self.__lblDescricao.place(x=110, y=285)

        self.__txtDescricao = Text(self.__frameOcorrencias, height=3)
        self.__txtDescricao.place(relx=0.22, y=270, relwidth=0.5)

        self.__lblValor = Label(self.__frameOcorrencias, text='Valor R$', bg='LightSteelBlue3')
        self.__lblValor['font'] = 'Serif', '12'
        self.__lblValor.place(x=130, y=335)

        self.__txtValor = Entry(self.__frameOcorrencias, width=20)
        self.__txtValor.place(relx=0.22, y=335, relwidth=0.15)

        self.__lblValorAtual = Label(self.__frameOcorrencias, text='Valor Atual R$', bg='LightSteelBlue3')
        self.__lblValorAtual['font'] = 'Serif', '12'
        self.__lblValorAtual.place(relx=0.425, y=335, relwidth=0.15)

        self.__txtValorAtual = Entry(self.__frameOcorrencias, width=20)
        self.__txtValorAtual.place(relx=0.57, y=335, relwidth=0.15)

        self.__btnAddOcorrencia = Button(self.__frameOcorrencias,
                                         text='Adicionar Ocorrência',
                                         compound=TOP,
                                         relief='flat',
                                         bg='LightSteelBlue3')
        self.__btnAddOcorrencia['image'] = img_adicionar
        self.__btnAddOcorrencia.image = img_adicionar
        self.__btnAddOcorrencia['command'] = lambda: self.insert_ocorrencia()

        self.__btnSalvar = Button(self.__frameOcorrencias,
                                  text='Salvar Ocorrência',
                                  compound=TOP,
                                  relief='flat',
                                  bg='LightSteelBlue3')
        self.__btnSalvar['image'] = img_salvar
        self.__btnSalvar.image = img_salvar
        self.__btnSalvar['command'] = lambda: self.update_ocorrencia()

        self.__btnPesquisar = Button(self.__frameOcorrencias,
                                     image=img_pesquisar,
                                     compound=TOP,
                                     relief='flat',
                                     bg='LightSteelBlue3',
                                     highlightthickness=False)
        self.__btnPesquisar.image = img_pesquisar
        self.__btnPesquisar['command'] = lambda: self.pesquisar()
        self.__btnPesquisar.place(relx=0.31, y=15)

        self.__btnCancelar = Button(self.__frameOcorrencias,
                                    image=img_cancelar,
                                    text='Cancelar',
                                    compound=TOP,
                                    relief='flat',
                                    bg='LightSteelBlue3')
        self.__btnCancelar.image = img_cancelar
        self.__btnCancelar['command'] = lambda: self.iniciar_pagina()

        self.__btnCalendario = Button(self.__frameOcorrencias,
                                      image=img_calendario,
                                      relief='flat',
                                      bg='LightSteelBlue3',
                                      highlightthickness=0
                                      )
        self.__btnCalendario.image = img_calendario
        self.__btnCalendario['command'] = lambda: Calendario(self.__frameOcorrencias,
                                                             self.__txtDataOcorrencia,
                                                             relx=self.__txtDataOcorrencia.winfo_rootx(),
                                                             rely=self.__txtDataOcorrencia.winfo_rooty())
        self.__btnCalendario.place(relx=0.31, rely=0.51)

    @property
    def caso(self):
        return self.__txtCaso.get()

    @caso.setter
    def caso(self, valor):
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
            self.validar()
        except ValueError:
            messagebox.showwarning('Atenção', 'Verifique os campos marcados em vermelho e tente novamente.')
        else:
            try:
                insert('ocorrencias', self.caso, self.data_ocorrencia, self.descricao, self.valor, self.vr_atual)
                messagebox.showinfo('Informação', 'Ocorrência adicionada com sucesso.')
                self.iniciar_pagina()
            except OperationalError:
                messagebox.showerror('Atenção', 'Ocorreu um erro...')

    def update_ocorrencia(self):
        try:
            self.validar()
        except ValueError:
            messagebox.showwarning('Atenção', 'Verifique os campos marcados em vermelho e tente novamente.')
        else:
            rid = self.__id
            update(rid, 'ocorrencias',
                   data=self.data_ocorrencia,
                   descricao=self.descricao,
                   valor=self.valor,
                   vr_atual=self.vr_atual)

            messagebox.showinfo('Informação', 'Registro alterado com Sucesso!')
            self.iniciar_pagina()

    def pesquisar(self):
        try:
            caso = self.caso
            values = search('processos', parms='caso, autor, reu, adv_externo, tipo_acao, processo, uf_municipio',
                            clause=f'where caso={caso}')[0]
            self.preencher(values, True)
            self.__btnAddOcorrencia.place_forget()
            self.__btnAddOcorrencia.place(x=250, y=370, relwidth=0.15)
            self.__btnCancelar.place(x=400, y=370, relwidth=0.15)

        except IndexError:
            messagebox.showwarning('Atenção', 'Nenhum registro encontrado.')
        except OperationalError:
            messagebox.showerror('Erro', 'Digite o número do caso que deseja consultar.')

    def preencher(self, values=None, alt=None):

        self.status_normal()
        limpar(self.__frameOcorrencias)
        if values and alt:
            self.caso = values[0]
            self.autor = values[1]
            self.reu = values[2]
            self.adv_externo = values[3]
            self.tipo_acao = values[4]
            self.num_processo = values[5]
            self.uf_municipio = values[6]

        elif values:
            self.__id = values[6]
            self.caso = values[7]
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
        self.status_readonly()

    def iniciar_pagina(self):
        self.status_normal()
        limpar(self.__frameOcorrencias)
        self.__frameOcorrencias.pack(side=BOTTOM, fill=X, pady=1)
        self.__btnAddOcorrencia.place(x=350, y=370, relwidth=0.15)
        self.__btnCancelar.place_forget()
        self.__btnSalvar.place_forget()
        self.status_readonly()
        self.__txtCaso['state'] = 'normal'
        self.__btnPesquisar['state'] = 'normal'

    def ocultar_pagina(self):
        self.__frameOcorrencias.pack_forget()

    def trocar_botoes(self):
        if not self.__btnSalvar.place_info():
            self.__btnAddOcorrencia.place_forget()
            self.__btnCancelar.place(x=500, y=390, relwidth=0.15)
            self.__btnSalvar.place(x=350, y=390)

    def status_normal(self):

        self.__txtCaso['state'] = 'normal'
        self.__txtAutor['state'] = 'normal'
        self.__txtProcesso['state'] = 'normal'
        self.__txtReu['state'] = 'normal'
        self.__txtTipoAcao['state'] = 'normal'
        self.__txtAdvExterno['state'] = 'normal'
        self.__txtUfMunicipio['state'] = 'normal'

    def status_readonly(self):
        self.__btnPesquisar['state'] = 'disabled'
        self.__txtCaso['state'] = 'readonly'
        self.__txtAutor['state'] = 'readonly'
        self.__txtProcesso['state'] = 'readonly'
        self.__txtReu['state'] = 'readonly'
        self.__txtTipoAcao['state'] = 'readonly'
        self.__txtAdvExterno['state'] = 'readonly'
        self.__txtUfMunicipio['state'] = 'readonly'

    def validar(self):
        valid = []
        for child in self.__frameOcorrencias.winfo_children():
            child_class = child.__class__.__name__

            if child_class == 'Entry':
                if validar_vazio(child.get()) and validar_space(child.get()):
                    child['background'] = '#fff'
                    valid.append(True)
                else:
                    child['background'] = 'Indian Red'
                    valid.append(False)
            elif child_class == 'Text':
                if validar_vazio(child.get(1.0, END)) and validar_space(child.get(1.0, END)):
                    child['background'] = '#fff'
                    valid.append(True)
                else:
                    child['background'] = 'Indian Red'
                    valid.append(False)
        if (validar_data(self.data_ocorrencia)) and (validar_float(self.valor)) and (validar_float(self.vr_atual)):
            valid.append(True)
        else:
            if not validar_data(self.data_ocorrencia):
                self.__txtDataOcorrencia['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtDataOcorrencia['background'] = '#fff'
                valid.append(True)

            if not validar_float(self.valor):
                self.__txtValor['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtValor['background'] = '#fff'
                valid.append(True)
            if not validar_float(self.vr_atual):
                self.__txtValorAtual['background'] = 'Indian Red'
                valid.append(False)
            else:
                self.__txtValorAtual['background'] = '#fff'
                valid.append(True)

        if False not in valid:
            return True
        else:
            raise ValueError
