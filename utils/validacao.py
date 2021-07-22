from datetime import datetime


def validar_int(entrada):
    if entrada.isdigit():
        return True
    else:
        return False


def validar_str(entrada):
    if entrada.isalpha():
        return True
    else:
        return False


def validar_float(entrada):
    try:
        float(entrada)
        return True
    except ValueError:
        return False


def validar_space(entrada):
    if entrada.isspace():
        return True
    else:
        return False


def validar_vazio(entrada):
    if entrada == '':
        return True
    else:
        return False


def validar_data(entrada):
    try:
        datetime.strptime(entrada, '%d/%m/%Y')
        return True
    except ValueError:
        return False
