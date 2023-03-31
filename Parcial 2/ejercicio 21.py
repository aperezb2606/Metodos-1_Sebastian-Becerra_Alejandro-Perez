import numpy as np
import matplotlib.pyplot as plt
x= np.linspace(-1,1,100)
def function(x):
    valor_y=0
    if x < 0:
        valor_y=-1
    elif x == 0:
        valor_y= 0
    elif x > 0:
        valor_y= 1
    return valor_y
sgn= function(x)
funcion_sgn= np.vectorize(sgn)
plt.plot(x,funcion_sgn)
plt.show()
n=15
x,W= np.polynomial.legendre.leggauss(n)
