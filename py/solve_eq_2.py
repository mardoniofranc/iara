#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import math 


# In[36]:


#x^2  - 15x + 50 ;   a = 1, b = -15, c= 50 


# In[ ]:


#7x^2 + 3x  + 4 ;    a = 7, b = 3  , c = 4


# In[37]:


a = 1; b = -15;  c = 50


# In[38]:


delta = (b)*(b) - 4*(a)*(c)


# In[39]:


delta


# In[40]:


x_1  = (- b + math.sqrt(delta))/2*(a)


# In[41]:


x_2  = (- b - math.sqrt(delta))/2*(a)


# In[42]:


print(x_1, x_2, delta)


# In[76]:


def delta(a,b,c):
    delta = (b)*(b) - 4*(a)*(c)
    return delta   


# In[84]:


def solve2aequacao(a,b,c):
    solve = []
    delta = (b)*(b) - 4*(a)*(c)
    
    if (delta >= 0):
        solve.append(delta)
        x_1  = (- b + math.sqrt(delta))/2*(a)
        x_2  = (- b - math.sqrt(delta))/2*(a)
        solve.append(x_1)
        solve.append(x_2)
    
    else :
        solve.append(delta)
        delta = delta * (-1)
        x_1  = (- b + math.sqrt(delta))/2*(a)
        x_2  = (- b - math.sqrt(delta))/2*(a)
        solve.append((str(x_1) + "i"))
        solve.append((str(x_2) + "i"))
 
    return solve


# In[85]:


delta(7,3,4)


# In[86]:


solve = solve2aequacao(7,3,4)


# In[87]:


solve


# In[88]:


out  = ' '.join([str(elem) for elem in solve])


# In[89]:


out = out.replace(' ',',')


# In[90]:


out


# In[93]:


path = 'output.txt'
data = open(path,'w')
data.write(out)
data.close


# In[ ]:





# In[ ]:




