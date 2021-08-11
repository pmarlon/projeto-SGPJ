from utils.modulos import *

from time import strftime
from datetime import datetime
from textblob import TextBlob


class Inicial:

    def __init__(self, master=None, app=None):
        img_wallpaper = ImageTk.PhotoImage(data=base64.b64decode(img_wallpaper_base64))  # Wallpaper
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

    def iniciar_pagina(self):
        self.ocultar_pagina()
        self.__frameInicial.pack(side=BOTTOM, fill=X, pady=1)

    def ocultar_pagina(self):
        self.__frameInicial.pack_forget()
