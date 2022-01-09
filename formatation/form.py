import locale

def format_curr(value):
    locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
    form = locale.currency(value, grouping=True)
    return form