from SGPJ.utils.modulos import *


class Principal:

    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.__framePrincipal = Frame(self.master, height=500, bg='LightSteelBlue3', bd=2, relief='ridge')

    def iniciar_pagina(self):
        self.ocultar_pagina()
        self.__framePrincipal.pack(side=BOTTOM, fill=X, pady=1)

    def ocultar_pagina(self):
        self.__framePrincipal.pack_forget()
