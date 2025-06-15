import streamlit as st
import pandas as pd
import io

st.title("🚶‍♂️ Obesity Dataset Explorer")

# Load dataset
df = pd.read_csv('ObesityDataSet.csv')  # Pastikan nama file ini sesuai

st.write("### Preview Data:")
st.dataframe(df.head())

if st.checkbox("Tampilkan info dataframe"):
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

st.write("### Statistik Deskriptif:")
st.write(df.describe())
