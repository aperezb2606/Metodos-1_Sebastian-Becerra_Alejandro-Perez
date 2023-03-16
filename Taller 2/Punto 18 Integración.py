import sympy as sym
import numpy as np
"Punto a ejercicio 18 de integración"
x=sym.Symbol("x")
lista_ceros= np.zeros(20)
lista_pesos=np.zeros(20)
n=1
while n <= 20:
 Hn= ((-1)**n)*np.exp(x**2)*(sym.diff(np.exp(-(x**2)),x,n))
 x_raiz= sym.solve(Hn,x)
 lista_ceros[n-1]=x_raiz
 w= ((2**(n-1))*np.math.factorial(n)*((np.pi)**(1/2)))/((n**2)*((-1)**(n-1))*np.exp((x_raiz)**2)*(sym.diff(np.exp(-((x_raiz)**2)),x,n-1)))
 lista_pesos[n-1]=w
 n+=1
"Las raíces y los pesos se entragara en orden a través de arrays"
print(lista_ceros)
print(lista_pesos)
