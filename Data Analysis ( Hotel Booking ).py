#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# # Loading the dataset

# In[7]:


df = pd.read_csv('hotel_booking.csv.csv')


# # Exploratory Data Analysis And Data Cleaning

# In[8]:


df.head()


# In[9]:


df.tail()


# In[10]:


df.shape


# In[11]:


df.columns


# In[12]:


df.info()


# In[13]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[14]:


df.info()


# In[15]:


df.describe(include = 'object')


# In[16]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[15]:


df.isnull().sum()


# In[17]:


df.drop(['company','agent'], axis = 1, inplace = True)
df.dropna(inplace = True)


# In[17]:


df.isnull().sum()


# In[18]:


df.describe()


# In[18]:


df['adr'].plot(kind = 'box')


# In[19]:


df = df[df['adr']<5000]


# In[20]:


df.describe()


# In[21]:


df = df[df['adr']<5000]


# # Data Analysis and Visualizations

# In[22]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
cancelled_perc

plt.figure(figsize = (5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(), edgecolor = 'k', width = 0.7)
plt.show()


# In[27]:


plt.figure(figsize = (8,4))
ax1= sns.countplot(x = 'hotel' , hue = 'is_canceled', data = df , palette = 'Blues')
legend_labels,_ = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status in different hotels', size = 20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()


# In[28]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[30]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[31]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[32]:


plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in city and Resort Hotel', fontsize = 30)
plt.plot(resort_hotel.index,resort_hotel['adr'],label = 'Resort Hotel')
plt.plot(city_hotel.index,city_hotel['adr'],label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[33]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))
ax1 = sns.countplot(x = 'month', hue = 'is_canceled',data = df,palette = 'bright')
legend_labels,_ = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor = (1,1))
plt.title('Reservation status per month', size = 20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()


# In[37]:


plt.figure(figsize=(15, 8))
plt.title('ADR per month', fontsize=30)
data = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index()
sns.barplot(x='month', y='adr', data=data)
plt.show()


# In[38]:


cancelled_data = df[df['is_canceled'] == 1 ]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('Top 10 countries with reservation cancelled')
plt.pie(top_10_country, autopct ='%.2f',labels = top_10_country.index)
plt.show()


# In[39]:


df['market_segment'].value_counts()


# In[40]:


df['market_segment'].value_counts(normalize = True )


# In[41]:


cancelled_data['market_segment'].value_counts(normalize = True )


# In[43]:


cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace = True )
cancelled_df_adr.sort_values('reservation_status_date',inplace = True )

not_cancelled_data = df[df['is_canceled'] == 0 ]
not_cancelled_df_adr = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace = True )
not_cancelled_df_adr.sort_values('reservation_status_date',inplace = True )

plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label = 'cancelled')
plt.legend()


# In[44]:


cancelled_df_adr = cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016') & (cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr = not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016') & (not_cancelled_df_adr['reservation_status_date']<'2017-09')]


# In[54]:


plt.figure(figsize = (20,6))
plt.title('Average Daily Rate',fontsize = 30)
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label = 'cancelled')
plt.legend(fontsize = 20)


# In[ ]:




