import streamlit as st
import pandas as pd

st.title("🚶‍♂️ Obesity Dataset Explorer")

# Load dataset
df = pd.read_csv('ObesityDataSet.csv')

st.write("### Preview Data:")
st.dataframe(df.head())

# Tambahan fitur (opsional)
if st.checkbox("Tampilkan info dataframe"):
    buffer = []
    df.info(buf=buffer)
    s = '\n'.join(map(str, buffer))
    st.text(s)

st.write("### Statistik Deskriptif:")
st.write(df.describe())
