from datetime import datetime


def validar_int(entrada):
    if entrada.isdigit():
        return True
    else:
        return False


def validar_str(entrada):
    entrada = entrada.strip()
    if entrada.isalpha():
        return True
    elif ' ' in entrada:
        x = [x for x in entrada if x.isdigit() or not x.isalpha() and x != ' ']

        if not x:
            return True
        else:
            return False

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
        return False
    else:
        return True


def validar_vazio(entrada):
    if entrada == '':
        return False
    else:
        return True


def validar_data(entrada):
    try:
        datetime.strptime(entrada, '%d/%m/%Y')
        return True
    except ValueError:
        return False
