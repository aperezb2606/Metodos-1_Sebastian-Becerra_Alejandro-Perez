# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
def funcion_factorial(natural:int)->int:
    natural_constante=natural
    while natural > 2:
        natural-=1
        natural_constante*=natural
    return natural_constante

