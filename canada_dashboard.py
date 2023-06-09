from lib2to3.pgen2.pgen import DFAState
import pandas as pd  #data load
import seaborn as sns # visualisation lib(graph)
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import numpy as np

@st.cache
def load_dataset():
    df=pd.read_excel('Canada.xlsx',
                 skiprows=20,
                 skipfooter=2,
                 sheet_name='Canada by Citizenship')
    df=preprocess(df)
    return df

def preprocess(df):
    #step 1
    cols_to_remove=['Type','Coverage','AREA','REG','DEV']
    df.drop(columns=cols_to_remove,inplace=True)

    #step 2
    df.rename({
    'OdName':'Country',
    'AreaName':'Continent',
    'RegName':'Region',
    'DevName':'Status',
    }, axis=1, inplace=True)

    #step 3
    df.columns=df.columns.astype(str)

    #step 4
    years=list(map(str,range(1980,2014)))
    df['Total']=df[years].sum(axis=1)

    #step 5
    df.set_index('Country', inplace=True)

    #step 6
    df.sort_values(by='Total',ascending=False, inplace=True) #descending is  by default

    #finally
    return df

#common list
years=list(map(str,range(1980,2014)))
df=load_dataset()

st.title('Canada Imigration Statistics')

if st.sidebar.checkbox('View the Raw Dataset'):
    st.dataframe(df)

country=st.selectbox('Select a Country',df.index.tolist())
year_start=st.sidebar.select_slider('Select Start Year',years)
year_end=st.sidebar.select_slider('Select End Year',years,value=years[-1])

graph_options=['line','bar','area']
graph_type=st.sidebar.radio('Select Graph Type',graph_options)

#plot graph
if st.sidebar.checkbox('Show Country Wise Data'):
    st.subheader(f'{country}')
    year_range=list(map(str,range(int(year_start),int(year_end)+1)))
    data=df.loc[country,year_range]
    if graph_type==graph_options[0]:
        fig=px.line(data, x=data.index, y=country)
    elif graph_type==graph_options[1]:
        fig=px.bar(data, x=data.index, y=country)
    elif graph_type==graph_options[2]:
        fig=px.area(data, x=data.index, y=country)
    st.plotly_chart(fig)

    

