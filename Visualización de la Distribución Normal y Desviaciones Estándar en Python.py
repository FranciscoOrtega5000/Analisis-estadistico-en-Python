# Importamos las bibliotecas necesarias
import numpy as np  # Para cálculos matemáticos y estadísticos
import matplotlib.pyplot as plt  # Para generar gráficos
from scipy.stats import norm  # Para calcular la distribución normal

# Definimos una lista de datos
datos = [50, 52, 54, 56, 58, 60, 62]  

# Calculamos la media y la desviación estándar de los datos
media = np.mean(datos)
desviacion_estandar = np.std(datos)

# Filtramos los valores dentro de 1, 2 y 3 desviaciones estándar de la media
rango_1 = [X for X in datos if media - desviacion_estandar <= X <= media + desviacion_estandar]
rango_2 = [X for X in datos if media - 2*desviacion_estandar <= X <= media + 2*desviacion_estandar]
rango_3 = [X for X in datos if media - 3*desviacion_estandar <= X <= media + 3*desviacion_estandar]

# Mostramos los resultados en la consola
print(f"Media: {media}")
print(f"Valores en 1 desviación estándar: {rango_1}")
print(f"Valores en 2 desviaciones estándar: {rango_2}")
print(f"Valores en 3 desviaciones estándar: {rango_3}")

# Creamos un rango de valores para graficar la curva de Gauss
x = np.linspace(min(datos) - 10, max(datos) + 10, 500)  # Valores en el eje X
y = norm.pdf(x, media, desviacion_estandar)  # Calculamos la densidad de probabilidad de la distribución normal

# Configuramos la figura del gráfico
plt.figure(figsize=(10, 6))

# Graficamos la curva de distribución normal
plt.plot(x, y, label='Curva de Gauss', color='blue')

# Representamos los datos originales con puntos rojos
plt.scatter(datos, [0]*len(datos), color='red', label='Datos originales')

# Línea vertical en la media
plt.axvline(media, color='green', linestyle='--', label='Media')

# Sombras para representar las desviaciones estándar
plt.fill_between(x, 0, y, where=(x >= media - desviacion_estandar) & (x <= media + desviacion_estandar),
                 color='yellow', alpha=0.3, label='1 desviación estándar')
plt.fill_between(x, 0, y, where=(x >= media - 2*desviacion_estandar) & (x <= media + 2*desviacion_estandar),
                 color='orange', alpha=0.2, label='2 desviaciones estándar')
plt.fill_between(x, 0, y, where=(x >= media - 3*desviacion_estandar) & (x <= media + 3*desviacion_estandar),
                 color='red', alpha=0.1, label='3 desviaciones estándar')

# Configuración final del gráfico
plt.title("Curva de Gauss y datos")
plt.xlabel("Valores")
plt.ylabel("Densidad de probabilidad")
plt.legend()  # Agregamos leyenda
plt.grid()  # Mostramos la cuadrícula
plt.show()  # Mostramos el gráfico
