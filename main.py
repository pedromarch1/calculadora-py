from calc_type.default.d import *
from calc_type.cientific.c import *
from calc_type.area.a import *
from calc_type.interest.i import *
from formatation.form import *
from tkinter import *

st = input('Select calculator mode: (D) Default, (C) Cientific, (A) Area or (I) Interest: ')

if(st.upper() == 'D'): #Basic operations for daily routines
    print('\nDefault Calculator\n----------------------------------------------------')
    n1 = float(input('\nInsert a number:\n'))
    op = input('\n(+) (-) (*) (/) (%) \n')
    n2 = float(input('\nInsert another number:\n'))
    r = d(n1, op, n2)
    print(f'\nOperation result:\n{r}')

elif(st.upper() == 'C'): #Calculate scientific values using special features, such as trigonometry
    print('\nCientific Calculator\n----------------------------------------------------')
    n1 = float(input('\nNumber:\n'))
    op = input('\n(**) (sqrt) (sen) (cos) (tan) (asen) (acos) (atan)\n')
    n2 = float(input('\nSecond number:\n'))
    r = sci(n1, op, n2)
    print(f'\nOperation result:\n{r}')

elif(st.upper() == 'A'): #Calculate an area of a reagular form, based on values given by the user
    print('\nArea Calculator\n----------------------------------------------------')
    a = input('\nArea type: (C) Circunference, (T) Triangle, (S) Square,(R) Rectangle, (P) Pentagon, (H) Hexagon\n')

    if(a.upper() == 'C'):        
        r = float(input('\nInsert circunference radius (m): '))
        a = circ(r)
        print(f'\nCircunference area: {a} sq. m')
        
    elif(a.upper() == 'T'):
        b = float(input('\nInsert triangle base (m): '))
        h = float(input('\nInsert triangle height (m): '))
        a = tri(b, h)
        print(f'Triangle area: {a} sq. m')

    elif(a.upper() == 'S'):
        r = float(input('\ninsert side of square (m): '))
        a = round(sqr(r), 2)
        print(f'Square area: {a} sq. m')

    elif(a.upper() == 'R'):
        l1 = float(input('\nInsert one side of the rectangle (m): '))
        l2 = float(input('\nInsert the other side of the rectangle (m): '))
        a = ret(l1, l2)
        print(f'Rectangle area: {a} sq. m')

    elif(a.upper() == 'P'):
        l = float(input('\nInsert the pentagon side (m): '))
        a = pent(l)
        print(f'Pentagon area: {a} sq. m')

    elif(a.upper() == 'H'):
        l = float(input('\nInsert the hexagon side (m): '))
        a = hex(l)
        print(f'Hexagon area: {a} sq. m')

elif(st.upper() == 'I'): #Calculate interests on an investment
    print('Interest Calculator\n----------------------------------------------------')
    tj = input('Interest type: Simple (S) Coumpound (C) ')

    if(tj.upper() == 'S'):
        c = float(input('Initial Capital: $'))
        i = float(input('Anual interest (%): '))
        t = int(input('Aplication time (years): '))
        j = simple(c, i, t)
        a = amount(c, j)
        fj = format_curr(j)
        fm = format_curr(a)
        p = perf(c, a)
        print(f'\nTotal Gains: {fj} (After {t} year(s))')
        print(f'\nTotal Amount: {fm} (Performance: {p}%)')

    elif(tj.upper() == 'C'):
        c = float(input('Initial Capital: $'))
        i = float(input('Anual interest (%): '))
        t = int(input('Aplication time (years): '))
        j = cp(c, i, t)
        a = amount(c, j)
        fj = format_curr(j)
        fm = format_curr(a)
        p = perf(c, a)
        print(f'\nTotal Gains: {fj} (After {t} year(s))')
        print(f'\nTotal Amount: {fm} (Performance: {p}%)')

else:
    print('Invalid character. Closing application...')
