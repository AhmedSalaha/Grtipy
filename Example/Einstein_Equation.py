# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:48:19 2018

@author: Windows 7
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:43:33 2018

@author: Windows 7
"""


import numpy as np 
from sympy import * 

def Einstein_Equation(d,x,g,ginverse):
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

    Ricci =[[[] for j in range(d)] for i in range(d)]

    for a in range(d):
        for c in range(d):
            summation=0.0
            for i in range(d):
                summation=summation+simplify(Riemann[i][a][i][c])
            Ricci[a][c]=simplify(summation)
    summation=0.0        
    for a in range(d):
        for c in range(d):
            summation=summation+ginverse[a][c]*Ricci[a][c]
        R=summation 
    RR=R
    GG=[[[] for i in range(d)] for j in range(d)]      

    for a in range(d):
        for b in range(d):
            summ=Ricci[a][b]-(1/2)*RR*g[a][b]
            GG[a][b]=summ       
            EN=print("G[",x[a],",",x[b],"]=",simplify(GG[a][b]))
    return EN
d=4
t, r, theta, phi, k= symbols('t r theta phi k')
x=np.array([t, r,theta,phi])
a= Function('a')(t)

g00 = 1
g11 = -a**2*(1/(1-r**2/k**2))
g22 = -a**2*r**2
g33 = -a**2*r**2*sin(theta)**2

g=np.array([[g00,0,0,0],[0,g11,0,0],[0,0,g22,0],[0,0,0,g33]])

ginverse = np.array([[np.reciprocal(g00),0,0,0],[0,np.reciprocal(g11),0,0],[0,0,np.reciprocal(g22),0],[0,0,0,np.reciprocal(g33)]])

print(Einstein_Equation(d,x,g,ginverse))
