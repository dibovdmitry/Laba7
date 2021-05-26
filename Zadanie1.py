#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys
if __name__ == '__main__':
    A = (5, 4, 3, 4, 5, 5, 3)
    G = (3, 2, 5, 5, 3, 4, 4, 4, 4, 3)
    F = (4, 2, 2, 5, 5, 5)
    SA = sum(A)
    SG = sum(G)
    SF = sum(F)
    if SA > SG and SF < SA:
        print(f'Самая высокая успеваемость по алгебре')
    elif SG > SA and SF < SG:
        print(f'Самая высокая успеваемость по геометрии')
    elif SF > SA and SG < SF:
        print(f'Самая высокая успеваемость по физике')
