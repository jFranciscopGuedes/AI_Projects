import streamlit as st
import joblib
import numpy as np

modelo = joblib.load('modelo_tsunami.pkl')

st.title("Previsor de Tsunami")

campos = ['Magnitude','CDI','MMI','SIG','NST','DMIN','GAP','DEPTH','LAT','LONG']
valores = []

for c in campos:
    val = st.number_input(f"{c}:", step=0.01)
    valores.append(val)

if st.button("Prever"):
    pred = modelo.predict([valores])[0]
    if pred == 1:
        st.error("Tsunami provável 🌊")
    else:
        st.success("Sem tsunami ✅")
