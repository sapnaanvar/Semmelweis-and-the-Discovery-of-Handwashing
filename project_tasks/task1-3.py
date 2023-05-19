#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
yearly = pd.read_csv("yearly_deaths_by_clinic.csv")
print(yearly)


# In[3]:


#TASK 2


yearly["propotion_deaths"]=yearly["deaths"] / yearly["births"]
yearly



# In[4]:


yearly_1 = yearly.loc[ yearly['clinic'] == 'clinic 1']
yearly_2 = yearly.loc[ yearly['clinic'] == 'clinic 2']
yearly_1


# In[7]:


#TASK3

ax = yearly_1. plot(x="year", y="deaths",
              label="clinic_1")
yearly_2. plot(x="year", y="deaths",
         label="clinic_2", ax=ax)

ax.set_ylabel("proportion_deaths")


# In[ ]:




