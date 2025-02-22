# Importamos las bibliotecas necesarias
import pandas as pd  # Para manipulación y análisis de datos
import numpy as np  # Para cálculos estadísticos y matemáticos
import matplotlib.pyplot as plt  # Para generar gráficos
import seaborn as sns  # Para visualizaciones más atractivas

# Creamos un diccionario con los datos de los estudiantes
data = {
    "Estudiante": [f"Estudiante {i}" for i in range(1, 31)],  # Nombres de los estudiantes
    "Nota": [78, 85, 90, 45, 88, 92, 60, 72, 50, 95, 80, 83, 77, 55, 89, 91, 68, 74, 63, 82, 
             97, 48, 93, 86, 79, 57, 71, 84, 66, 58],  # Notas de los estudiantes
    "Horas de Estudio": [6, 8, 10, 3, 9, 11, 4, 6, 3, 12, 7, 7, 5, 3, 10, 11, 5, 7, 4, 9, 
                         12, 2, 10, 8, 7, 4, 6, 8, 5, 3]  # Horas que cada estudiante estudió
}

# Convertimos el diccionario en un DataFrame de pandas
df = pd.DataFrame(data)

# Mostramos los primeros 5 registros del DataFrame
print(df.head())

# Cálculo de medidas estadísticas básicas
print("Media:", np.mean(df["Nota"]))  # Calculamos la media de las notas
print("Mediana:", np.median(df["Nota"]))  # Calculamos la mediana de las notas
print("Cuartiles:")
print(np.percentile(df["Nota"], [25, 50, 75]))  # Calculamos los cuartiles (Q1, Q2, Q3)

# Detección de valores atípicos utilizando el rango intercuartílico (IQR)
Q1, Q3 = np.percentile(df["Nota"], [25, 75])  # Calculamos el primer y tercer cuartil
IQR = Q3 - Q1  # Calculamos el rango intercuartílico (IQR)
limite_inferior = Q1 - 1.5 * IQR  # Definimos el límite inferior para valores atípicos
limite_superior = Q3 + 1.5 * IQR  # Definimos el límite superior para valores atípicos

# Filtramos y mostramos los valores atípicos en las notas
print(f"Valores atípicos: {df[(df['Nota'] < limite_inferior) | (df['Nota'] > limite_superior)]['Nota'].values}")

# Generamos un histograma para visualizar la distribución de las notas
plt.hist(df["Nota"], bins=10, color="skyblue", edgecolor="black")
plt.title("Distribución de Notas")
plt.xlabel("Notas")
plt.ylabel("Frecuencia")
plt.show()

# (Esta línea está duplicada, por lo que podríamos eliminarla)
plt.hist(df["Nota"], bins=10, color="skyblue", edgecolor="black")
plt.title("Distribución de Notas")
plt.xlabel("Notas")
plt.ylabel("Frecuencia")
plt.show()

# Creamos un gráfico de dispersión para visualizar la relación entre las horas de estudio y las notas obtenidas
plt.scatter(df["Horas de Estudio"], df["Nota"], color="red")
plt.title("Relación entre Notas y Horas de Estudio")
plt.xlabel("Horas de Estudio")
plt.ylabel("Nota")
plt.show()
