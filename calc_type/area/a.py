import math

def circ(r):
    a = round(math.pi * (math.pow(r, 2)), 2)
    return a

def tri(b, h):
    a = round(b * h / 2, 2)
    return a


def sqr(l):
    a = math.pow(l, 2)
    return a

def ret(l1, l2):
    a = round(l1 * l2, 2)
    return a

def pent(l):
    a = round((5 * math.pow(l, 2)) / (4 * math.tan(0.628319)), 2)
    return a

def hex(l):
    a = round(((3 * math.sqrt(3)) * (math.pow(l, 2))) / 2, 2)
    return a
