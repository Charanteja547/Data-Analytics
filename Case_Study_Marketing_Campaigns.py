#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis - Marketing Campaigns Analysis
# 
# In this notebook we will explore how to perform **Non Visual** as well as **Visual Analysis** on the Marketing Dataset. 
# 
# ## Getting Started
# 
# **About the Use Case**  
# Consider a well-established company operating in the retail food sector. Presently they have around several hundred thousands of registered customers and serve almost one million consumers a year. They sell products from 5 major categories: wines, rare meat products, exotic fruits, specially prepared fish and sweet products. These can further be divided into gold and regular products. The customers can order and acquire products through 3 sales channels: physical stores, catalogs and the company's website. Globally, the company had solid revenues and a healthy bottom line in the past 3 years, but the profit growth perspectives for the next 3 years are not promising... For this reason, several strategic initiatives are being considered to reverse this situation. One is to improve the performance of marketing activities, with a special focus on marketing campaigns.
# 
# 
# **The Marketing Department**  
# The marketing department was pressured to spend its annual budget more wisely. The CMO perceives the importance of having a more quantitative approach when making decisions, the reason why a small team of data scientists was hired with a clear objective in mind: to build a predictive model which will support direct marketing initiatives. Desirably, the success of these activities will prove the value of the approach and convince the more skeptical within the company.
# 
# **The Objective**  
# The objective of the team is to build a predictive model that will produce the highest profit for the next direct marketing campaign, scheduled for the next month. The new campaign, sixth, aims at selling a new gadget to the Customer Database. 
# 
# To build the model, a pilot campaign involving 2240 customers was carried out. The customers were selected at random and contacted by phone regarding the acquisition of the gadget. During the following months, customers who bought the offer were properly labeled. The total cost of the sample campaign was 6720MU and the revenue generated by the customers who accepted the offer was 3674MU. Globally the campaign had a profit of -3046MU. The success rate of the campaign was 15%. 
# 
# The objective of the team is to develop a model that predicts customer behavior and to apply it to the rest of the customer base. Hopefully the model will allow the company to cherry pick the customers that are most likely to purchase the offer while leaving out the non-respondents, making the next campaign highly profitable. Moreover, other than maximizing the profit of the campaign, the CMO is interested in understanding to study the characteristic features of those customers who are willing to buy the gadget.
# 
# 
# **Objectives**   
# 
# Key Objectives are: 
# 1. Explore the data – be creative and pay attention to the details. You need to provide the marketing team a better understanding of the characteristic features of respondents; 
# 2. Propose and describe a customer segmentation based on customers behaviors; 
# 3. Create a predictive model which allows the company to maximize the profit of the next marketing campaign.
# 4. Whatever else you think is necessary.
# 
# **The Data Dictionary**  
# The data set contains socio-demographic and firmographic features about 2240 customers who were contacted. Additionally, it contains a flag for those customers who responded to the campaign, by buying the product.
# <img height="400" width="400" src="data/marketing_data_dictionary.png">
# 
# 
# **Are you getting confused from the above problem statement? 🤯😰**
# 
# Don’t worry. I have compiled the major takeaways in a more informative and easily to understand manner. Kindly go through the following carefully.
# 
# <a href="https://docs.google.com/document/d/1ufcHX6SNkk6e9J2i15tUH3CINxGK5VjwsSLILRxPcUM/edit?usp=sharing">Click here</a> to get the Domain Knowledge Documentation.
# 

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


PATH = "data/marketing_data.csv"

df = pd.read_csv(PATH)

df.head()


# In[3]:


df.shape


# In[4]:


df.columns


# ### Renaming the Columns

# In[5]:


df.columns = df.columns.str.strip()

df.columns


# ### Fixing the Data Types of Columns

# In[6]:


df.info()


# In[7]:


df['Income'] = df['Income'].str.strip().str.replace('$', '', regex=False).str.replace(',', '', regex=False)

df['Income'] = df['Income'].astype('float')


# In[8]:


df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])

df.info()


# # Steps Involved in Exploratory Data Analysis
# 
# 1. **Univariate Analysis**  
#   A. Discrete Data (i.e. Categorical or Numerical Discrete Columns)
#     - Statistical Non Visual Analysis
# 		- Purpose: Helps us describe and summarize the data
# 		- count, nunique, unique, value_counts
# 	- Visual Analysis
# 		- Purpose: Helps us understand how the data is distributed and Outliers
# 		- Bar/Count Plot   
# 
#   B. Continuous Numerical Data (i.e. Real Numerical)
#     - Statistical Non Visual Analysis
# 		- Purpose: Helps us describe and summarize the data
# 		- min, max, sum, mean, median, var, std, range, iqr
# 	- Visual Analysis
# 		- Purpose: Helps us understand the Distribution of data and Outliers
# 		- Histogram Plot, KDE Plot and Box Plot
# 
# 2. **Bivariate Analysis (Purpose - Helps identify the relationships)**  
#   A. Continuous Numerical vs Continuous Numerical Data
#     - Statistical Non Visual Analysis
# 		- Purpose: Is there any relationship between two variables - Linear or non Linear relationship?
# 		- Pearson Correlation Coefficient
# 	- Visual Analysis
# 		- Scatter Plot
# 
#   B. Continuous Numerical vs Discrete Data
#     - Statistical Non Visual Analysis
# 		- Purpose: How many discrete groups are there and Are the individuals in the groups independent or dependent?
# 		- Compare the Mean, Median, Std of the groups
# 	- Visual Analysis
# 		- Box Plots and Histogram Plots
# 
#   C. Discrete vs Discrete Data
#     - Statistical Non Visual Analysis
# 		- Purpose: Are the individuals in the groups independent or dependent?
# 		- Cross Tabs (i.e. Frequency Tables)
# 	- Visual Analysis
# 		- Stacked Bar Plot, Unstacked Bar Plot

# ### 1. Univariate Analysis - Statistical Non Visual Analysis

# In[9]:


discrete_df = df.select_dtypes(include=['object'])

numerical_df = df.select_dtypes(include=['int64', 'float64'])


# In[10]:


def discrete_univariate_analysis(discrete_data):
    for col_name in discrete_data:
        print("*"*10, col_name, "*"*10)
        print(discrete_data[col_name].agg(['count', 'nunique', 'unique']))
        print('Value Counts: \n', discrete_data[col_name].value_counts())
        print()


# In[11]:


discrete_univariate_analysis(discrete_df)


# In[12]:


def numerical_univariate_analysis(numerical_data):
    for col_name in numerical_data:
        print("*"*10, col_name, "*"*10)
        print(numerical_data[col_name].agg(['min', 'max', 'mean', 'median', 'std']))
        print()


# In[13]:


numerical_univariate_analysis(numerical_df)


# In[14]:


numerical_df.columns


# In[15]:


discrete_num_cols = ['ID', 'Year_Birth', 'Kidhome', 'Teenhome',
                   'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',
                   'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2',
                   'Response', 'Complain']
numerical_df.drop(columns=discrete_num_cols, axis=1, inplace=True)

print('Shape:', numerical_df.shape)
print('Columns:', numerical_df.columns)


# In[16]:


discrete_num_df = df[discrete_num_cols]

print('Shape:', discrete_num_df.shape)
print('Columns:', discrete_num_df.columns)


# In[17]:


discrete_num_df = discrete_num_df.drop(columns=['ID'], axis=1)

print('Shape:', discrete_num_df.shape)
print('Columns:', list(discrete_num_df.columns))


# In[18]:


numerical_univariate_analysis(numerical_df)


# In[19]:


discrete_univariate_analysis(discrete_df)


# In[20]:


discrete_univariate_analysis(discrete_num_df)


# In[21]:


df[discrete_num_cols] = df[discrete_num_cols].astype('object')

df.info()


# ### 2. Univariate - Visual Analysis

# In[22]:


df.shape


# In[23]:


df.plot(kind='hist', subplots=True, layout=(4, 2), figsize=(10, 10))


# In[24]:


df.plot(kind='box', subplots=True, layout=(4, 2), figsize=(10, 10))


# In[25]:


df = df.loc[df['Income'] < 100000]

df.shape


# In[26]:


df = df.loc[(df['MntMeatProducts'] < 1000)]

df.shape


# In[27]:


df = df.loc[(df['MntSweetProducts'] < 200)]

df.shape


# In[28]:


df = df.loc[(df['MntGoldProds'] < 250)]

df.shape


# ## 3. Bivariate Analysis

# ### a. Continuous vs Continuous Numerical Data

# In[29]:


df.columns


# In[31]:


df.corr()


# In[33]:


df.plot(kind='scatter', x='Income', y='MntWines', figsize=(4, 4))


# In[34]:


df.plot(kind='scatter', x='Income', y='MntMeatProducts', figsize=(4, 4))


# ### b. Discrete vs Discrete Data

# In[35]:


df.columns


# In[36]:


pd.crosstab(df['Marital_Status'], df['Response'])


# In[37]:


pd.crosstab(df['Marital_Status'], df['Response'], normalize=True)


# In[38]:


pd.crosstab(df['Marital_Status'], df['Response'], normalize='index')


# In[39]:


pd.crosstab(df['Marital_Status'], df['Response'], normalize='index', margins=True)


# In[40]:


pd.crosstab(df['Marital_Status'], df['Response'], normalize='columns')


# In[41]:


pd.crosstab(df['Marital_Status'], df['Response'], normalize='columns', margins=True)


# In[42]:


tab = pd.crosstab(df['Marital_Status'], df['Response'], normalize='index')

tab.plot(kind='bar')


# In[43]:


tab.plot(kind='barh', stacked=True)


# ### c. Continuous Numerical vs Discrete Data

# In[44]:


df.columns


# In[45]:


df.info()


# In[46]:


group = df.groupby('Marital_Status')

group['Income'].agg(['min', 'max', 'mean', 'median'])


# In[47]:


df.boxplot(by='Marital_Status', column='Income')

