#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r'E:\DA Test\Find 3 Useful insights from this messy data\Market Prices.xlsx')
df.head()


# In[56]:


df1=df.iloc[:,:]
df1.drop_duplicates(inplace=True)
df1.reset_index(drop=True,inplace=True)
df1.head()


# ## Counting the total number of companies 

# In[60]:


st=set(df['Company'])
lst=list(st)
len(lst)


# ## Knowing the number of watt types for each lamp for each company

# In[46]:


for i in range(len(lst)):
    grouped1 = df.groupby('Company')
    df_grouped1 = grouped1.get_group(lst[i]).iloc[:,:]
    if df_grouped1.Watt.value_counts().empty :
        continue
    else:
        print("The Count of Watt lamps for Company :" , lst[i] ,'\n', df_grouped1.Watt.value_counts().sum())


#  ## Knowing the number of items for each company

# In[112]:


lst1 = []
lst2 = []
for i in range(len(lst)):
    grouped1 = df.groupby('Company')
    df_grouped1 = grouped1.get_group(lst[i]).iloc[:,:]
    if df_grouped1.Item.value_counts().empty :
        continue
    else:
        lst1.append(df_grouped1.Item.value_counts().sum())
        lst2.append(lst[i])
        print("The Count of items for Company :" , lst[i] ,'\n', df_grouped1.Item.value_counts().sum())


# # Most company has the most number of items

# In[111]:


print(lst2[lst1.index(max(lst1))]," : ",max(lst1))


# ## List of companies that own more than 100 items 

# In[110]:


lst3=lst1.copy()
lst3.sort(reverse=True)
lst4=lst3[:8]
lst5 = [lst2[lst1.index(lst4[i])] for i in range(len(lst4))]
print(lst5)


# # Reading Sheet "Prices" at Excel file

# In[122]:


df2 = pd.read_excel(open(r'E:\DA Test\Find 3 Useful insights from this messy data\Market Prices.xlsx', 'rb'),
              sheet_name='Prices')  
df2.head()


# ## Plotting the average prices for each company

# In[132]:


plt.scatter(lst,lst6)
plt.show()


# ## Showing companies that have outliers from average prices (greater than 1000) 

# In[136]:


lst7


# ## Plotting histograms for prices of each company

# In[135]:


lst6 = []
lst7 = []
for i in range(len(lst)):
    grouped2 = df2.groupby('Company')
    df_grouped2 = grouped2.get_group(lst[i]).iloc[:,:]
    lst6.append(df_grouped2['Price'].mean())
    if df_grouped2['Price'].mean()>1000 :
        lst7.append([lst[i],df_grouped2['Price'].mean()])
    plt.hist(df_grouped2['Price'])
    plt.show()


# In[ ]:




