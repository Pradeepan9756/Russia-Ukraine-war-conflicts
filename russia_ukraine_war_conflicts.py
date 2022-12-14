# -*- coding: utf-8 -*-
"""RUSSIA UKRAINE WAR CONFLICTS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x5iejmS_d_JtQXjFHElBJVm7m40i1hJy

import necessary libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import plotly.express as px
import warnings
!pip install country_converter
import country_converter 
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os
WIDTH= 850
for dirname, _,filenames in os.walk('/kaggle/input/'):
  for filename in filenames:
    print(os.path.join(dirname,filename))
warnings.filterwarnings('ignore')

df = pd.read_csv('/content/UKR_refugee_by_countries.csv',index_col=0)
df.head()

df.rename(columns = {'lan_min':'lat_min'},inplace=True)
df.head()

df['country_ISO3'] = country_converter.convert(df['country'],to='ISO3')

df.head()

"""Investigating the datasets """

df.info()

df.describe()

plt.title('Distribution of data sources')
sns.histplot(df['source'], kde=False)
plt.show()

def unique_values(cols):
  for col in cols:
    print('the unique values '+ col +'are:')
    print(df[col].unique())

cols = ['country','centroid_lon','centroid_lat','lat_min','lon_min']
unique_values(cols)

df.groupby('country')[['centroid_lon','centroid_lat','lat_min','lon_min']].agg([max,min])

#let see which country hold more refugees
df_max = df.groupby('country_ISO3')[['individuals']].max().sort_values('individuals', ascending =False)
fig_bar = px.bar(x = df_max.index, y = df_max.individuals, color = df_max.individuals, color_continuous_scale='dense')
fig_bar.update_layout(width = WIDTH, height =500, title_text = 'TOP countries by Refugees')
fig_bar.update_xaxes(title = 'country')
fig_bar.update_yaxes(title = 'Refugees in M')
fig_bar.show()

#Lets add ukraine to the dataset for better visualizion:
df.loc[len(df.index)] = ['Ukraine_2022-9-14', 'Ukraine', 2022-9-14, 43158862,31.1656,48.3794,0,0,0,0,'0','UKR']
df.tail()

df_max = df.groupby('country_ISO3')[['individuals']].max().sort_values('individuals', ascending= False)
fig = px.choropleth(locations = df_max.index,
                    color =df_max['individuals'],
                    color_continuous_scale='matter',
                    title ='individuals by Location')


fig.update_layout(width = WIDTH, height = 600, title_text = 'Refugees by country world map')
fig.show()