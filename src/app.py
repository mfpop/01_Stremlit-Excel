# core Pkgs
from pathlib import Path
import streamlit as st

# Additional Pkgs
import pandas as pd

# Functions

def main():
   """All your code goes here"""
   
   df=pd.read_csv("Etiquetas.csv")
  # st.dataframe(df.style.highlight_max())
   status=st.radio("What is your status?",("active", "inactive"))
   if status=='active':
      st.success("you are active")
   elif status=="inactive":
      st.warning("you are inactive")     
      
      
   value = st.slider('Select a value:', 0, 100, 50)
   st.write('You selected:', value)

      
      
   pass

if __name__== '__main__':
   main()
   
