from tkcalendar import Calendar

from time import localtime
from utils.modulos import *

data = localtime()


class Calendario:

    def __init__(self, frame, campo=None, *, relx=0, rely=0):
        img_selecionar = PhotoImage(data=base64.b64decode(img_selecionar_base64))  # imagem do botão Selecionar Data
        img_cancelar = PhotoImage(data=base64.b64decode(img_cancelar_base64))  # imagem do botão Cancelar
        win = Toplevel(frame)
        win.geometry(f'300x260+{relx}+{rely-300}')
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
                                     image=img_selecionar,
                                     compound=LEFT,
                                     relief='flat')
        btn_selecionar_data['bg'] = 'LightSteelBlue3'
        btn_selecionar_data['command'] = lambda: command_selecionar()
        btn_selecionar_data.image = img_selecionar
        btn_selecionar_data.place(x=10, y=205)

        btn_cancelar = Button(win,
                              text='Cancelar',
                              image=img_cancelar,
                              compound=LEFT,
                              relief='flat')
        btn_cancelar['bg'] = 'LightSteelBlue3'
        btn_cancelar['command'] = lambda: command_cancelar()
        btn_cancelar.image = img_cancelar
        btn_cancelar.place(x=160, y=205)

        def command_selecionar():
            data_selecionada = cal.get_date()
            campo.delete(0, END)
            campo.insert(END, data_selecionada)
            win.destroy()

        def command_cancelar():
            win.destroy()
