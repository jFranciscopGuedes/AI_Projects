import streamlit as st       # Importa o Streamlit para criar a interface web
import joblib                # Importa joblib para carregar o modelo treinado
import numpy as np           # Importa NumPy (útil para manipular arrays numéricos)

modelo = joblib.load('modelo_tsunami.pkl')  # Carrega o modelo treinado salvo no ficheiro .pkl

st.title("Previsor de Tsunami")  # Define o título da aplicação no topo da página

campos = ['Magnitude','CDI','MMI','SIG','NST','DMIN','GAP','DEPTH','LAT','LONG']  # Lista com os nomes das features usadas pelo modelo
valores = []  # Lista onde serão guardados os valores inseridos pelo utilizador

for c in campos:                               # Itera sobre cada nome de variável
    val = st.number_input(f"{c}:", step=0.01)  # Cria uma caixa numérica para inserir o valor da variável
    valores.append(val)                        # Guarda o valor introduzido na lista 'valores'

if st.button("Prever"):                  # Cria um botão que executa o código dentro quando clicado
    pred = modelo.predict([valores])[0]  # O modelo devolve um array com uma previsão (ex: [1]); 
                                         #[0] serve para extrair o único valor (1 ou 0) dessa lista
    if pred == 1:
        st.error("Tsunami provável 🌊")   # Mostra mensagem vermelha se o modelo prever tsunami
    else:
        st.success("Sem tsunami ✅")       # Mostra mensagem verde se o modelo prever ausência de tsunami


#Para correr -> streamlit run prever_tsunami_streamlib.py