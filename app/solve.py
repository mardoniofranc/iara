#!/usr/bin/env python
# coding: utf-8

import math 

def delta(a,b,c):
    deltaf = (b)*(b) - 4*(a)*(c)
    return deltaf   

def solve2aequacao(a,b,c):
    solve = []
    deltaf = (b)*(b) - 4*(a)*(c)

    if (deltaf >= 0):
        solve.append(deltaf)
        x_1  = (- b + math.sqrt(deltaf))/2*(a)
        x_2  = (- b - math.sqrt(deltaf))/2*(a)
        solve.append(x_1)
        solve.append(x_2)
    else :
        solve.append(deltaf)
        deltaf = deltaf * (-1)
        x_1  = (- b + math.sqrt(deltaf))/2*(a)
        x_2  = (- b - math.sqrt(deltaf))/2*(a)
        solve.append((str(x_1) + "i"))
        solve.append((str(x_2) + "i"))
    return solve

import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
data_path = str(sys.argv[4])

deltaf = delta(a,b,c)
solve = solve2aequacao(a,b,c)
print(a,b,c, deltaf, solve)

out  = ' '.join([str(elem) for elem in solve])
out = out.replace(' ',',')

path = data_path + '/' + 'data/output.txt'
data = open(path,'w')
data.write(out)
data.close
