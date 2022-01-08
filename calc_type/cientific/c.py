import math
def sci(n1, op, n2):
    if(op == '**'):
        r = math.pow(n1, n2)
        return r

    elif(op.lower() == 'sqrt'):
        r = n1 * math.sqrt(n2)
        return r

    elif(op == '%'):
        r = n1 * n2 / 100
        return r

    elif(op.lower() == 'sen'):
        r = n1 * math.sin(n2)
        return r

    elif(op.lower() == 'cos'):
        r = n1 * math.cos(n2)
        return r

    elif(op.lower() == 'tan'):
        r = n1 * math.tan(n2)
        return r

    elif(op.lower() == 'asen'):
        r = n1 * math.asin(n2)
        return r

    elif(op.lower() == 'acos'):
        r = n1 * math.acos(n2)
        return r

    elif(op.lower() == 'atan'):
        r = n1 * math.atan(n2)
        return r
