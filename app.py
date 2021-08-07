from utils.modulos import *

from models.inicial import Inicial
from models.consultas import Consultas
from models.add_advogado import AddAdvogado
from models.ocorrencias import Ocorrencias
from models.processos import Processos
from models.pesquisar import Pesquisar


class App:

    def __init__(self, root=None):

        logo = ImageTk.PhotoImage(data=base64.b64decode(logo_completo_base64))
        img_inicial = PhotoImage(data=base64.b64decode(img_home_base64))  # imagem do botão Página Inicial
        img_ocorrencias = PhotoImage(data=base64.b64decode(img_ocorrencias_base64))  # imagem do botão Ocorrências
        img_processo = PhotoImage(data=base64.b64decode(img_processo_base64))  # imagem do botão Processos
        img_advogados = PhotoImage(data=base64.b64decode(img_advogados_base64))  # imagem do botão Escolher Advogado
        img_pesquisar = PhotoImage(data=base64.b64decode(img_pesquisar_base64))  # imagem do botão Pesquisar
        img_sair = PhotoImage(data=base64.b64decode(img_sair_base64))  # imagem do botão Sair
        img_consultas = PhotoImage(data=base64.b64decode(img_consultas_base64))  # imagem do botão Consultas

        self.root = root
        # Cabeçalho do Programa
        self.__Header = Frame(self.root, height=100, bg='#282a34')
        self.__Header.pack(side=TOP, fill=X)
        self.__lblLogo = Label(self.__Header, image=logo, bg='#282a34')
        self.__lblLogo.place(x=100, y=0)
        self.__lblLogo = logo

        # Menu com os botões das páginas do programa
        self.__MenuBar = Frame(self.root, height=80, bg='LightSteelBlue3', bd=2, relief='ridge')
        self.__MenuBar.pack(side=TOP, fill=X, pady=1)

        self.btnInicial = Button(self.__MenuBar,
                                 text='Página Inicial',
                                 image=img_inicial,
                                 compound=TOP,
                                 relief='flat',
                                 bg='LightSteelBlue3',
                                 activebackground='#4444ff')
        self.btnInicial.image = img_inicial
        self.btnInicial['command'] = lambda: self.switch_frame(self.frameInicial, self.btnInicial)
        self.btnInicial.place(x=10, y=3, relwidth=0.13)

        self.btnProcessos = Button(self.__MenuBar,
                                   text='Processos',
                                   image=img_processo,
                                   compound=TOP,
                                   relief='flat',
                                   bg='LightSteelBlue3',
                                   activebackground='#4444ff')
        self.btnProcessos.image = img_processo
        self.btnProcessos['command'] = lambda: self.switch_frame(self.frameProcessos, self.btnProcessos)
        self.btnProcessos.place(x=145, y=3, relwidth=0.13)

        self.btnOcorrencias = Button(self.__MenuBar,
                                     text='Ocorrências',
                                     compound=TOP,
                                     relief='flat',
                                     bg='LightSteelBlue3',
                                     activebackground='#4444ff')
        self.btnOcorrencias['image'] = img_ocorrencias
        self.btnOcorrencias.image = img_ocorrencias
        self.btnOcorrencias['command'] = lambda: self.switch_frame(self.frameOcorrencias, self.btnOcorrencias)
        self.btnOcorrencias.place(x=280, y=3, relwidth=0.13)

        self.btnAdvogados = Button(self.__MenuBar,
                                   text='Advogados',
                                   image=img_advogados,
                                   compound=TOP,
                                   relief='flat',
                                   bg='LightSteelBlue3',
                                   activebackground='#4444ff')
        self.btnAdvogados.image = img_advogados
        self.btnAdvogados['command'] = lambda: self.switch_frame(self.frameAdvogados, self.btnAdvogados)
        self.btnAdvogados.place(x=415, y=3, relwidth=0.13)

        self.btnConsultas = Button(self.__MenuBar,
                                   text='Consultas',
                                   image=img_consultas,
                                   compound=TOP,
                                   relief='flat',
                                   bg='LightSteelBlue3',
                                   activebackground='#4444ff')
        self.btnConsultas.image = img_consultas
        self.btnConsultas['command'] = lambda: self.switch_frame(self.frameConsultas, self.btnConsultas)
        self.btnConsultas.place(x=550, y=3, relwidth=0.13)

        self.btnPesquisar = Button(self.__MenuBar,
                                   text='Pesquisar',
                                   image=img_pesquisar,
                                   compound=TOP,
                                   relief='flat',
                                   bg='LightSteelBlue3',
                                   activebackground='#4444ff')
        self.btnPesquisar.image = img_pesquisar
        self.btnPesquisar['command'] = lambda: self.switch_frame(self.framePesquisar, self.btnPesquisar)
        self.btnPesquisar.place(x=685, y=3, relwidth=0.13)

        self.__btnSair = Button(self.__MenuBar,
                                text='Sair',
                                image=img_sair,
                                compound=TOP,
                                relief='flat',
                                bg='LightSteelBlue3',
                                activebackground='#4444ff')
        self.__btnSair.image = img_sair
        self.__btnSair['command'] = lambda: root.destroy()
        self.__btnSair.place(x=820, y=3, relwidth=0.13)

        # Frame inicial
        self.frameInicial = Inicial(self.root, self)
        self.frameInicial.iniciar_pagina()

        # Frame Processos
        self.frameProcessos = Processos(self.root, self)

        # Frame Ocorrências
        self.frameOcorrencias = Ocorrencias(self.root, self)

        # Frame Advogados
        self.frameAdvogados = AddAdvogado(self.root, self)

        # Frame Consultas
        self.frameConsultas = Consultas(self.root, self)

        # Frame Pesquisar
        self.framePesquisar = Pesquisar(self.root, self)

    def ocultar_paginas(self):
        self.frameInicial.ocultar_pagina()
        self.frameProcessos.ocultar_pagina()
        self.frameAdvogados.ocultar_pagina()
        self.frameConsultas.ocultar_pagina()
        self.framePesquisar.ocultar_pagina()
        self.frameOcorrencias.ocultar_pagina()

    def switch_frame(self, frame, btn=None):
        """Recebe um frame como parâmetro, oculta os frames ativos e inicia o frame recebido"""
        self.ocultar_paginas()
        frame.iniciar_pagina()
        self.switch_btn_color()
        if btn:
            btn['background'] = '#4444ff'

    def switch_btn_color(self):
        self.btnInicial['background'] = 'LightSteelBlue3'
        self.btnProcessos['background'] = 'LightSteelBlue3'
        self.btnOcorrencias['background'] = 'LightSteelBlue3'
        self.btnAdvogados['background'] = 'LightSteelBlue3'
        self.btnConsultas['background'] = 'LightSteelBlue3'
        self.btnPesquisar['background'] = 'LightSteelBlue3'


if __name__ == '__main__':
    root = Tk()
    App(root)
    root.title('SGPJ - Sistema para Gerenciamento de Processos Jurídicos')
    root.geometry('960x650+200+50')
    root.resizable(width=False, height=False)
    root['bg'] = 'LightSteelBlue3'
    root.mainloop()
