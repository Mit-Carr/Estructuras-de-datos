import numpy as np
#se importa numpy para simular con mayor precision el hecho de que solo ingresen 5 datos, debido a que diferencia de java, python no es tan estricto
#
# Crear un arreglo de 5 enteros inicializado en 0 (tamaño fijo)
calificaciones = np.zeros(5, dtype=int)

# Capturar las calificaciones desde el teclado
for i in range(5):
    entrada = input(f"Captura la calificación {i+1}: ")
    calificaciones[i] = int(entrada)

# Mostrar resultados
print("Calificaciones capturadas:", calificaciones)

#en el otro caso al ser dinamico simplemente se crea el array
frutas = []

# Agregar elementos 5
frutas.append("mango")
frutas.append("manzana")
frutas.append("banana")
frutas.append("uvas")

print(frutas)  # ['mango', 'manzana', 'banana', 'uvas']

# Remover elementos por índice
frutas.pop(0)  # elimina "mango"
frutas.pop(1)  # ahora elimina "banana" (que estaba en índice 1 tras la eliminación anterior)

print(frutas)  # ['manzana', 'uvas']
