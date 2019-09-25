#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# In[2]:


indeed_data = "indeed_job_dataset.csv"


# In[3]:


df = pd.read_csv(indeed_data)
df.info()
# questions:
# top five induestries
# top five companies in those industries
# rating of the companies
#company revenue has sig amount of null values 2017/5715, consider not using 


# In[4]:


# Collect only relevant columns 
columns = [
    'Company_Industry',
    'Company',
    'No_of_Stars',
]
df_company = df[columns]


# In[5]:


#removing nulls from dataset
df_company = df_company[df_company.Company_Industry.notnull()]
df_company.head(10)


# # Top Industries:

# In[6]:


#Review unique industry names in dataset
industries = df_company.Company_Industry.unique()
industries


# In[7]:


#top five industries by number of job listings 
series_by_industry = df_company['Company_Industry'].value_counts()
series_by_industry.head(5)


# In[8]:


series_by_industry_top5 = series_by_industry.sort_values(ascending=False)[:5]
top_5_industries = series_by_industry_top5.index


# In[9]:


target_values = series_by_industry_top5.values
target_values


# In[10]:


#plotting pie chart

target_series = series_by_industry_top5


labels = target_series.index
sizes = target_series.values
colors = ["yellowgreen","orange","orangered","cornflowerblue","yellow"]
explode = (0.1,0,0,0,0)

#Plot; note 'tight' allows for all text to be displayed on PDF
plt.pie(sizes,  labels=labels,  colors = colors, autopct='%1.1f%%', shadow=True, startangle=140, textprops={'color':"black"})

plt.axis('equal')
plt.savefig('piechart_top5.png', bbox_inches="tight", transparent = False)

plt.show()


# # Top Companies Within Industries

# In[11]:


df_company.head()


# In[12]:


#list top five companies per top five industries- Industry 1

top_5_industry_1 = df_company.loc[df_company['Company_Industry'] == 'Consulting and Business Services', :]

rating_table = top_5_industry_1.groupby(['Company']).agg(['mean'])

job_count_table = top_5_industry_1.groupby(['Company']).agg(['count'])


job_count_table = job_count_table['Company_Industry']
finalTable = pd.concat([job_count_table,rating_table], axis=1) 
finalTable = finalTable.sort_values(by=['count'], ascending=False)
finalTable = finalTable[:5]

finalTable = finalTable['No_of_Stars', 'mean']
labels = finalTable.index
sizes = finalTable.values

objects = labels
y_pos = np.arange(len(objects))
performance = sizes
color= ('yellowgreen')

plt.bar(y_pos, performance, align='center', color = color, alpha=0.5)
plt.xticks(y_pos, objects,rotation=25)
plt.ylabel('Rating')
plt.title('Top 5 Companies in Consulting and Business Services')

for i, v in enumerate(sizes):
    plt.text(y_pos[i] , v + 0.01, str(round(v, 2)))
    
plt.savefig('industry1.png', bbox_inches="tight", transparent = False)
plt.show()


       


# In[13]:


#list top five companies per top five industries- Industry 2

top_5_industry_1 = df_company.loc[df_company['Company_Industry'] == 'Internet and Software', :]

rating_table = top_5_industry_1.groupby(['Company']).agg(['mean'])

job_count_table = top_5_industry_1.groupby(['Company']).agg(['count'])


job_count_table = job_count_table['Company_Industry']
finalTable = pd.concat([job_count_table,rating_table], axis=1) 
finalTable = finalTable.sort_values(by=['count'], ascending=False)
finalTable = finalTable[:5]

finalTable = finalTable['No_of_Stars', 'mean']
labels = finalTable.index
sizes = finalTable.values

objects = labels
y_pos = np.arange(len(objects))
performance = sizes
color= ('orangered')
# plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
# plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
plt.bar(y_pos, performance, align='center', color = color, alpha=0.5)
plt.xticks(y_pos, objects,rotation=25)
plt.ylabel('Rating')
plt.title('Top 5 Companies in Internet and Software')

for i, v in enumerate(sizes):
    plt.text(y_pos[i] , v + 0.01, str(round(v, 2)))
    
plt.savefig('industry2.png', bbox_inches="tight", transparent = False)
plt.show()


       


# In[14]:


#list top five companies per top five industries- Industry 3

top_5_industry_1 = df_company.loc[df_company['Company_Industry'] == 'Banks and Financial Services', :]

rating_table = top_5_industry_1.groupby(['Company']).agg(['mean'])

job_count_table = top_5_industry_1.groupby(['Company']).agg(['count'])


job_count_table = job_count_table['Company_Industry']
finalTable = pd.concat([job_count_table,rating_table], axis=1) 
finalTable = finalTable.sort_values(by=['count'], ascending=False)
finalTable = finalTable[:5]

finalTable = finalTable['No_of_Stars', 'mean']
labels = finalTable.index
sizes = finalTable.values

objects = labels
y_pos = np.arange(len(objects))
performance = sizes
color= ('red')
# plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
# plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
plt.bar(y_pos, performance, align='center', color = color, alpha=0.5)
plt.xticks(y_pos, objects,rotation=25)
plt.ylabel('Rating')
plt.title('Top 5 Companies in Banks and Financial Services')

for i, v in enumerate(sizes):
    plt.text(y_pos[i] , v + 0.01, str(round(v, 2)))
    
plt.savefig('industry3.png', bbox_inches="tight", transparent = False)
plt.show()


       


# In[15]:


#list top five companies per top five industries- Industry 4

top_5_industry_1 = df_company.loc[df_company['Company_Industry'] == 'Health Care', :]

rating_table = top_5_industry_1.groupby(['Company']).agg(['mean'])

job_count_table = top_5_industry_1.groupby(['Company']).agg(['count'])


job_count_table = job_count_table['Company_Industry']
finalTable = pd.concat([job_count_table,rating_table], axis=1) 
finalTable = finalTable.sort_values(by=['count'], ascending=False)
finalTable = finalTable[:5]

finalTable = finalTable['No_of_Stars', 'mean']
labels = finalTable.index
sizes = finalTable.values

objects = labels
y_pos = np.arange(len(objects))
performance = sizes
color= ('cornflowerblue')
# plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
# plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
plt.bar(y_pos, performance, align='center', color = color, alpha=0.5)
plt.xticks(y_pos, objects,rotation=25)
plt.ylabel('Rating')
plt.title('Top 5 Companies in Health Care')

for i, v in enumerate(sizes):
    plt.text(y_pos[i] , v + 0.01, str(round(v, 2)))
    
plt.savefig('industry4.png', bbox_inches="tight", transparent = False)
plt.show()


       


# In[16]:


#list top five companies per top five industries- Industry 5

top_5_industry_1 = df_company.loc[df_company['Company_Industry'] == 'Insurance', :]

rating_table = top_5_industry_1.groupby(['Company']).agg(['mean'])

job_count_table = top_5_industry_1.groupby(['Company']).agg(['count'])


job_count_table = job_count_table['Company_Industry']
finalTable = pd.concat([job_count_table,rating_table], axis=1) 
finalTable = finalTable.sort_values(by=['count'], ascending=False)
finalTable = finalTable[:5]

finalTable = finalTable['No_of_Stars', 'mean']
labels = finalTable.index
sizes = finalTable.values

objects = labels
y_pos = np.arange(len(objects))
performance = sizes
color= ('yellow')
# plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
# plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = False
plt.bar(y_pos, performance, align='center', color = color, alpha=0.5)
plt.xticks(y_pos, objects,rotation=25)
plt.ylabel('Rating')
plt.title('Top 5 Companies in Insurance')

for i, v in enumerate(sizes):
    plt.text(y_pos[i] , v + 0.01, str(round(v, 2)))
    
plt.savefig('industry5.png', bbox_inches="tight", transparent = False)
plt.show()


       


# # Industry Reviews:

# In[44]:


#Part A
df_industry_count = df_company.groupby(['Company_Industry']).count()
df_industry_count = df_industry_count[['Company']]

df_industry_count = df_industry_count.reset_index()
df_industry_count.head()


# In[45]:


#Part B
df_industry_mean = df_company.groupby(['Company_Industry']).mean()
df_industry_mean.reset_index(inplace=True)
df_industry_mean.head().round(2)


# In[43]:


#Merge between A+B
df_company_sort = df_industry_mean.merge(df_industry_count).sort_values(['Company'],ascending=False)
df_company_sort.reset_index(inplace=True)
df_company_sort.head().round(2)


# In[46]:


df_company['No_of_Stars'].describe()


# In[41]:


#27.95% corr between the # of job postings and the average star rating 
import seaborn as sns
data2 = df_company_sort
corr = data2.corr()
corr

