import math

def comp(c, i, t):
    j = c * math.pow(1 + (i / 100), t) - c
    return j

def montante(c, j):
    m = c + float(j)
    return m