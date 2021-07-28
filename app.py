from utils.modulos import *


class App:

    def __init__(self, root=None):
        logo = ImageTk.PhotoImage(Image.open('imagens/logo.png').resize((80, 80), Image.ANTIALIAS))
        img_principal = PhotoImage(file='imagens/imgHome.png')  # imagem do botão Página Principal
        img_ocorrencias = PhotoImage(file='imagens/imgObservar.png')  # imagem do botão Ocorrências
        img_processo = PhotoImage(file='imagens/imgProcessos.png')  # imagem do botão Processos
        img_advogados = PhotoImage(file='imagens/imgAdvogados.png')  # imagem do botão Escolher Advogado
        img_pesquisar = PhotoImage(file='imagens/imgPesquisar.png')  # imagem do botão Pesquisar
        img_sair = PhotoImage(file='imagens/imgSair.png')  # imagem do botão Sair
        img_consultas = PhotoImage(file='imagens/imgConsultas.png')  # imagem do botão Consultas

        self.root = root

        # Cabeçalho do Programa
        self.__Header = Frame(self.root, height=100, bg='#282a34')
        self.__Header.pack(side=TOP, fill=X)
        self.__lblTitulo = Label(self.__Header, text='SGPJ - Advogados Associados', bg='#282a34')
        self.__lblTitulo['font'] = 'Serif', '24', 'bold'
        self.__lblTitulo['fg'] = '#64b6fa'
        self.__lblTitulo.place(x=200, y=30)
        self.__lblTitulo.place(x=200, y=30)
        self.__lblLogo = Label(self.__Header, image=logo, bg='#282a34')
        self.__lblLogo.place(x=100, y=0)
        self.__lblLogo = Label(self.__Header, image=logo, bg='#282a34')
        self.__lblLogo.place(x=750, y=0)
        self.__lblLogo.logo = logo

        # Menu com os botões das páginas do programa
        self.__MenuBar = Frame(self.root, height=80, bg='LightSteelBlue3', bd=2, relief='ridge')
        self.__MenuBar.pack(side=TOP, fill=X, pady=1)

        self.__btnPrincipal = Button(self.__MenuBar,
                                     text='Página Principal',
                                     image=img_principal,
                                     compound=TOP,
                                     relief='flat',
                                     bg='LightSteelBlue3')
        self.__btnPrincipal.image = img_principal
        self.__btnPrincipal['command'] = lambda: self.switch_frame(self.framePrincipal)
        self.__btnPrincipal.place(x=10, y=3, relwidth=0.13)

        self.__btnProcessos = Button(self.__MenuBar,
                                     text='Processos',
                                     image=img_processo,
                                     compound=TOP,
                                     relief='flat',
                                     bg='LightSteelBlue3')
        self.__btnProcessos.image = img_processo
        self.__btnProcessos['command'] = lambda: self.switch_frame(self.frameProcessos)
        self.__btnProcessos.place(x=145, y=3, relwidth=0.13)

        self.__btnOcorrencias = Button(self.__MenuBar,
                                       text='Ocorrências',
                                       compound=TOP,
                                       relief='flat',
                                       bg='LightSteelBlue3')
        self.__btnOcorrencias['image'] = img_ocorrencias
        self.__btnOcorrencias.image = img_ocorrencias
        self.__btnOcorrencias['command'] = lambda: self.switch_frame(self.frameOcorrencias)
        self.__btnOcorrencias.place(x=280, y=3, relwidth=0.13)

        self.__btnAdvogados = Button(self.__MenuBar,
                                     text='Advogados',
                                     image=img_advogados,
                                     compound=TOP,
                                     relief='flat',
                                     bg='LightSteelBlue3')
        self.__btnAdvogados.image = img_advogados
        self.__btnAdvogados['command'] = lambda: self.switch_frame(self.frameAdvogados)
        self.__btnAdvogados.place(x=415, y=3, relwidth=0.13)

        self.__btnConsultas = Button(self.__MenuBar,
                                     text='Consultas',
                                     image=img_consultas,
                                     compound=TOP,
                                     relief='flat',
                                     bg='LightSteelBlue3')
        self.__btnConsultas.image = img_consultas
        self.__btnConsultas['command'] = lambda: self.switch_frame(self.frameConsultas)
        self.__btnConsultas.place(x=550, y=3, relwidth=0.13)

        self.__btnPesquisar = Button(self.__MenuBar,
                                     text='Pesquisar',
                                     image=img_pesquisar,
                                     compound=TOP,
                                     relief='flat',
                                     bg='LightSteelBlue3')
        self.__btnPesquisar.image = img_pesquisar
        self.__btnPesquisar['command'] = lambda: self.switch_frame(self.framePesquisar)
        self.__btnPesquisar.place(x=685, y=3, relwidth=0.13)

        self.__btnSair = Button(self.__MenuBar,
                                text='Sair',
                                image=img_sair,
                                compound=TOP,
                                relief='flat',
                                bg='LightSteelBlue3')
        self.__btnSair.image = img_sair
        self.__btnSair['command'] = lambda: root.destroy()
        self.__btnSair.place(x=820, y=3, relwidth=0.13)

        # Frame principal
        self.framePrincipal = Principal(self.root, self)
        self.framePrincipal.iniciar_pagina()

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
        self.framePrincipal.ocultar_pagina()
        self.frameProcessos.ocultar_pagina()
        self.frameAdvogados.ocultar_pagina()
        self.frameConsultas.ocultar_pagina()
        self.framePesquisar.ocultar_pagina()
        self.frameOcorrencias.ocultar_pagina()

    def switch_frame(self, frame):
        """Recebe um frame como parâmetro, oculta os frames ativos e inicia o frame recebido"""
        self.ocultar_paginas()
        frame.iniciar_pagina()


if __name__ == '__main__':
    root = Tk()
    App(root)
    root.title('SGPJ - Sistema para Gerenciamento de Processos Jurídicos')
    root.geometry('960x650+200+50')
    root['bg'] = 'LightSteelBlue3'
    root.resizable(width=False, height=False)
    root.mainloop()
