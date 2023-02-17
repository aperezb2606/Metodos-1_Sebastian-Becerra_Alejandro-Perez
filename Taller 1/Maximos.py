#!/usr/bin/env python
# coding: utf-8

# In[326]:


import numpy as np
import matplotlib.pyplot as plt


# In[327]:


archivo = np.loadtxt("EstrellaEspectro.txt")


# In[328]:


print(archivo)


# In[329]:


def columna_1():
    datos = archivo
    for i in range(len(datos[1,:])):
        col1 = datos[:,i]
        return col1

def columna_2():
    datos = archivo
    for i in range(len(datos[1,:])):
        col2 = datos[:,i]
    return col2  

axisx = columna_1()
axisy = columna_2()

def maximos():
    ax = axisx
    ay = axisy
    maximosx = []
    maximosy = []
    for k in range(1, (len(ax)-1)):
        if (ay[k] > ay[k+1]) and (ay[k] > ay[k-1]):
            maximosx.append(ax[k])
            maximosy.append(ay[k])
    return maximosx, maximosy
        


# In[330]:


plt.figure()
plt.plot(axisx,axisy)
plt.scatter(maximos()[0], maximos()[1], color = "r", marker="o")
plt.show()


# In[ ]:




