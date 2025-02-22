# Importamos las bibliotecas necesarias
import numpy as np  # Para cálculos matemáticos y estadísticos
from scipy import stats  # Para cálculos estadísticos adicionales

# Definimos una lista de datos numéricos
datos = [8, 10, 10, 15, 20, 25, 30]  

# Calculamos la media (promedio de los valores)
media = np.mean(datos)

# Calculamos la mediana (valor central cuando los datos están ordenados)
mediana = np.median(datos)

# Calculamos la moda (el valor que más se repite)
moda = stats.mode(datos, keepdims=True)  # keepdims=True es necesario en versiones recientes de SciPy

# Imprimimos los resultados
print(f"Media: {media}, Mediana: {mediana}, Moda: {moda.mode[0]}")
