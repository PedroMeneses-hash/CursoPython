def aumentar(valor, taxa):
    s = valor + valor*taxa/100

    return s


def diminuir(valor, taxa):
    s = valor - valor*taxa/100

    return s


def dobro(valor):
    s = valor * 2

    return s


def metade(valor):
    s = valor / 2

    return s

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')
