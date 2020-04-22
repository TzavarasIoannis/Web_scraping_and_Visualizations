#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

names = ['2019_table.csv' , '2018_table.csv','2017_table.csv','2016_table.csv','2015_table.csv','2014_table.csv']


    
table_2019= pd.read_csv(names[0],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)
table_2018= pd.read_csv(names[1],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)
table_2017= pd.read_csv(names[2],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)
table_2016= pd.read_csv(names[3],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)
table_2015= pd.read_csv(names[4],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)
table_2014= pd.read_csv(names[5],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)




# In[2]:


#export well formed csv files 
table_2019.to_csv('table_2019.csv',encoding='utf-8-sig')
table_2018.to_csv('table_2018.csv',encoding='utf-8-sig')
table_2017.to_csv('table_2017.csv',encoding='utf-8-sig')
table_2016.to_csv('table_2016.csv',encoding='utf-8-sig')
table_2015.to_csv('table_2015.csv',encoding='utf-8-sig')
table_2014.to_csv('table_2014.csv',encoding='utf-8-sig')


# In[51]:


# in case that has strings and numbers in a column 
'''     
import re 
for column in table_2019.columns[2:]:
    i=0
    for value in table_2019[column]:
        table_2019[column][i] = re.sub("[^0-9]", "",value )
        i=i+1
''' 


# In[ ]:





# In[ ]:




