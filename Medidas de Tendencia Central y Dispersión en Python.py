# Importamos las librerías necesarias
import numpy as np  # Para cálculos matemáticos y estadísticos
from scipy import stats  # Para cálculos estadísticos adicionales

# Definimos la lista de datos con valores numéricos
datos = [7500, 8200, 9100, 8800, 9400, 7600, 8100, 8700, 9600, 
         7500, 8200, 9100, 8800, 9400, 7600, 8100, 8700, 9600, 
         7500, 8200, 9100, 8800, 9400, 7600, 8100, 8700, 9600]

# Calculamos la media (promedio)
media = np.mean(datos)

# Calculamos la mediana (valor central de los datos ordenados)
mediana = np.median(datos)

# Calculamos la moda (el valor que más se repite en la muestra)
moda = stats.mode(datos, keepdims=True)  # keepdims=True es necesario en versiones recientes de SciPy

# Calculamos la media geométrica usando el producto de todos los elementos elevado a la inversa del número de elementos
media_geometrica = np.prod(datos)**(1/len(datos))

# Calculamos la media armónica como el número total de elementos dividido por la suma de los inversos de cada valor
media_armonica = len(datos) / sum(1/x for x in datos)

# Calculamos la desviación estándar (mide la dispersión de los datos respecto a la media)
desviacion_estandar = np.std(datos)

# Calculamos la varianza (la desviación estándar al cuadrado)
varianza = np.var(datos)

# Calculamos el coeficiente de variación (mide la dispersión en relación con la media, expresado en %)
cv = (desviacion_estandar / media) * 100

# Imprimimos los resultados en la consola
print(f"Media: {media}, Mediana: {mediana}, Moda: {moda.mode[0]}")
#print(f"Media Geometrica:: {media_geometrica}")  # Descomentarlo si se desea mostrar
#print(f"Media Armonica:: {media_armonica}")  # Descomentarlo si se desea mostrar
print(f"Desviacion Estandar: {desviacion_estandar}")
print(f"Varianza: {varianza}")
print(f"Coeficiente de Variacion: {cv}")
