#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
qty=20
N=9
a=np.ones(10)
b=np.ones(10)
CA=np.ones(qty)

for j in range(abs(qty)):
    if qty>0:
        for i in range(N-1, 0, -1):
            a[i]=a[i-1]
            b[i]=b[i-1]
            CA[i]=CA[i-1]
        a[0]=(a[3]+a[9])%2
        a3=a[9]
        
        b1=(b[5]+b[7]+b[8]+b[9])%2
        b2=(b[1]+b[2])%2
        b3=(b[2]+b[3])%2
        b[0]=(b1+b2)%2
        
        CA3=(a3+b3)%2
        CA[j]=CA3
print(CA)


# In[ ]:




