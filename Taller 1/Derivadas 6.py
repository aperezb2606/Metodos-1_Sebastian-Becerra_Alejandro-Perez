# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
"Punto a del ejercicio 6"
x= np.linspace(-4,4,25)
y= np.linspace(-4,4,25)
X,Y= np.meshgrid(x,y)


"Punto b del ejercicio 6"
def Function(x,y):
    R=2
    resultado=2*x(1-(R**2)/(x**2+y**2))
    return resultado        

"Punto c del ejercicio 6"
def Derivative_x(f,x,y,h=0.001):
    resultado=(f(x+h,y)-f(x-h,y))/(2*h)
    return  resultado

def Derivative_y(f,x,y,h=0.001):
    resultado=(f(x,y+h)-f(x,y-h))/(2*h)
    return resultado

V_x= Derivative_x(Function,X,Y)
V_y= -(Derivative_y(Function,X,Y))

"Punto d del ejercicio 6"
fig= plt.figure(figsize=(5,5))
ax= fig.add_subplot(121)
for i in range(25):
    for j in range(25):
        ax.quiver(x[i], y[j], V_x[i,j], V_y[i,j])
    