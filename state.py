#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# Las instacias del problma serán arreglos representados por listas
# s será un arreglo

class State:
    n = 0

    def __init__(self, lista, w=1):
        self.array = lista
        self.w = w
        self.g = 100000000
        self.h = h(lista)
        self.parent = None
        self.pos = None
        self.succ = []
        self.n += 1
        self.largo = 1

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        if isinstance(other, State):
            if self.array == other.array:
                #self.pos = other.pos
                return True
        return False

    def __repr__(self):
        return str(self.array)

    @property
    def f(self):
        return self.g + self.w * self.h

    def expand(self, w):
        n = len(self.array)
        for i in range(2, n + 1):
            sucesor = State(flip(self.array, i), w=w)
            self.succ.append(sucesor)


    def largo_path(self):
        if self.parent:
            self.largo += self.parent.largo_path()
        return self.largo

def flip(lista, i):
    pre = lista[:i]
    pre.reverse()
    return pre + lista[i:]


def h(s):
    h_value = 0
    for i in range(len(s) - 1):
        if abs(s[i] - s[i+1]) > 1:
            h_value += 1
    return h_value

def fhash(lista):
    rep = ''
    for i in lista:
        rep += str(i)
    return rep

if __name__ == '__main__':
    a = State([3, 1, 2])
    b = State([2, 1, 3])
    a.expand()
    print(a.succ)
