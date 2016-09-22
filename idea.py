#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from state import State

def idastar (s_0, w=1):
    s_0.g = 0
    s_0.w = w
    f_limit = s_0.f

    while True:
        exp = 0
        gen = 0
        result, f_limit, exp, gen = contour(s_0, f_limit, exp, gen)
        if result is not None:
            return exp, gen, result
        if f_limit == 10000000:
            return None

def contour(s, f_limit, exp , gen):
    next_f = 10000000
    if goal(s):
        return s, f_limit, exp, gen

    if s.f > f_limit:
        return None, s.f, exp, gen

    s.expand(s.w)
    exp += 1
    for suc in s.succ:
        gen += 1
        suc.g = s.g + 1
        new_f = suc.f
        solution, next_f, exp, gen = contour(suc, f_limit, exp, gen)
        if solution is not None:
            return solution, f_limit, exp, gen
        next_f = min(next_f, new_f)
    return None, next_f, exp, gen

def goal(s):
    if s == State([i + 1 for i in range(len(s.array))]):
        return True
    return False
