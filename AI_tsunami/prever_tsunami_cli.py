import joblib
import numpy as np

# Carregar o modelo salvo
modelo = joblib.load('modelo_tsunami.pkl')

# Inserir valores manualmente (features)
dados = np.array([[7.0, 8, 6, 900, 300, 0.5, 20, 25, 10.5, -80.3]])

# Fazer previsão
resultado = modelo.predict(dados)[0]

# Mostrar saída
print("Provável tsunami" if resultado == 1 else "Sem tsunami previsto")

#Para correr -> python prever_tsunami_cli.py   