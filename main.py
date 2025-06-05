import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# ----------------------------------------------------------
# PARTE 1 – Função temperatura(m): Evolução da temperatura ao longo dos meses
# Fórmula: temperatura(m) = 35 + (1 - e^(-m/27)) + m * e^(-34.33m)
# ----------------------------------------------------------
 
# Listas para armazenar os valores
tempo_meses = []
valores_temperatura = []
 
# Usando while
mes = 1
while mes <= 36:
    temperatura = 35 + (1 - np.exp(-mes / 27)) + mes * np.exp(-34.33 * mes)
    tempo_meses.append(mes)
    valores_temperatura.append(temperatura)
    mes += 1
 
# Criação do DataFrame
df_temperatura = pd.DataFrame({'Mes': tempo_meses, 'Temperatura': valores_temperatura})
 
# Exibição dos valores mínimo e máximo
print("Temperatura minima registrada:")
print(df_temperatura[df_temperatura['Temperatura'] == df_temperatura['Temperatura'].min()])
print("Temperatura maxima registrada:")
print(df_temperatura[df_temperatura['Temperatura'] == df_temperatura['Temperatura'].max()])
 
# Gráfico da função temperatura(m)
plt.figure(figsize=(10, 5))
plt.plot(df_temperatura['Mes'], df_temperatura['Temperatura'], marker='o', linestyle='-', color='red', label='Temperatura(m)')
plt.title('Evolucao da Temperatura ao longo dos Meses')
plt.xlabel('Meses')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
 
# ----------------------------------------------------------
# PARTE 2 – Função e(x): Escala Richter em função da velocidade
# Fórmula: e(x) = 5.47 + 1.85 * e^(-v) * cos(√8 * v - 19.47) + (v - 1.365) * e^(-34.33 * v)
# ----------------------------------------------------------
 
# Geração dos valores de velocidade entre 0 e 5 m/s
x = np.linspace(0, 5, 1000)
 
# Cálculo da função e(x)
e = ( 5.47 + 1.85 * np.exp(-x) * np.cos(np.sqrt(8) * x - 19.47) +(x - 1.365) * np.exp(-34.33 * x))
 
# DataFrame com os resultados
df_escala_richter = pd.DataFrame({'Velocidade (m/s)': x, 'Escala Richter': e})
 
# Exibição dos valores mínimo e máximo
print("Escala Richter minima registrada:")
print("Minimo:", df_escala_richter['Escala Richter'].min())
print("Escala Richter maxima registrada:")
print("Maximo:", df_escala_richter['Escala Richter'].max())
 
# Gráfico da função e(x)
plt.figure(figsize=(10, 5))
plt.plot(df_escala_richter['Velocidade (m/s)'], df_escala_richter['Escala Richter'], color='purple', label='Escala Richter(x)')
plt.title('Escala Richter em função da Velocidade')
plt.xlabel('Velocidade (m/s)')
plt.ylabel('Escala Richter')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()