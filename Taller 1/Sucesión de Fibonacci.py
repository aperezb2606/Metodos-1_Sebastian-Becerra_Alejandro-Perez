#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt


# In[8]:


def fibonacci(n_max:int):
    f0 = 0
    f1 = 1
    fib = np.array([f0,f1])
    for n in range(2, n_max+1):
        fn = (fib[n-1]) + (fib[n-2])
        fib = np.append(fib,fn)
    return fib


# In[9]:


a = fibonacci(40)
fibonacci_20 = a[:20] #20 primeros valores de la serie de fibonacci
axisx=np.arange(len(fibonacci_20))
plt.figure()
plt.plot(axisx,fibonacci_20,color='g',label="Sucesión de Fibonacci")
plt.legend(loc=0)
plt.show()


# In[10]:


def fib_aureo():
    fib = fibonacci(20)
    aureo1 = np.array([])
    for i in range(2,21):
        aureo1 = np.append(aureo1, (fib[i]/fib[i-1]))
    return aureo1


# In[11]:


num_aureo = (1+(5**(1/2)))/2 #Valor teórico aureo

def aureo(k:int):
    return num_aureo


# In[12]:


b = fib_aureo()
axisy = range(2,20)
plt.figure()
plt.plot(b,label="Estimación con la serie fibonacci")
rango = range(0, len(fib_aureo()))
plt.plot([aureo(i) for i in rango], ls='--', color = "r", label="Valor exacto número aureo")
plt.legend(loc=0)
plt.show()


# In[ ]:





# In[ ]:




