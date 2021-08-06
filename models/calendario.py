from tkcalendar import Calendar

from time import localtime
from utils.modulos import *


class Calendario:

    def __init__(self, frame, campo=None):
        img_selecionar = PhotoImage(data=base64.b64decode(img_selecionar_base64))  # imagem do botão Selecionar Data
        img_cancelar = PhotoImage(data=base64.b64decode(img_cancelar_base64))  # imagem do botão Cancelar
        data = localtime()
        relx, rely = preencher_data(frame, None, campo)
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
            preencher_data(frame, data_selecionada, campo)
            win.destroy()

        def command_cancelar():
            win.destroy()


def preencher_data(frame, data, campo):
    """
    Função que preenche um campo de data de acordo com os parâmetros recebidos
    :param frame: frame onde o campo de data se encontra
    :param data: data recebida direto da class Calendário
    :param campo: nome do campo data, usado para encontrar o campo correto no frame
    :return: retorna a posição do campo no frame, usado para posicionar o Toplevel do Calendário
    """
    for child in frame.winfo_children():
        child_class = child.__class__.__name__
        if child_class == 'Entry':
            if child.winfo_name() == campo:
                if not data:
                    return child.winfo_rootx(), child.winfo_rooty()
                else:
                    child.delete(0, END)
                    child.insert(END, data)
