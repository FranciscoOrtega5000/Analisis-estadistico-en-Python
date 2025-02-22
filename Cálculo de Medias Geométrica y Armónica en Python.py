# Importamos la biblioteca numpy para realizar cálculos matemáticos
import numpy as np  

# Definimos una lista de datos
datos = [2, 4, 3]  

# Calculamos la media geométrica: 
# Se obtiene multiplicando todos los valores y luego extrayendo la raíz enésima (según el número de valores)
media_geometrica = np.prod(datos)**(1/len(datos))

# Calculamos la media armónica:
# Se obtiene dividiendo el número total de valores entre la suma de los inversos de cada valor
media_armonica = len(datos) / sum(1/x for x in datos)

# Imprimimos los resultados en la consola
print(f"Media Geometrica: {media_geometrica}")
print(f"Media Armonica: {media_armonica}")
