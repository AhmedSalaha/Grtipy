import numpy as np 
from sympy import * 

def Riemann_All(d,x,g,ginverse):
    christoffel = [[[[]for k in range(d)] for j in range(d)] for i in range(d)]
    for n in range(d):
        for a in range(d):
            for b in range(d):
                summation=0.0
                for i in range(d):
                    summation= summation+ginverse[n][i]*(diff(g[i][a],x[b])+diff(g[i][b],x[a])-diff(g[a][b],x[i]))
                christoffel[n][a][b]=summation/2
    

    Riemann= [[[[[] for l in range(d)] for k in range(d)] for j in range(d)] for i in range(d)]

    for n in range(d):
        for a in range(d):
            for b in range(d):
                for c in range(d):
                    parials=diff(christoffel[n][a][c],x[b])-diff(christoffel[n][a][b],x[c])
                    summation=0.0
                    for i in range(d):
                        summation=summation+christoffel[n][b][i]*christoffel[i][a][c]-christoffel[n][c][i]*christoffel[i][a][b]
                    Riemann[n][a][b][c]=parials+summation

    for n in range(0,d):
        for a in range(0,d):
            for b in range(0,d):
                for c in range(d):
                    Rie=print("Riemann[",x[n],"]","[",x[a],"]","[",x[b],"]","[",x[c],"]=", simplify(Riemann[n][a][b][c]))
    return Rie
