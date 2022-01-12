import math

def simple(c, i, t):
    j = round(c * (i/100) * t, 2)
    return j


def cp(c, i, t):
    j = c * math.pow(1 + (i / 100), t) - c
    return j


def amount(c, j):
    a = c + j
    return a


def perf(initial_cap, amount):
    p = round(float(((amount / initial_cap) - 1)  * 100), 2)
    return p


