#!/usr/bin/env python
# coding: utf-8

# In[1]:


import env
import pandas as pd
import os


# In[23]:


def get_titanic_data():   
    if os.path.exists('titanic.csv'):
        return pd.read_csv('titanic.csv')
    else:
        url = env.get_connection('titanic_db')
        query = 'select * from passengers'
        df = pd.read_sql(query,url)
        df.to_csv('titanic.csv')
        return df


# In[24]:


def get_iris_data(): 
    if os.path.exists('iris.csv'):
        return pd.read_csv('iris.csv')
    else:
        url = env.get_connection('iris_db')
        query = 'select * from measurements join species using (species_id)'
        df = pd.read_sql(query,url)
        df.to_csv('iris.csv')
        return df


# In[25]:


def get_telco_data():   
    if os.path.exists('telco.csv'):
        return pd.read_csv('telco.csv')
    else:
        url = env.get_connection('telco_churn')
        query = 'select * from customers join contract_types using (contract_type_id) join internet_service_types using (internet_service_type_id) join payment_types using (payment_type_id)'
        df = pd.read_sql(query,url)
        df.to_csv('telco.csv')
        return df


# In[ ]:




