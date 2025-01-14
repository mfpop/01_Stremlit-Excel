import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_excel('Etiquetas.xlsx')

st.set_page_config(page_title='Dashboard', page_icon=':bar_chart:', layout='wide')
 
st.write("""   ## Production dashboard    """)
st.write("""   ### Efficiency    """)

         
#create sidebar table with filters and data columns

st.sidebar.title('Filter by:') 
