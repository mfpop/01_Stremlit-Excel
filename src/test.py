from rich import traceback
import streamlit as st
import pandas as pd
# import sqlite3
from pathlib import Path
traceback.install()





src_path = Path(__file__).parent
app_path = src_path / ".."
app_path = app_path.resolve()


# # Connect to the database
# conn = sqlite3.connect('../database/your_database_file.db')
# c = conn.cursor()

# Streamlit app
st.title("Production Dashboard")

# # Example query
# c.execute('SELECT * FROM your_table')
# data = c.fetchall()

# # Display data from the database
# st.write("Database Data:")
# st.write(data)

# Read and display Excel file

# excel_file_path = Path(__file__).parent / "excel_files"/ "Etiquetas.xlsx"
excel_path = app_path.resolve() / "excel_files"
etiquetas_path = excel_path / "Etiquetas.csv"

df = pd.read_csv(etiquetas_path.resolve())

st.write("Excel Data:")
st.write("app path: ", app_path)
st.write("src path: ", src_path)
st.write("excel path: ", excel_path)
st.write("etiquetas path: ", etiquetas_path)
st.write(df)

# Close the connection
# conn.close()
