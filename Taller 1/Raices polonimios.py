#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
from scipy.signal import argrelextrema


# In[31]:


def fx(x):
    return (3*(x**5))+(5*(x**4))-(x**3)


# In[32]:


def dfx(x):
    return (15*(x**4))+(20*(x**3))-(3*(x**2))


# In[33]:


def newton_raphson(f,xn):
    i=1
    while i > 1e-11:
        
        i= f(xn)/dfx(xn)
        xn1= xn-i
        xn=xn1
    
    return xn


# In[37]:


tol = 6
raices=[]  
x=np.arange(-2,2,0.01)   
for n in range(1):
    y=fx(x)
    y_abs=np.abs(y)
    mins=x[argrelextrema(y_abs, np.less)]
    for i in range(len(mins)):
        mins[i]=newton_raphson(fx,mins[i])
    raices.append(np.round(mins,tol))
    
print(raices)


# In[35]:





# In[ ]:





# In[ ]:




