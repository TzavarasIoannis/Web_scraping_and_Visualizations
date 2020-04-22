#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports
import bs4
from csv import writer 
import requests



# In[2]:


from bs4 import BeautifulSoup as soup 


# In[17]:


#URL :superleage football leageu (Greek championship) , 6 years period => 6 tables => 6 pages 
ural_names = ['https://www.slgr.gr/el/scoreboard/18/','https://www.slgr.gr/el/scoreboard/17/',
              'https://www.slgr.gr/el/scoreboard/16/','https://www.slgr.gr/el/scoreboard/15/',
              'https://www.slgr.gr/el/scoreboard/14/','https://www.slgr.gr/el/scoreboard/13/']


# In[18]:


i=0
season= 2019
for ural_name in ural_names: #for each URL
    uclient = requests.get(ural_name)#grap the page 
    page_soup = soup(uclient.text, 'html.parser') 
     
    container = page_soup.find_all('div',{'class' :  'table-row'}) #focus on the html part with names points etc..
    #names for csv creation
    names = ['2019_table.csv' , '2018_table.csv','2017_table.csv','2016_table.csv','2015_table.csv','2014_table.csv']
    #demostrate a csv file 
    with open( names[i], "w" ,encoding='utf-8'  ) as csv_file : 
        csv_writer = writer(csv_file)  #create a csv file 
        Headers= ['Season', 'Team', 'Points' , 'Goals_for_+' , 'Goals_against_-', 'Wins', 'Draws', 'Losses'] #csv headers
        csv_writer.writerow(Headers)  

        #first two objects in list container don't have the info that we need 
        for dock in container[2:] : 
            team_name = dock.find('span' , {'class' : 'full-name'})  #grap the name

            points = dock.find('div' , {'class' : 'd-inline-block text-center horizontal-center sm-width bold'}) #grap the ponts 

            goal_for = dock.find_all('div' , {'class' : 'd-inline-block text-center horizontal-center sm-width mobile-hide'})[0] #grap the goals for

            goal_against = dock.find_all('div' , {'class' : 'd-inline-block text-center horizontal-center sm-width mobile-hide'})[1] #grap the goals_ agains

            wins = dock.findChildren("div", { 'class' : 'text-center horizontal-center filter-option option-0 sm-width mobile-hide'})[0] #grap the wins

            draws = dock.findChildren("div", { 'class' : 'text-center horizontal-center filter-option option-0 sm-width mobile-hide'})[1] # grap the draws

            losses = dock.findChildren("div", { 'class' : 'text-center horizontal-center filter-option option-0 sm-width mobile-hide'})[2]#grap the losses
            #write a row in csv 
            csv_writer.writerow([season, team_name.text,points.text,goal_for.text,goal_against.text,wins.text, draws.text,losses.text])  #write in csv 
            
    season = season - 1
    i= i + 1 


# In[ ]:





# In[ ]:





# In[ ]:




