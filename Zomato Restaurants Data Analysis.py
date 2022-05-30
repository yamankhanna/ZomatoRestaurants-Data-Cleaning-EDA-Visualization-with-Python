#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_csv(r"C:\Users\hp\Downloads\Compressed\zomato.csv")


# In[6]:


df.head()


# In[7]:


df.shape


# In[8]:


df.columns


# In[21]:


df.drop(["url","dish_liked","reviews_list","menu_item","address","phone"],axis=1,inplace=True)


# In[22]:


df.info()


# In[23]:


df.drop_duplicates(inplace = True)


# In[24]:


df.shape


# In[25]:


df.head()


# In[26]:


df["rate"].unique()


# In[35]:


def handlerate(value):
    if value=='NEW' or value=='-':
        return np.nan
    else:
        value = str(value).split('/')
        value = value[0]
        return float(value)
    
df['rate'] = df['rate'].apply(handlerate)


# In[36]:


df["rate"].head()


# In[37]:


df["rate"].isnull().sum()


# In[42]:


df["rate"].fillna(df["rate"].mean(), inplace=True)


# In[44]:


df["rate"].isnull().sum()


# In[45]:


df.info()


# In[46]:


df.dropna(inplace = True)


# In[47]:


df.head()


# In[48]:


df.rename(columns = {"approx_cost(for two people)":"cost2plates", "listed_in(type)":"type"}, inplace = True)


# In[49]:


df.head()


# In[50]:


df["location"].unique()


# In[51]:


df["listed_in(city)"].unique()


# In[143]:


df.drop(["listed_in(city)"], axis = 1, inplace=True)


# In[55]:


df["cost2plates"].unique()


# In[56]:


def handlecomma(value):
    value = str(value)
    if "," in value:
        value = value.replace(",", "")
        return float(value)
    else:
        return float(value)

df["cost2plates"] = df["cost2plates"].apply(handlecomma)


# In[57]:


df["cost2plates"].head()


# In[58]:


df["cost2plates"].unique()


# In[60]:


df["rest_type"].value_counts()


# In[61]:


rest_types = df["rest_type"].value_counts(ascending=False)


# In[63]:


rest_types


# In[65]:


rest_types_lessthan1000 = rest_types[rest_types<1000]


# In[66]:


rest_types_lessthan1000


# In[67]:


def handle_rest_type(value):
    if value in rest_types_lessthan1000:
        return "others"
    else:
        return value


# In[68]:


df["rest_type"] = df["rest_type"].apply(handle_rest_type)


# In[70]:


df["rest_type"].unique()


# In[71]:


df["rest_type"].value_counts()


# In[73]:


df["location"].value_counts()


# In[74]:


location = df["location"].value_counts(ascending=False)


# In[75]:


location_lessthan300 = location[location<300]


# In[76]:


def handle_location(value):
    if value in location_lessthan300:
        return "others"
    else:
        return value


# In[77]:


df["location"] = df["location"].apply(handle_location)


# In[78]:


df["location"].value_counts()


# In[79]:


df.head()


# In[80]:


df["cuisines"].value_counts()


# In[81]:


cuisines = df["cuisines"].value_counts(ascending=False)


# In[82]:


cuisines_lessthan100 = cuisines[cuisines<100]


# In[83]:


def handle_cuisines(value):
    if value in cuisines_lessthan100:
        return "others"
    else:
        return value


# In[84]:


df["cuisines"] = df["cuisines"].apply(handle_cuisines)


# In[85]:


df["cuisines"].value_counts()


# In[88]:


df["type"].value_counts()


# In[96]:


plt.figure(figsize=(16,10))
location_count = sns.countplot(df["location"])
plt.xticks(rotation=90)


# In[98]:


plt.figure(figsize=(6,6))
sns.countplot(df['online_order'])


# In[99]:


sns.countplot(df['book_table'])


# In[101]:


plt.figure(figsize=(6,6))
sns.boxplot(x="online_order",y="rate",data=df)


# In[103]:


plt.figure(figsize=(6,6))
sns.boxplot(x="book_table",y="rate",data=df)


# In[116]:


plt.figure(figsize=(14,10))
sns.boxplot(x="type",y="rate",data=df)


# In[130]:


df.head()


# In[144]:


df.head()


# In[148]:


df.shape


# In[149]:


df.to_csv("Zomato Banglore Data Cleaned.csv")


# In[ ]:




