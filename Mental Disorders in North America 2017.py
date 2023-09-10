#!/usr/bin/env python
# coding: utf-8

#Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('C:/Users/Dominga Genao/OneDrive/Escritorio/mental.csv')
# df = pd.DataFrame(df, columns=df.columns)
df = df.drop("index",axis=1)
df.info()

# Check the head and tail of the dataframe:
df
df.iloc[6467]

map_names = {'geometry': 'country',
             'Year' : 'year',
             'Schizophrenia (%)':'schizo', 
             'Bipolar disorder (%)':'bipolar',
             'Eating disorders (%)' : 'eds',
             'Anxiety disorders (%)' : 'anxiety',
             'Drug use disorders (%)':'drug',
             'Depression (%)':'depres',
             'Alcohol use disorders (%)':'alcohol'}

df.rename(columns=map_names,inplace=True)
df.head()

df.dropna(inplace=True)
df

df['year'] = pd.to_numeric(df['year'])
df['schizo'] = pd.to_numeric(df['schizo'])
df['bipolar'] = pd.to_numeric(df['bipolar'])
df['eds'] = pd.to_numeric(df['eds'])
df.info()

dom = df[df['Code'] == 'DOM']
dom.set_index('year')
dom

dom.plot(x='year', title = 'Prevalence of Various Mental Health Diagnosis in the DOM', xlabel = 'Year', ylabel = 'Prevalence (%)')


# Lista de paises de norte américa
countries_americas = ['Argentina', 'Brazil', 
                      'Canada', 'Mexico', 
                      'United States', 
                      'Colombia', 'Chile', 
                      'Peru', 'Venezuela', 
                      'Ecuador', 'Guatemala', 
                      'Cuba', 'Bolivia', 
                      'Dominican Republic', 
                      'Honduras', 'Paraguay', 
                      'El Salvador', 'Nicaragua', 
                      'Costa Rica', 'Puerto Rico', 
                      'Panama', 'Uruguay', 
                      'Jamaica', 'Trinidad and Tobago', 
                      'Guyana', 'Suriname', 
                      'French Guiana', 'Belize', 
                      'Barbados', 'Saint Lucia', 
                      'Grenada', 'Saint Vincent and the Grenadines', 
                      'Antigua and Barbuda', 'Saint Kitts and Nevis', 
                      'Bahamas', 'Turks and Caicos Islands', 
                      'British Virgin Islands', 
                      'Bermuda', 'Anguilla', 'Montserrat']


la = df[df['country'].isin(countries_americas)]
la = la[la['year'] == 2017]
la.head()


pip install plotly

import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True) 

# Schizophrenia
sch_data = dict(
        type = 'choropleth',
        colorscale = 'YlGnBu',
        reversescale = True,
        locations = la['country'],
        locationmode = "country names",
        z = la['schizo'],
        text = la['country'],
        colorbar = {'title' : 'Schizophrenia %'},
      ) 
sch_layout = dict(title = 'Prevalence of Schizophrenia in North America in 2017', 
              geo = dict({'scope':'north america'}, projection = {'type':'natural earth'}, showframe = True))


# Bipolar Disorder
bp_data = dict(
        type = 'choropleth',
        colorscale = 'YlGnBu',
        reversescale = True,
        locations = la['country'],
        locationmode = "country names",
        z = la['bipolar'],
        text = la['country'],
        colorbar = {'title' : 'Bipolar %'},
      ) 
bp_layout = dict(title = 'Prevalence of Bipolar Disorder in North America in 2017', 
              geo = dict({'scope':'north america'}, projection = {'type':'natural earth'}, showframe = True))


# Eating Disorders
ed_data = dict(
        type = 'choropleth',
        colorscale = 'YlGnBu',
        reversescale = True,
        locations = la['country'],
        locationmode = "country names",
        z = la['eds'],
        text = la['country'],
        colorbar = {'title' : 'EDs %'},
      ) 
ed_layout = dict(title = 'Prevalence of Eating Disorders in North America in 2017', 
              geo = dict({'scope':'north america'}, projection = {'type':'natural earth'}, showframe = True))


# Anxiety
anx_data = dict(
        type = 'choropleth',
        colorscale = 'YlGnBu',
        reversescale = True,
        locations = la['country'],
        locationmode = "country names",
        z = la['anxiety'],
        text = la['country'],
        colorbar = {'title' : 'Anxiety %'},
      ) 
anx_layout = dict(title = 'Prevalence of Anxiety Disorder in North America in 2017', 
              geo = dict({'scope':'north america'}, projection = {'type':'natural earth'}, showframe = True))


# Drug Abuse
d_data = dict(
        type = 'choropleth',
        colorscale = 'YlGnBu',
        reversescale = True,
        locations = la['country'],
        locationmode = "country names",
        z = la['drug'],
        text = la['country'],
        colorbar = {'title' : 'Drug Users %'},
      ) 
d_layout = dict(title = 'Prevalence of Drug Abuse in North America in 2017', 
              geo = dict({'scope':'north america'}, projection = {'type':'natural earth'}, showframe = True))



# Depression
dep_data = dict(
        type = 'choropleth',
        colorscale = 'YlGnBu',
        reversescale = True,
        locations = la['country'],
        locationmode = "country names",
        z = la['depres'],
        text = la['country'],
        colorbar = {'title' : 'Depression %'},
      ) 
dep_layout = dict(title = 'Prevalence of Depressive Disorder in Latin America in 2017', 
              geo = dict({'scope':'north america'}, projection = {'type':'natural earth'}, showframe = True))


# Alcohol Abuse
alc_data = dict(
        type = 'choropleth',
        colorscale = 'YlGnBu',
        reversescale = True,
        locations = la['country'],
        locationmode = "country names",
        z = la['alcohol'],
        text = la['country'],
        colorbar = {'title' : 'Alcohol Abuse %'},
      ) 
alc_layout = dict(title = 'Prevalence of Alcohol Abuse in North America in 2017', 
              geo = dict({'scope':'north america'}, projection = {'type':'natural earth'}, showframe = True))


go.Figure(data = [sch_data],layout = sch_layout) 
choromap = go.Figure(data = [sch_data],layout = sch_layout) 
iplot(choromap)

go.Figure(data = [ed_data],layout = ed_layout) 
choromap = go.Figure(data = [ed_data],layout = ed_layout) 
iplot(choromap)

go.Figure(data = [anx_data],layout = anx_layout) 
choromap = go.Figure(data = [anx_data],layout = anx_layout) 
iplot(choromap)

go.Figure(data = [d_data],layout = d_layout) 
choromap = go.Figure(data = [d_data],layout = d_layout) 
iplot(choromap)

go.Figure(data = [dep_data],layout = dep_layout) 
choromap = go.Figure(data = [dep_data],layout = dep_layout) 
iplot(choromap)

go.Figure(data = [alc_data],layout = alc_layout) 
choromap = go.Figure(data = [alc_data],layout = alc_layout) 
iplot(choromap)

go.Figure(data = [bp_data],layout = bp_layout) 
choromap = go.Figure(data = [bp_data],layout = bp_layout) 
iplot(choromap)

# Crear la matriz de correlación
matriz_correlacion = dfc[columnas_seleccionadas].corr()

# Mapa de calor utilizando Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()







# In[ ]:




