from utils.modulos import *

from time import strftime
from datetime import datetime
from passlib.hash import pbkdf2_sha256 as cryp


class Inicial:

    def __init__(self, master=None, app=None):
        img_wallpaper = ImageTk.PhotoImage(data=base64.b64decode(img_wallpaper_base64))  # Wallpaper
        img_entrar = ImageTk.PhotoImage(data=base64.b64decode(img_entrar_base64))  # Imagem do botão Entrar
        img_cadastrar = ImageTk.PhotoImage(data=base64.b64decode(img_cadastrar_base64))  # Imagem do botão Cadastrar
        img_cancelar_cadastro = ImageTk.PhotoImage(data=base64.b64decode(img_cancelar_cadastro_base64))
        img_logout = ImageTk.PhotoImage(data=base64.b64decode(img_logout_base64))

        self.master = master
        self.app = app

        self.__login = False

        self.__frameInicial = Frame(self.master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')

        self.__lblWallpaper = Label(self.__frameInicial, image=img_wallpaper, bg='LightSteelBlue3')

        hoje = datetime.today()

        def tic():

            self.__lblWallpaper['text'] = strftime(f'{formata_data(hoje)} %H:%M:%S\n')
            self.__lblWallpaper['compound'] = 'top'
            self.__lblWallpaper['fg'] = '#1e1d20'

        def tac():
            tic()
            self.__lblWallpaper.after(1000, tac)

        self.__lblWallpaper['font'] = 'Serif 14 bold'
        self.__lblWallpaper.place(x=0, y=0, relwidth=1, relheight=1)
        tac()
        self.__lblWallpaper.image = img_wallpaper

        self.__lblBoasVindas = Label(self.__frameInicial, font='Serif 14 bold', bg='LightSteelBlue3', fg='#1d1e20')
        self.__lblBoasVindas['text'] = ''
        self.__lblBoasVindas.place(x=20, y=10)

        self.__btnLogout = Button(self.__frameInicial,
                                  image=img_logout,
                                  padx=0,
                                  pady=0,
                                  bg='LightSteelBlue3',
                                  relief='flat',
                                  highlightthickness=0)
        self.__btnLogout['command'] = lambda: self.command_logout()
        self.__btnLogout.image = img_logout

        self.__frameLogin = Frame(self.__frameInicial, bg='light blue')
        self.__frameLogin.place(width=300, height=300, relx=0.3855, y=50)

        self.__lblLogin = Label(self.__frameLogin, text='Login', font='Serif 18 bold', bg='light blue')
        self.__lblLogin.place(relx=0.38, y=20)

        self.__lblUsuario = Label(self.__frameLogin, text='Usuário', font='Serif 12 italic', bg='light blue')
        self.__lblUsuario.place(relx=0.075, y=100)

        self.__txtUsuario = Entry(self.__frameLogin, highlightthickness=0)
        self.__txtUsuario.place(relx=0.31, y=100, relwidth=0.5)

        self.__lblSenha = Label(self.__frameLogin, text='Senha', font='Serif 12 italic', bg='light blue')
        self.__lblSenha.place(relx=0.12, y=140)

        self.__txtSenha = Entry(self.__frameLogin, show='*', highlightthickness=0)
        self.__txtSenha.place(relx=0.31, y=140, relwidth=0.5)

        self.__btnEntrar = Button(self.__frameLogin,
                                  image=img_entrar,
                                  relief='flat',
                                  padx=0,
                                  pady=0,
                                  bg='light blue',
                                  highlightthickness=0)
        self.__btnEntrar['command'] = lambda: self.command_entrar()
        self.__btnEntrar.image = img_entrar
        self.__btnEntrar.place(relx=0.4, y=175)

        self.__lblCadastro = Label(self.__frameLogin,
                                   text='Ainda não tem cadastro?',
                                   font='Serif 8 italic',
                                   bg='light blue')
        self.__lblCadastro.place(relx=0.075, y=230)

        self.__btnCadastro = Button(self.__frameLogin, text='Cadastre-se',
                                    font='Serif 10',
                                    fg='purple',
                                    relief='flat',
                                    padx=0,
                                    pady=0,
                                    bg='light blue',
                                    highlightthickness=0)
        self.__btnCadastro['command'] = lambda: self.command_cadastro()
        self.__btnCadastro.place(relx=0.52, y=225)

        self.__lblMensagens = Label(self.__frameLogin, font='Serif 7 bold italic', fg='red', bg='light blue')
        self.__lblMensagens.place(relx=0.31, y=80)

        self.__frameCadastro = Frame(self.__frameInicial, bg='light blue')

        self.__lblCadastro = Label(self.__frameCadastro, text='Cadastro', font='Serif 18 bold', bg='light blue')
        self.__lblCadastro.place(relx=0.38, y=20)

        self.__lblDicaUsuario = Label(self.__frameCadastro, font='Serif 7 bold italic', fg='red', bg='light blue')
        self.__lblDicaUsuario.place(relx=0.4, y=85)

        self.__lblNovoUsuario = Label(self.__frameCadastro, text='Usuário', bg='light blue', font='Serif 10 italic')
        self.__lblNovoUsuario.place(relx=0.22, y=100)

        self.__txtNovoUsuario = Entry(self.__frameCadastro, highlightthickness=0)
        self.__txtNovoUsuario.place(relx=0.4, y=100, relwidth=0.5)

        self.__lblDicaSenha = Label(self.__frameCadastro, font='Serif 7 bold italic', fg='red', bg='light blue')
        self.__lblDicaSenha.place(relx=0.4, y=125)

        self.__lblNovaSenha = Label(self.__frameCadastro, text='Senha', font='Serif 10 italic', bg='light blue')
        self.__lblNovaSenha.place(relx=0.25, y=140)

        self.__txtNovaSenha = Entry(self.__frameCadastro, show='*', highlightthickness=0)
        self.__txtNovaSenha.place(relx=0.4, y=140, relwidth=0.5)

        self.__lblDicaConfirmaSenha = Label(self.__frameCadastro, font='Serif 7 bold italic', fg='red', bg='light blue')
        self.__lblDicaConfirmaSenha.place(relx=0.4, y=165)

        self.__lblConfirmaSenha = Label(self.__frameCadastro, text='Confirmar Senha',
                                        font='Serif 10 italic',
                                        bg='light blue')
        self.__lblConfirmaSenha.place(relx=0.04, y=180)

        self.__txtConfirmaSenha = Entry(self.__frameCadastro, show='*', highlightthickness=0)
        self.__txtConfirmaSenha.place(relx=0.4, y=180, relwidth=0.5)

        self.__btnCadastrar = Button(self.__frameCadastro,
                                     image=img_cadastrar,
                                     relief='flat',
                                     padx=0,
                                     pady=0,
                                     bg='light blue',
                                     highlightthickness=0)
        self.__btnCadastrar['command'] = lambda: self.command_cadastrar()
        self.__btnCadastrar.image = img_cadastrar
        self.__btnCadastrar.place(relx=0.38, y=220)

        self.__btnCancelar = Button(self.__frameCadastro,
                                    image=img_cancelar_cadastro,
                                    relief='flat',
                                    padx=0,
                                    pady=0,
                                    bg='light blue',
                                    highlightthickness=0)
        self.__btnCancelar['command'] = lambda: self.command_cancelar()
        self.__btnCancelar.image = img_cancelar_cadastro
        self.__btnCancelar.place(relx=0.65, y=220)

    @property
    def usuario(self):
        return self.__txtUsuario.get().lower()

    @property
    def novo_usuario(self):
        return self.__txtNovoUsuario.get()

    def command_entrar(self):
        if (validar_vazio(self.usuario)) and (validar_space(self.usuario)):

            if checa_usuario(self.usuario):
                senha = search('cadastro', parms='senha', clause=f'where usuario="{self.usuario}"')[0][0]

                if (validar_vazio(self.__txtSenha.get())) and (validar_space(self.usuario)):

                    if self.checa_senha(senha):
                        self.__lblMensagens['text'] = ''
                        self.__login = True
                        self.__lblBoasVindas['text'] = f'Seja Bem-vindo(a) {self.usuario.title()}'
                        self.__btnLogout.place(relx=0.9, y=10)
                        print('logado')
                    else:
                        self.__lblMensagens['text'] = 'Senha incorreta'
                else:
                    self.__lblMensagens['text'] = 'Digite a senha'
            else:
                self.__lblMensagens['text'] = 'Usuário não encontrado'
        else:
            self.__lblMensagens['text'] = 'Digite um nome de usuário'

    def command_cadastro(self):
        self.__frameLogin.place_forget()
        limpar(self.__frameLogin)
        limpar(self.__frameCadastro)
        self.__lblDicaUsuario['text'] = ''
        self.__lblDicaConfirmaSenha['text'] = ''
        self.__lblDicaSenha['text'] = ''
        self.__frameCadastro.place(width=350, height=300, relx=0.38, y=50)

    def command_cadastrar(self):

        if self.validar():
            senha = cryp.hash(self.__txtNovaSenha.get(), rounds=200000, salt_size=16)
            insert('cadastro', self.novo_usuario, senha)
            messagebox.showinfo('Informação', 'Usuário Cadastrado com sucesso.')
            self.iniciar_pagina()

    def command_cancelar(self):
        self.iniciar_pagina()

    def command_logout(self):

        if messagebox.askyesno('Atenção', 'Deseja mesmo Sair?'):
            self.__login = False
            self.iniciar_pagina()

    def checa_senha(self, senha):
        if cryp.verify(self.__txtSenha.get(), senha):
            return True
        return False

    def validar(self):
        valid = []

        if validar_vazio(self.__txtNovoUsuario.get()) and validar_space(self.__txtNovoUsuario.get()):

            if checa_usuario(self.novo_usuario):
                self.__txtNovoUsuario['background'] = 'Indian red'
                self.__lblDicaUsuario['text'] = 'Este usuário já existe'
                valid.append(False)
            else:

                if not validar_usuario(self.novo_usuario):
                    self.__txtNovoUsuario['background'] = 'Indian Red'
                    self.__lblDicaUsuario['text'] = 'Símbolos não são permitidos'
                    valid.append(False)
                else:
                    self.__txtNovoUsuario['background'] = '#fff'
                    self.__lblDicaUsuario['text'] = ''
                    valid.append(True)
        else:
            self.__txtNovoUsuario['background'] = 'Indian Red'
            self.__lblDicaUsuario['text'] = 'Digite um nome de usuário válido'
            valid.append(False)

        if validar_vazio(self.__txtNovaSenha.get()) and validar_space(self.__txtNovaSenha.get()):

            if not validar_senha(self.__txtNovaSenha.get()):
                self.__txtNovaSenha['background'] = 'Indian Red'
                self.__lblDicaSenha['text'] = 'Mínimo 8 caracteres para senha'
                valid.append(False)
            else:
                self.__lblDicaSenha['text'] = ''
                self.__txtNovaSenha['background'] = '#fff'
                if validar_vazio(self.__txtConfirmaSenha.get()) and validar_space(self.__txtConfirmaSenha.get()):

                    if self.__txtNovaSenha.get() == self.__txtConfirmaSenha.get():
                        self.__lblDicaConfirmaSenha['text'] = ''
                        self.__txtConfirmaSenha['background'] = '#fff'
                        valid.append(True)
                    else:
                        self.__txtConfirmaSenha['background'] = 'Indian Red'
                        self.__lblDicaConfirmaSenha['text'] = 'As senhas não conferem'
                        valid.append(False)

                else:
                    self.__txtConfirmaSenha['background'] = 'Indian Red'
                    self.__lblDicaConfirmaSenha['text'] = 'Você precisa confirmar a senha'
                    valid.append(False)

        else:
            self.__txtNovaSenha['background'] = 'Indian Red'
            self.__lblDicaSenha['text'] = 'Digite uma senha válida'
            valid.append(False)

        if False not in valid:
            return True
        else:
            return False

    def iniciar_pagina(self):
        self.ocultar_pagina()
        limpar(self.__frameLogin)
        limpar(self.__frameCadastro)
        self.__lblMensagens['text'] = ''
        self.__frameInicial.pack(side=BOTTOM, fill=X, pady=1)

        if not self.__login:
            self.__frameLogin.place(width=300, height=300, relx=0.3855, y=50)
            self.__btnLogout.place_forget()
            self.__lblBoasVindas['text'] = ''

    def ocultar_pagina(self):
        self.__frameLogin.place_forget()
        self.__frameCadastro.place_forget()
        self.__frameInicial.pack_forget()
