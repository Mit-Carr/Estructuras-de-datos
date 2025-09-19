import numpy as np
import pandas as pd
import time # 1. Importamos la librería time

# --- Parámetros iniciales ---
num_alumnos = 500
num_materias = 5

#==================================================================
# 1. Generar los datos base con NumPy
#==================================================================
### INICIA CRONÓMETRO 1 ###
inicio_numpy = time.time()

# Generamos la matriz de calificaciones
datos_calificaciones = np.random.randint(5, 11, size=(num_alumnos, num_materias))

### TERMINA CRONÓMETRO 1 ###
fin_numpy = time.time()
tiempo_numpy = fin_numpy - inicio_numpy


#==================================================================
# 2. Crear un DataFrame de Pandas
#==================================================================
### INICIA CRONÓMETRO 2 ###
inicio_df = time.time()

# Creamos etiquetas para las filas (índice) y las columnas
indice_alumnos = [f'Alumno_{i+1}' for i in range(num_alumnos)]
nombres_materias = [f'Materia_{i+1}' for i in range(num_materias)]

# Creamos el DataFrame
df_calificaciones = pd.DataFrame(datos_calificaciones, index=indice_alumnos, columns=nombres_materias)

### TERMINA CRONÓMETRO 2 ###
fin_df = time.time()
tiempo_df = fin_df - inicio_df


#==================================================================
# 3. Manipular y buscar los datos con Pandas
#==================================================================
alumno_a_buscar = 'Alumno_321'
materia_a_buscar = 'Materia_5'

print("La tabla de calificaciones tiene el siguiente formato (primeras 5 filas):")
print(df_calificaciones.head())
print("\n" + "="*50 + "\n")


### INICIA CRONÓMETRO 3 ###
inicio_busqueda = time.time()

try:
    # Usamos el método .loc[] para buscar por etiquetas
    calificacion_encontrada = df_calificaciones.loc[alumno_a_buscar, materia_a_buscar]
    
    ### TERMINA CRONÓMETRO 3 ###
    fin_busqueda = time.time()
    tiempo_busqueda = fin_busqueda - inicio_busqueda

    print(f"Buscando la calificación para '{alumno_a_buscar}' en la '{materia_a_buscar}'...")
    print("--------------------------------------------------")
    print(f"La calificación encontrada es: {calificacion_encontrada}")

except KeyError:
    print("El alumno o la materia no se encontró en el DataFrame.")

print("Mostrando el DataFrame completo con las nuevas opciones de visualización:")
# Configuramos pandas para mostrar el DataFrame completo
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Imprimimos el DataFrame completo para verificar
print(df_calificaciones)
#==================================================================
# 4. Resumen de Tiempos y Visualización Completa
#==================================================================
print("\n" + "="*50 + "\n")
print("📊 RESUMEN DE RENDIMIENTO:")
print(f"Tiempo en generar datos con NumPy:   {tiempo_numpy:.8f} segundos")
print(f"Tiempo en crear el DataFrame:        {tiempo_df:.8f} segundos")
print(f"Tiempo de búsqueda con .loc[]:       {tiempo_busqueda:.8f} segundos")
print("\n" + "="*50 + "\n")

