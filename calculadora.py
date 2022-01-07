import math

st = input('Selecione o modo da calculadora: (C) Científica, (P) Padrão, (A) Área ou (J) Juros: ')

if(st.upper() == 'P'):

    print('Calculadora Padrão\n----------------------------------------------------')

    a = eval(input('Insira uma conta (insira apenas operadores básicos): '))
    print(float(a))

elif(st.upper() == 'C'):

    def calc(n1, op, n2):
        if(op == '**'):
            r = math.pow(n1, n2)
            return r

        elif(op == 'sqrt'):
            r = n1 * math.sqrt(n2)
            return r
        
        elif(op == '%'):
            r = n1 * n2 / 100
            return r
        
        elif(op == 'sin' or op == 'sen' or op == 'seno'):
            r = n1 * math.sin(n2)
            return r
        
        elif(op == 'cos' or op == 'cossen' or op == 'cosseno'):
            r = n1 * math.cos(n2)
            return r
        
        elif(op == 'tan' or op == 'tg' or op == 'tangente'):
            r = n1 * math.tan(n2)
            return r
        
        elif(op == 'asin' or op == 'asen' or op == 'arcosseno'):
            r = n1 * math.asin(n2)
            return r
        
        elif(op == 'acos' or op == 'acossen' or op == 'arco cosseno'):
            r = n1 * math.acos(n2)
            return r
        
        elif(op == 'atan' or op == 'atg' or op == 'arco tangente'):
            r = n1 * math.atan(n2)
            return r

    print('Calculadora Científica\n----------------------------------------------------')

    n1 = float(input('Insira um numero: '))
    op = input('Operador científico: ')
    n2 = float(input('Segundo numero: '))

    r = calc(n1, op, n2)
    print(r)

elif(st.upper() == 'A'):

    print('Calculadora de Área\n----------------------------------------------------')

    a = input('\nSelecione qual área você deseja calcular: (C) Círculo, (T) Triângulo, (Q) Quadrado,(R) Retângulo, (P) Pentágono, (H) Hexágono\n')

    if(a == 'C' or a == 'c'):
        def circ(r):
            a = math.pi * (math.pow(r, 2))
            return a
            
        r = float(input('\nInsira o raio da circunferência: '))

        a = round(circ(r), 2)

        print(f'Área da circunferência: {a}')
        
    elif(a == 'T' or a == 't'):
        def tri(b, h):
            a = b * h / 2
            return a
            
        b = float(input('\nInsira a base do triângulo: '))

        h = float(input('\nInsira a altura do triângulo: '))

        a = round(tri(b, h), 2)

        print(f'Área do triângulo: {a}')

    elif(a == 'Q' or a == 'q'):
        def quad(l):
            a = math.pow(l, 2)
            return a

        r = float(input('\nInsira o lado do quadrado: '))
        a = round(quad(r), 2)

        print(f'Área do quadrado: {a}')

    elif(a == 'R' or a == 'r'):
        def ret(l1, l2):
            a = l1 * l2
            return a

        l1 = float(input('\nInsira um lado do retângulo: '))

        l2 = float(input('\nInsira o outro lado do retângulo: '))

        a = round(ret(l1, l2), 2)

        print(f'Área do retângulo: {a}')

    elif(a == 'P' or a == 'p'):
        def pent(l):
            a = (5 * math.pow(l, 2)) / (4 * math.tan(0.628319))
            return a

        l = float(input('\nInsira o lado do pentágono: '))

        a = round(pent(l), 2)

        print(f'Área do pentágono: {a}')

    elif(a == 'H' or a == 'h'):
        def hex(l):
            a = ((3 * math.sqrt(3)) * (math.pow(l, 2))) / 2
            return a

        l = float(input('\nInsira o lado do hexágono: '))

        a = round(hex(l), 2)

        print(f'Área do hexágono: {a}')

elif(st.upper() == 'J'):
    def simples(c, i, t):
        j = round(c * (i/100) * t, 2)
        return j
    
    def montante(c, j):
        m = c + j
        return m

    print('Calculadora de Juros\n----------------------------------------------------')

    tj = input('Insira o tipo de juros: juros simples (S) ou juros compostos (C) ')

    if(tj == 'S' or tj == 's'):

        c = float(input('Insira o capital inicial: '))

        i = float(input('Insira a taxa de juros: '))

        t = int(input('Insira o tempo da aplicação: '))

        j = simples(c, i, t)

        m = montante(c, j)

        print(f'\nTotal de juros: R${j}')
        print(f'\nMontante: R${m}')

    elif(tj == 'C' or tj == 'c'):

        def comp(c, i, t):
            j = round(c * math.pow(1 + (i / 100), t) - c, 2)
            return j

        def montante(c, j):
            m = round(c + j, 2)
            return m

        c = float(input('Insira o capital inicial: '))

        i = float(input('Insira a taxa de juros: '))

        t = int(input('Insira o tempo da aplicação: '))

        j = comp(c, i, t)

        m = montante(c, j)

        print(f'\nTotal de juros: R${j}')
        print(f'\nMontante: R${m}')

else:
    print('Caracter inválido. Encerrando aplicação.')
