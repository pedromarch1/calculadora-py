from cientifica.cien import *
from area.area import *
from juros.simples import *
from juros.comp import *
from formatar.dinh import *
import locale

st = input('Selecione o modo da calculadora: (P) Padrão, (C) Científica, (A) Área ou (J) Juros: ')

if(st.upper() == 'P'):
    print('\nCalculadora Padrão\n----------------------------------------------------')
    print('\n(+) (-) (*) (/)\n')
    a = eval(input('\nInsira uma conta utilizando os operadores acima:\n'))
    print(float(a))

elif(st.upper() == 'C'):
    print('Calculadora Científica\n----------------------------------------------------')
    n1 = float(input('Insira um numero: '))
    op = input('Operador científico: (**) (sqrt) (%) (sen) (cos) (tan) (asen) (acos) (atan) ')
    n2 = float(input('Segundo numero: '))
    r = calc(n1, op, n2)
    print(r)

elif(st.upper() == 'A'):
    print('Calculadora de Área\n----------------------------------------------------')
    a = input('\nSelecione qual área você deseja calcular: (C) Círculo, (T) Triângulo, (Q) Quadrado,(R) Retângulo, (P) Pentágono, (H) Hexágono\n')

    if(a.upper() == 'C'):        
        r = float(input('\nInsira o raio da circunferência: '))
        a = circ(r)
        print(f'Área da circunferência: {a}')
        
    elif(a.upper() == 'T'):
        b = float(input('\nInsira a base do triângulo: '))
        h = float(input('\nInsira a altura do triângulo: '))
        a = tri(b, h)
        print(f'Área do triângulo: {a}')

    elif(a.upper() == 'Q'):
        r = float(input('\nInsira o lado do quadrado: '))
        a = round(quad(r), 2)
        print(f'Área do quadrado: {a}')

    elif(a.upper() == 'R'):
        l1 = float(input('\nInsira um lado do retângulo: '))
        l2 = float(input('\nInsira o outro lado do retângulo: '))
        a = ret(l1, l2)
        print(f'Área do retângulo: {a}')

    elif(a.upper() == 'P'):
        l = float(input('\nInsira o lado do pentágono: '))
        a = pent(l)
        print(f'Área do pentágono: {a}')

    elif(a.upper() == 'H'):
        l = float(input('\nInsira o lado do hexágono: '))
        a = hex(l)
        print(f'Área do hexágono: {a}')

elif(st.upper() == 'J'):
    print('Calculadora de Juros\n----------------------------------------------------')
    tj = input('Insira o tipo de juros: juros simples (S) ou juros compostos (C) ')

    if(tj.upper() == 'S'):
        c = float(input('Insira o capital inicial: R$ '))
        i = float(input('Insira a taxa de juros anual (%): '))
        t = int(input('Insira o tempo da aplicação (meses): '))
        j = comp(c, i, t)
        m = montante(c, j)
        fj = formata_dinheiro(j)
        fm = formata_dinheiro(m)
        print(f'\nTotal de juros: {fj}')
        print(f'\nMontante: {fm}')

    elif(tj.upper() == 'C'):
        c = float(input('Insira o capital inicial: R$ '))
        i = float(input('Insira a taxa de juros anual (%): '))
        t = int(input('Insira o tempo da aplicação (anos): '))
        j = comp(c, i, t)
        m = montante(c, j)
        fj = formata_dinheiro(j)
        fm = formata_dinheiro(m)
        print(f'\nTotal de juros: {fj}')
        print(f'\nMontante: {fm}')

else:
    print('Caracter inválido. Encerrando aplicação.')
