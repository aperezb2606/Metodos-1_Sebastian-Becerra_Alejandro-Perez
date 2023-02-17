# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
def funcion_factorial(natural:int)->int:
    natural_constante=natural
    while natural > 2:
        natural-=1
        natural_constante*=natural
    return natural_constante
"Punto a del ejercicio 6"
x= np.linspace(-4,4,25)
y= np.linspaces(-4,4,25)
"Punto b del ejercicio 6"
def Function(x):
    return 2*x(1-((4)/(x**2+y**2)))
"Punto c del ejercicio 6"

