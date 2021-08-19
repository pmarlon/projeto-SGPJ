from utils.modulos import *


def criar_botao(frame, texto, imagem, comando, x, y, rw=0.1):
    Button(frame,
           text=texto,
           image=imagem,
           compound=TOP,
           relief='flat',
           bg='LightSteelBlue3', command=comando).place(x=x, y=y, relwidth=rw)
    return imagem


def linha_selecionada(tv, event):
    linha = tv.selection()
    valores = tv.item(linha)['values']
    return valores


def limpar(frame, tv=None):
    if tv:
        # Limpa todas as linhas do TreeView
        tv.delete(*tv.get_children())

    # Captura todos os elementos do Frame
    for child in frame.winfo_children():
        # Captura o nome da classe de cada elemento
        widget_class = child.__class__.__name__
        # Se a classe for Entry limpa o campo
        if widget_class == 'Entry':
            child['background'] = '#fff'
            child.delete(0, END)
        elif widget_class == 'Combobox':
            style = ttk.Style()
            style.theme_use('alt')
            style.configure("w.TCombobox", fieldbackground='#fff')
            child['style'] = 'w.TCombobox'
            child.delete(0, END)
        elif widget_class == 'Text':
            child['background'] = '#fff'
            child.delete(1.0, END)


def get_id(tv, tabela):
    if tabela == 'advogados':
        cpf = linha_selecionada(tv, '<<TreeviewSelect>>')[2]
        rid = search(tabela, parms='id', clause=f'where cpf="{cpf}"')[0][0]
        return rid
    elif tabela == 'processos':
        caso = linha_selecionada(tv, '<<TreeviewSelect>>')[0]
        rid = search(tabela, parms='id', clause=f'where caso="{caso}"')[0][0]
        return rid
    elif tabela == 'consultas':
        consulta = linha_selecionada(tv, '<<TreeviewSelect>>')[0]
        rid = search(tabela, parms='id', clause=f'where consulta="{consulta}"')[0][0]
        return rid
    elif tabela == 'ocorrencias':
        caso = linha_selecionada(tv, '<<TreeviewSelect>>')[0]
        data = linha_selecionada(tv, '<<TreeviewSelect>>')[1]
        desc = linha_selecionada(tv, '<<TreeviewSelect>>')[2]
        rid = search(tabela, parms='id', clause=f'where caso="{caso}" and data="{data}" and descricao="{desc}"')[0][0]
        return rid


def deletar(tv, tabela):

    try:

        rid = None

        if tabela == 'processos' or tabela == 'ocorrencias':
            caso = linha_selecionada(tv, '<<TreeviewSelect>>')[0]
            rid = search(tabela, parms='id', clause=f'where caso={caso}')[0][0]

        elif tabela == 'consultas':
            consulta = linha_selecionada(tv, '<<TreeviewSelect>>')[0]
            rid = search(tabela, parms='id', clause=f'where consulta={consulta}')[0][0]

        if messagebox.askyesno('Atenção', 'Deseja mesmo excluir o registro?'):
            delete(rid, tabela)
            messagebox.showinfo('Informação', 'Cadastro excluído com sucesso.')
            tv.delete(tv.selection())

    except IndexError:
        messagebox.showerror('Atenção', 'Você precisa selecionar um registro.')
    except TypeError:
        messagebox.showerror('Erro', 'Algo deu errado...')
    except OperationalError:
        messagebox.showerror('Erro', 'Algo deu errado...')


def auto_complete(entrada, tabela, campo, tv=None):
    if entrada:

        if tabela == 'advogados':
            advogados = search(tabela, clause=f"where {campo} like '%{entrada}%'")

            for advogado in advogados:

                tv.insert('', END, iid=None, values=(advogado[1], advogado[2], advogado[9],
                                                     advogado[8], f'{advogado[6]} / {advogado[5]}'))

    else:
        pass


def formata_data(data):
    mes = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Maço', 4: 'Abril', 5: 'Maio', 6: 'Junho',
           7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    dia_semana = {0: 'Segunda-feira', 1: 'Terça-feira', 2: 'Quarta-feira',
                  3: 'Quinta-feira', 4: 'Sexta-feira', 5: 'Sábado', 6: 'Domingo'}
    return f"{dia_semana[data.weekday()]}, {data.day} de {mes[data.month]} de {data.year}"


def checa_usuario(usuario):
    usuarios = search('cadastro', parms='usuario')
    for user in usuarios:
        if usuario == user[0]:
            return True
