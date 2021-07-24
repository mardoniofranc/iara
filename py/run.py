#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[10]:


#01, 5x^2 - 3x - 21  ;   a = 5, b = -3,  c= 21 
#02, x^2  - 6x       ;   a = 1, b = -6,  c= 0 
#03, x^2  - 10x + 25 ;   a = 1, b = -10, c=-25 
#04, x^2  - x - 20   ;   a = 1, b = -1,  c= 20 
#05, x^2  - 3x -4    ;   a = 1, b = -3,  c= -2 
#06, x^2  - 8x + 7   ;   a = 1, b = -8,  c= 7 
#07, x^2  - 18x + 81 ;   a = 1, b = -18, c= 81 
#08, x^2  - 5x + 6   ;   a = 1, b = -5,  c= 6 
#09, x^2  - 12x + 16 ;   a = 1, b = -12, c= 16 
#10, x^2  - 15x + 50 ;   a = 1, b = -15, c= 50 


# In[11]:


data = 'tarefas.csv'
df   = pd.read_csv(data, encoding="utf-8", sep=",")
df.head()


# In[12]:


for index, row in df.iterrows():
    print(row['job'], row['a'], row['b'], row['c'])


# In[ ]:





# In[ ]:




