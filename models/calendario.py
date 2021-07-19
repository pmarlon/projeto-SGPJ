from utils.modulos import *

from tkcalendar import DateEntry


class Calendario:

    def __init__(self, frame):
        imgbtn5 = PhotoImage(file=f'{base_dir}/imagens/imgSelecionar.png')  # imagem do botão Selecionar Data
        imgbtn6 = PhotoImage(file=f'{base_dir}/imagens/imgCancelar.png')  # imagem do botão Cancelar
        data = localtime()
        win = Toplevel(frame)
        win.geometry('300x260+400+250')
        win['bg'] = 'LightSteelBlue3'
        win.resizable(width=False, height=False)
        cal = Calendar(win,
                       selectmode='day',
                       year=data[0],
                       month=data[1],
                       day=data[2],
                       firstweekday='sunday')
        cal.place(x=30, y=20)

        btn_selecionar_data = Button(win,
                                     text='Selecionar',
                                     image=imgbtn5,
                                     compound=LEFT,
                                     relief='flat')
        btn_selecionar_data['bg'] = 'LightSteelBlue3'
        btn_selecionar_data['command'] = lambda: print(command_selecionar())
        btn_selecionar_data.image = imgbtn5
        btn_selecionar_data.place(x=10, y=205)

        btn_cancelar = Button(win,
                              text='Cancelar',
                              image=imgbtn6,
                              compound=LEFT,
                              relief='flat')
        btn_cancelar['bg'] = 'LightSteelBlue3'
        btn_cancelar['command'] = lambda: command_cancelar()
        btn_cancelar.image = imgbtn6
        btn_cancelar.place(x=160, y=205)

        def command_selecionar():
            return cal.get_date()

        def command_cancelar():
            win.destroy()


class SelecionarData:
    def __init__(self, frame=None):
        cal = DateEntry(frame, width=12)
        cal.place(x=30, y=20)
