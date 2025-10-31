import tkinter as tk          # Importa o módulo Tkinter para criar a interface gráfica (GUI)
import joblib                 # Importa joblib para carregar o modelo treinado salvo
import numpy as np            # Importa NumPy (usado para lidar com arrays numéricos, se necessário)

modelo = joblib.load('modelo_tsunami.pkl')  # Carrega o modelo treinado a partir do ficheiro .pkl

def prever():                                     # Define a função chamada quando o utilizador clica em "Prever"
    valores = [float(e.get()) for e in entradas]  # Lê todos os valores inseridos nas caixas de texto e converte para float
    y = modelo.predict([valores])[0]              # Usa o modelo para prever; [0] extrai o valor único (0=sem tsunami, 1=tsunami)
    saida['text'] = "Tsunami" if y == 1 else "Sem tsunami"  # Mostra o resultado na interface

janela = tk.Tk()                     # Cria a janela principal da aplicação
janela.title("Previsor de Tsunami")  # Define o título da janela

campos = ['Magnitude','CDI','MMI','SIG','NST','DMIN','GAP','DEPTH','LAT','LONG']  # Lista com os nomes das variáveis de entrada
entradas = []  # Lista onde serão guardadas as caixas de texto (inputs)

for c in campos:                        # Para cada nome de variável na lista
    tk.Label(janela, text=c).pack()     # Cria um rótulo (texto) com o nome da variável
    e = tk.Entry(janela)                # Cria uma caixa de entrada (campo de texto)
    e.pack()                            # Adiciona a caixa de texto à janela
    entradas.append(e)                  # Guarda a caixa na lista 'entradas' para leitura posterior

tk.Button(janela, text="Prever", command=prever).pack()  # Cria o botão "Prever" que executa a função 'prever' ao clicar
saida = tk.Label(janela, text="")       # Cria um rótulo vazio onde será exibido o resultado da previsão
saida.pack()                            # Adiciona o rótulo à janela

janela.mainloop()  # Inicia o loop principal do Tkinter; mantém a janela aberta e à espera de interações


#Para correr -> python prever_tsunami_gui.py