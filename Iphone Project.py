#!/usr/bin/env python
# coding: utf-8

# In[278]:


import pandas as pd
import numpy as np
df = pd.read_csv('iphone.csv')


# In[279]:


#1 - The column names have spaces . rename the column names to have underscore '_' instead of space
#(try to do in one go instead of specifying each column nam in rename method)
df.columns = ['product_name','product_url','brand','sale_price','mrp','number_of_ratings','number_of_reviews','upc','star_rating','ram']
#better solution - df.columns = df.columns.str.replace(' ', '_')


# In[22]:


#2- start rating for some of the models is missing in the dataset. fill those missing values with the average rating all the models
avg = round(df['star_rating'].mean(),1)
df['star_rating'] = df['star_rating'].fillna(value = avg)


# In[47]:


#3- Now instead of filling missing values with avg rating of full dataset , fill with avg rating based on RAM. example : 
#if rating for a 2 gb phone is missing then take average of all other 2 gb phones rating and fill that value. 
avg_cat =  round(df.groupby('ram')['star_rating'].mean(),1).reset_index(name = 'avgs')
dfa = pd.merge(left = df, right = avg_cat, how = 'inner' ,left_on = 'ram', right_on = 'ram')
dfa['star_rating'] = df['star_rating'].fillna(value = dfa['avgs'])


# In[51]:


#4- create a new column in the dataframe "Discount_Percentage" based on MRP and sale value
df['discount_percentage'] = (df['mrp']-df['sale_price'])/df['mrp'] * 100


# In[55]:


#5- which model has highest percent discount ?
dfd = df.sort_values(by = 'discount_percentage', ascending = False)
dfd['product_name'].head(1)


# In[89]:


#6- find total no of models  each space configuration (128 GB , 64 GB etc)
c = pd.DataFrame()
c['value'] = df['product_name'].str.contains('128 GB') | df['product_name'].str.contains('64 GB')
c['value'].value_counts()


# In[211]:


#7- find total number of models for each color 

#to capture position of bracket
for i,name in enumerate(df['product_name']):
    for j in range(len(name)):
        if name[j] == '(':
           df.at[i,'open'] = j
        elif  name[j] == ')':
            df.at[i,'close'] = j
df['open'] = df['open'].astype(int)
df['close'] = df['close'].astype(int)

#extract colour and spec
for i, name in enumerate(df['product_name']):
    o = df.at[i, 'open']
    c = df.at[i, 'close']
    df.at[i, 'colour_space'] = name[o:c]

df['colour_space'] = df['colour_space'].str.replace('(','')

#extract colour 
for i,name in enumerate(df['colour_space']):
    for j in range(len(name)):
        if name[j] == ',':
           df.at[i,'colour'] = name[0:j]

df.groupby('colour')['product_name'].count().sort_values(ascending=False)



# In[280]:


#8- find total number of models by iphone version : eg
#iphone 8:  9
#iphone XR : 5
#get all the elements in product name as separate elements
for i,name in enumerate(df['product_name'].str.split('(')):
    df.at[i,'model'] = name[0]


#removing company name since all are iPhones
df['model'] = df['model'].str.replace('apple','',case = False)
#splitting the elements by space
df['model'] = df['model'].str.split(' ')
#taking only name and model 
df['final'] =  df['model'].str[1:3]
df['final'] = df['final'].str[0].str.capitalize() + ' ' + df['final'].str[1].astype(str)
df.groupby('final')['product_name'].count().sort_values(ascending=False)


# In[105]:


#9- list top 5 models having highest no of reviews 
dfs = df.sort_values(by ='number_of_reviews', ascending = False)
dfs.head(5)


# In[109]:


#10 - what is the price diffrence between highest price and lowest price iphone (based on mrp)
high  = df['sale_price'].max()
low = df['sale_price'].min()
print(high - low)


# In[123]:


#11 - find total no of reviews for iphone 11 and iphone 12 category . Output should have only 2 rows (for 11 and 12)
dfe =df[ (df['product_name'].str.contains('iphone 11', case = False)) | (df['product_name'].str.contains('iphone 12', case = False))  ]
dfe['model'] = dfe['product_name'].str.slice(6, 15)
dfe.groupby('model')['number_of_reviews'].sum()


# In[135]:


#12- which iphone has 3rd highest MRP
dfm = df.sort_values(by = 'mrp', ascending = False).reset_index()
dfm.iloc[2,1]


# In[138]:


#13- what is the average mrp of iphones which costs above 100,000
dft = df[df['mrp']> 100000]
print(dft['mrp'].mean())


# In[146]:


#14- which iphone with 128 GB space has highest ratings to review ratio
df['rr_ratio'] = df['number_of_ratings']/df['number_of_reviews']
dfab = df[df['product_name'].str.contains('128 GB')]
dfab.sort_values(by = 'rr_ratio', ascending = False, inplace = True)
dfab.head(1)

