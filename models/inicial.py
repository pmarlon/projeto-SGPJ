from utils.modulos import *

from time import strftime
from datetime import datetime


class Inicial:

    def __init__(self, master=None, app=None):
        img_wallpaper = ImageTk.PhotoImage(data=base64.b64decode(img_wallpaper_base64))  # Wallpaper
        img_entrar = ImageTk.PhotoImage(data=base64.b64decode(img_entrar_base64))  # Imagem do botão Entrar
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
        self.__btnCadastro.place(relx=0.52, y=225)

        self.__lblMensagens = Label(self.__frameLogin, font='Serif 7 bold italic', fg='red', bg='light blue')
        self.__lblMensagens['text'] = 'Usuário e/ou senha inválidos.'
        self.__lblMensagens.place(relx=0.31, y=80)

    def command_entrar(self):
        self.__frameLogin.place_forget()

    def command_cadastro(self):
        pass

    def iniciar_pagina(self):
        self.ocultar_pagina()
        self.__frameInicial.pack(side=BOTTOM, fill=X, pady=1)

    def ocultar_pagina(self):
        self.__frameInicial.pack_forget()
