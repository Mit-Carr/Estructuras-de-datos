# ------------------------------------------------
# main.py (Versión "Explosiva")
# ------------------------------------------------
from parte2class import MyLinkedList

# --- Una pequeña función para hacer la salida más clara ---
def print_header(title):
    """Imprime un título bonito para separar las pruebas."""
    print("\n" + "="*40)
    print(f" 🧪 PRUEBA: {title.upper()} 🧪")
    print("="*40)
# ---------------------------------------------------------


print_header("1. Creación y estado inicial")
lista_prueba = MyLinkedList()
print("¿Lista recién creada está vacía?", lista_prueba.is_empty())
print("Tamaño inicial:", lista_prueba.length())
print("Mostrando lista vacía:")
lista_prueba.show()

# ---
print_header("2. Añadiendo elementos (Append)")
print("Añadiendo: 10, 20, 30, 40")
lista_prueba.append(10)
lista_prueba.append(20)
lista_prueba.append(30)
lista_prueba.append(40)
lista_prueba.show()
print("Tamaño actual:", lista_prueba.length())
print("¿Está vacía ahora?", lista_prueba.is_empty())

# ---
print_header("3. Añadiendo al inicio (Insert at Start)")
print("Añadiendo: 5 y 1 al inicio")
lista_prueba.insert_at_start(5)
lista_prueba.insert_at_start(1)
# Lista esperada: 1 -> 5 -> 10 -> 20 -> 30 -> 40
lista_prueba.show()
print("Tamaño actual:", lista_prueba.length())

# ---
print_header("4. Búsqueda (Search)")
print("Buscando 20 (debería ser True):", lista_prueba.search(20))
print("Buscando 1 (la cabeza, True):", lista_prueba.search(1))
print("Buscando 40 (la cola, True):", lista_prueba.search(40))
print("Buscando 99 (no existe, False):", lista_prueba.search(99))

# ---
print_header("5. Inserción en posición (Insert at Position)")
# Lista actual: 1 -> 5 -> 10 -> 20 -> 30 -> 40
print("Insertando 99 en posición 3 (después del 10)")
try:
    lista_prueba.insert_at_position(3, 99)
    # Lista esperada: 1 -> 5 -> 10 -> 99 -> 20 -> 30 -> 40
    lista_prueba.show()
except IndexError as e:
    print(f"Error: {e}")

print(f"\nInsertando 100 al final (en posición {lista_prueba.length()})")
try:
    # Esto debería funcionar como un append
    lista_prueba.insert_at_position(lista_prueba.length(), 100)
    # Lista esperada: 1 -> 5 -> 10 -> 99 -> 20 -> 30 -> 40 -> 100
    lista_prueba.show()
except IndexError as e:
    print(f"Error: {e}")

print("\nIntentando insertar en índice inválido (ej: 50)")
try:
    lista_prueba.insert_at_position(50, 777)
except IndexError as e:
    print(f"Error capturado (¡esto es bueno!): {e}")
lista_prueba.show()

# ---
print_header("6. Eliminación (Remove) - Casos Especiales")
# Lista actual: 1 -> 5 -> 10 -> 99 -> 20 -> 30 -> 40 -> 100
print("Eliminando 99 (un nodo en medio)")
lista_prueba.remove(99)
# Lista esperada: 1 -> 5 -> 10 -> 20 -> 30 -> 40 -> 100
lista_prueba.show()

print("\nEliminando 1 (el nodo 'head' o cabeza)")
lista_prueba.remove(1)
# Lista esperada: 5 -> 10 -> 20 -> 30 -> 40 -> 100
lista_prueba.show()

print("\nEliminando 100 (el nodo 'tail' o cola)")
lista_prueba.remove(100)
# Lista esperada: 5 -> 10 -> 20 -> 30 -> 40
lista_prueba.show()

print("\nIntentando eliminar 99 de nuevo (ya no existe)")
lista_prueba.remove(99)
print("La lista no debería cambiar:")
lista_prueba.show()
print("Tamaño actual:", lista_prueba.length())

# ---
print_header("7. Vaciando la lista")
print("Eliminando todos los elementos restantes...")
lista_prueba.remove(10)
lista_prueba.remove(30)
lista_prueba.remove(5)
lista_prueba.remove(40)
lista_prueba.remove(20) 
print("Lista final:")
lista_prueba.show()
print("¿Está vacía ahora?", lista_prueba.is_empty())
print("Tamaño final:", lista_prueba.length())

# ---
print_header("8. Pruebas en lista vacía")
print("Intentando eliminar '10' de la lista ya vacía:")
lista_prueba.remove(10) 
print("Buscando '10' en la lista vacía:", lista_prueba.search(10))
print("Mostrando lista vacía de nuevo:")
lista_prueba.show()

print("\n" + "="*40)
print("PRUEBAS COMPLETADAS")
print("="*40)
