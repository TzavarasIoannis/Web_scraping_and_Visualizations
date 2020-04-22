#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import packages
import pandas as pd 
import matplotlib.pyplot as plt


# In[2]:



#create a dataframe each table
names = ['2019_table.csv' , '2018_table.csv','2017_table.csv','2016_table.csv','2015_table.csv','2014_table.csv']


table_2019= pd.read_csv(names[0],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)
table_2018= pd.read_csv(names[1],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)
table_2017= pd.read_csv(names[2],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)
table_2016= pd.read_csv(names[3],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)
table_2015= pd.read_csv(names[4],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)
table_2014= pd.read_csv(names[5],names=['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'],sep=',',na_values=["\r\n"],header=0)



# In[3]:


#lets choose to visualize the total wins and total goals for this 6 years period

dictionary1 ={}
dictionary2 ={}

#create  dictionaries for season 2019 , one dict for total goals and one for total wins
for i in range(0,len(table_2019)):
    
    dictionary1[table_2019['Team'][i]] = table_2019['Wins'][i]
    dictionary2[table_2019['Team'][i]] = table_2019['Goals_for_+'][i]-table_2019['Goals_against_-'][i]

    

#list of dataframes for the rest of the seasons 
list_of_df =[ table_2018,table_2017,table_2016,table_2015,table_2014 ]



#this function returns a dict  the number of the wins for teams in current season table for all seasons 
def dict_of_wins(dictionary:dict, lista:list):
    
    for table in lista: #for each season 
         
        for key,values in dictionary.items():  #for teams : wins pairs in dict

            for i in range(0, len(table)):  
                    if table['Team'][i] in dictionary.keys():
                       # print(table['Team'])
                        dictionary.update( { table['Team'][i] :table['Wins'][i]+values}) #update the wins

    return dictionary


#this function returns a dict with  total for and against goals 
def total_for_and_against_goals(lista:list,dictionary:dict):
    
    
    
        for table in lista:
        
            for key,values in dictionary.items():

                for i in range(0, len(table)):
                        if table['Team'][i] in dictionary.keys():
                           # print(table['Team'])
                            dictionary.update( { table['Team'][i] : (table['Goals_for_+'][i]-table['Goals_against_-'][i])+ values})
                            
        return dictionary

                            
    
    


# In[31]:


total_wins = dict_of_wins(dictionary1 , list_of_df)
goals = total_for_and_against_goals(list_of_df,dictionary2)


# In[128]:


import seaborn as sn
plt.figure( figsize=(9,7) )
ax=sn.barplot(list( total_wins.keys()),  list ( total_wins.values())  ,palette='Paired' )

plt.xticks(rotation=75)
plt.title('Total wins for seasons: 2019 - 2014'  , size=18)
plt.xlabel('Teams',size=15)
plt.ylabel('Wins',size=15)
plt.ylim([0,150])
for index , row in enumerate (total_wins.values()):
        ax.text(index , row,row , ha='center'  ,va=  'bottom'  , fontsize=12) 

        
plt.show()
    


# In[149]:


plt.figure( figsize=(9,7) )


ax=sn.barplot(list( goals.keys()),  list ( goals.values())  ,palette='Paired' )

plt.xticks(rotation=75)
plt.title('Total for & against Goals for seasons: 2019 - 2014'  , size=18)
plt.xlabel('Teams',size=15)
plt.ylabel('Goals',size=15)
plt.ylim([-60,150])
for index , row in enumerate (goals.values()):
        ax.text(index , row,row , ha='center'  ,va=  'bottom'  , fontsize=12) 

        
plt.show()
    


# In[ ]:




