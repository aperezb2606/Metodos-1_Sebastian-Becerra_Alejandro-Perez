#!/usr/bin/env python
# coding: utf-8

# In[95]:


import numpy as np
import matplotlib.pyplot as plt


# In[96]:


T = np.array([-3,2])
R = np.array([2,-2])


# In[97]:


t = lambda x: 1*((((x-T[0])**2)+((T[1])**2))**(1/2)) + 1.33*((((x-R[0])**2)+((R[1])**2))**(1/2))


# In[98]:


x = np.linspace(-3,3,100)
tx = t(x)

plt.plot(x, tx)
plt.show()


# In[99]:


def Derivative(f,x,h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)

def Second_Derivative(f,x,h=1e-5):
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)


# In[100]:


def Newton_Raphson(f, df,df2,xn,imax = 100, precision=1e-6):
    
    error = 1
    i = 0
    
    while error > precision and i <= imax:
        try:
            xn1 = xn - df(f,xn)/df2(f,xn)
            
            error = np.abs(df(f,xn)/df2(f,xn))

        except ZeroDivisionError:
            
            print('Division por cero')
            
        i += 1
        xn = xn1
    
    if i == imax:
        False
    else:
        return xn


# In[101]:


x_min = Newton_Raphson(t, Derivative, Second_Derivative, 1)


# In[102]:


ao = np.arccos(2/(1*((((x_min-T[0])**2)+((T[1])**2))**(1/2)))) 
a1 = np.arccos(-2/(((x_min-R[0])**2)+((R[1])**2))**(1/2))


# In[103]:


print(ao)
print(a1)


# In[104]:


snell = (np.sin(a1)/np.sin(ao))
snell_ = 1/1.33


# In[105]:


#Comprobación snell
print(snell)
print(snell_)

#Conclusión: si se cumple la ley de snell, la cantidad en la que difieren los resultados se puede despreciar


# In[ ]:





# In[ ]:




