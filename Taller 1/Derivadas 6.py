import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
"Punto a del ejercicio 6"
n = 25
x = np.linspace(-4,4,n)
y = np.linspace(-4,4,n)
X,Y = np.meshgrid(x,y)
"Punto b del ejercicio 6"
def Function(x,y):
    R=2
    resultado=2*x*(1-((R**2)/(x**2+y**2)))
    return resultado       
"Punto c del ejercicio 6"
def Derivative_x(f,x,y,h=0.001):
    resultado=(f(x+h,y)-f(x-h,y))/(2*h)
    return  resultado

def Derivative_y(f,x,y,h=0.001):
    resultado=(f(x,y+h)-f(x,y-h))/(2*h)
    return resultado
V_x= np.zeros((n,n))
V_y= np.zeros((n,n))
for i in range(n):
    for j in range(n):
        V_x[i,j]=Derivative_x(Function,x[i],y[j])
        V_y[i,j]=Derivative_x(Function,x[i],y[j])
        
        V_x[i,j]+=Derivative_x(Function,x[i],y[j])
        V_y[i,j]+=Derivative_x(Function,x[i],y[j])
"Punto d del ejercicio 6"
fig= plt.figure(figsize=(5,5))
ax= fig.add_subplot(121)
for i in range(n):
    for j in range(n):
        ax.quiver(x[i], y[j], V_x[i,j], V_y[i,j])