
MAX_CAPACIDAD = 8


#  LIFO (Last-In, First-Out).
pila = []


def insertar(pila_actual, elemento):
    """
    Esta función añade un elemento al TOPE de la pila.
    Es la operación "push".
    """
    
    print(f"-> Operación: Insertar('{elemento}')")

  
    if len(pila_actual) < MAX_CAPACIDAD:
        
        pila_actual.append(elemento)
    else:
        
        print(f"   ¡ERROR! Desbordamiento. La pila está llena.")
    
    
    print(f"   Estado: {pila_actual}, TOPE = {len(pila_actual)}")

def eliminar(pila_actual):
    """
    Esta función elimina el elemento del TOPE de la pila y lo devuelve.
    Es la operación "pop".
    """
    
    print(f"-> Operación: Eliminar()")

   
    if len(pila_actual) > 0:
      
        elemento_eliminado = pila_actual.pop()
        print(f"   Elemento eliminado del TOPE: '{elemento_eliminado}'")
        return elemento_eliminado
    else:
        
        print("   ¡ERROR! Subdesbordamiento. La pila está vacía.")
        # 'None' para indicar que no se pudo sacar nada.
        return None



print(f"--- Inicio de la simulación ---")
print(f"Pila inicial: {pila}, TOPE = {len(pila)}, Capacidad Máxima: {MAX_CAPACIDAD}\n")


# a
insertar(pila, 'X')

# b.
insertar(pila, 'Y')

# c
Z = eliminar(pila)

# d. 
T = eliminar(pila)

# e. 
U = eliminar(pila)

# f. Añade 'V'.
insertar(pila, 'V')

# g. Añade 'W' sobre 'V'.
insertar(pila, 'W')

# h..
p = eliminar(pila)

# i
insertar(pila, 'R')

print("\n--- Simulación Finalizada ---")



# solo se mantiene V y R
print(f"El estado final de la pila es: {pila}")

# quedan solo 2
print(f"La cantidad final de elementos es: {len(pila)}")
