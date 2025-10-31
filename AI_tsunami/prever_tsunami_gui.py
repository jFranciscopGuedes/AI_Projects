import tkinter as tk
import joblib
import numpy as np

modelo = joblib.load('modelo_tsunami.pkl')

def prever():
    valores = [float(e.get()) for e in entradas]
    y = modelo.predict([valores])[0]
    saida['text'] = "Tsunami" if y == 1 else "Sem tsunami"

janela = tk.Tk()
janela.title("Previsor de Tsunami")

campos = ['Magnitude','CDI','MMI','SIG','NST','DMIN','GAP','DEPTH','LAT','LONG']
entradas = []

for c in campos:
    tk.Label(janela, text=c).pack()
    e = tk.Entry(janela)
    e.pack()
    entradas.append(e)

tk.Button(janela, text="Prever", command=prever).pack()
saida = tk.Label(janela, text="")
saida.pack()

janela.mainloop()
