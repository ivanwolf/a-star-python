#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from state import State
from heap import BinHeap


def astar(s_0, w=1):
    """
    s_0: Objeto tipo State
    w: peso de la heuristica
    """


    def goal(n, w):
        return State([i + 1 for i in range(n)], w)

    def improve(u, v):
        cost_v = u.g + 1
        if cost_v >= v.g:
            return
        v.g = cost_v
        v.parent = u
        if v.pos is not None:  # i.e v in Open
        #if v in Open:
            # Entramos a la open pero no tenemos posicion!
            Open.swap_up(v.pos)
        elif v in Closed:
            Closed.remove(v)
            Open.insert(v)
        else:
            Open.insert(v)


    ## INICIO

    n = len(s_0.array)
    s_g = goal(n, w)
    Closed = []
    Open = BinHeap()
    Open.insert(s_0)
    s_0.w = w
    s_0.g = 0

    expansiones = 0
    nodos_expandidos = 0

    while Open:
        u = Open.del_min()
        Closed.append(u)

        if u == s_g:
            return expansiones, nodos_expandidos, u

        u.expand(w)
        expansiones += 1
        for v in u.succ:
            nodos_expandidos += 1
            improve(u, v)
