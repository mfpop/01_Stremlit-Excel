import pandas as pd
import streamlit as st

#df=pd.read_excel(    'data.xlsx',    sheet_name='Sheet1',    header=0)

st.set_page_config(page_title='Dashboard', page_icon=':bar_chart:', layout='wide')

st.title('Dashboard')
         
#create sidebar table with filters and data columns

st.sidebar.title('Filter by:') 

category = st.sidebar.multiselect('Category', ['A', 'B', 'C'], default=['A', 'B', 'C'])
