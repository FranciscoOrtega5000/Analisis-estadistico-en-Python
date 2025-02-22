# Importamos la biblioteca numpy para realizar cálculos matemáticos
import numpy as np  

# Definimos una lista de datos numéricos
datos = [12, 15, 17, 20]  

# Calculamos el rango (diferencia entre el valor máximo y mínimo)
rango = max(datos) - min(datos)

# Calculamos la varianza (mide la dispersión de los datos respecto a la media)
varianza = np.var(datos)

# Calculamos la desviación estándar (raíz cuadrada de la varianza, mide la dispersión en la misma unidad de los datos)
desviacion_estandar = np.std(datos)

# Calculamos la media (promedio de los valores)
media = np.mean(datos)

# Calculamos el coeficiente de variación (CV), que mide la dispersión en términos relativos (%)
cv = (desviacion_estandar / media) * 100  

# Imprimimos los resultados en la consola
print(f"Rango: {rango}")  
print(f"Varianza: {varianza}")  
print(f"Desviacion Estandar: {desviacion_estandar}")  
print(f"Coeficiente de Variacion: {cv}")  
