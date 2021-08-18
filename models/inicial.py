from utils.modulos import *

from time import strftime
from datetime import datetime


class Inicial:

    def __init__(self, master=None, app=None):
        img_wallpaper = ImageTk.PhotoImage(data=base64.b64decode(img_wallpaper_base64))  # Wallpaper
        img_entrar = ImageTk.PhotoImage(data=base64.b64decode(img_entrar_base64))  # Imagem do botão Entrar
        img_cadastrar = ImageTk.PhotoImage(data=base64.b64decode(img_cadastrar_base64))  # Imagem do botão Cadastrar
        img_cancelar_cadastro = ImageTk.PhotoImage(data=base64.b64decode(img_cancelar_cadastro_base64))  # Imagem do botão Cancelar
        self.master = master
        self.app = app
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
        self.__lblMensagens['text'] = 'Usuário e/ou senha inválidos.'
        self.__lblMensagens.place(relx=0.31, y=80)

        self.__frameCadastro = Frame(self.__frameInicial, bg='light blue')

        self.__lblCadastro = Label(self.__frameCadastro, text='Cadastro', font='Serif 18 bold', bg='light blue')
        self.__lblCadastro.place(relx=0.38, y=20)

        self.__lblNovoUsuario = Label(self.__frameCadastro, text='Usuário', bg='light blue', font='Serif 10 italic')
        self.__lblNovoUsuario.place(relx=0.22, y=100)

        self.txtNovoUsuario = Entry(self.__frameCadastro, highlightthickness=0)
        self.txtNovoUsuario.place(relx=0.4, y=100, relwidth=0.5)

        self.__lblNovaSenha = Label(self.__frameCadastro, text='Senha', font='Serif 10 italic', bg='light blue')
        self.__lblNovaSenha.place(relx=0.25, y=140)

        self.__txtNovaSenha = Entry(self.__frameCadastro, show='*', highlightthickness=0)
        self.__txtNovaSenha.place(relx=0.4, y=140, relwidth=0.5)

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
        self.__btnCadastrar['command'] = ''
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

    def command_entrar(self):
        self.__frameLogin.place_forget()

    def command_cadastro(self):
        self.__frameLogin.place_forget()
        self.__frameCadastro.place(width=350, height=300, relx=0.38, y=50)

    def command_cancelar(self):
        self.__frameCadastro.place_forget()
        self.__frameLogin.place(width=300, height=300, relx=0.3855, y=50)

    def iniciar_pagina(self):
        self.ocultar_pagina()
        self.__frameInicial.pack(side=BOTTOM, fill=X, pady=1)

    def ocultar_pagina(self):
        self.__frameInicial.pack_forget()
