#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplement
ation.html
"""


class BinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def __repr__(self):
        return str(self.heap_list)

    def __len__(self):
        return len(self.heap_list)

    def __contains__(self, item):
        return item in self.heap_list

    def swap_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                aux = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = aux
                self.heap_list[i // 2].pos = i
                self.heap_list[i].pos = i // 2
            i = i // 2

    def insert(self, state):
        self.heap_list.append(state)
        self.current_size += 1
        self.swap_up(self.current_size)
        state.pos = self.current_size

    def swap_down(self, i):
        while i * 2 <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
                if i // 2 > 0:
                    self.heap_list[i // 2].pos = i
                    self.heap_list[i].pos = i // 2
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.swap_down(1)
        return retval
