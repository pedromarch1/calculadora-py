import locale

def formata_dinheiro(valor):
    locale.setlocale(locale.LC_MONETARY, 'pt_BR')
    form = locale.currency(valor, grouping=True)
    return form


