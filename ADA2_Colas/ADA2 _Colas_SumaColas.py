# PARTE 1: DEFINICIÓN DE LA CLASE COLA
class Cola:
    """
    Representa una cola, una estructura de datos FIFO (First-In, First-Out).
    """
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("No se puede desencolar de una cola vacía.")

    def __str__(self):
        """Permite imprimir la cola de forma legible."""
        return str(self.items)

# PARTE 2: FUNCIÓN PARA SUMAR
def sumar_colas(cola1, cola2):
    """
    Recibe dos Colas y devuelve una nueva con la suma de sus elementos.
    """
    cola_resultado = Cola()
    while not cola1.esta_vacia() and not cola2.esta_vacia():
        num1 = cola1.desencolar()
        num2 = cola2.desencolar()
        cola_resultado.encolar(num1 + num2)
    return cola_resultado

# PARTE 3: PROGRAMA INTERACTIVO
def programa_principal():
    """
    Función principal que interactúa con el usuario para crear y sumar las colas.
    """
    print("### Suma de Elementos de dos Colas (Versión Interactiva) ###\n")

    # Pedir y validar el tamaño de las colas
    tamano = 0
    while True:
        try:
            tamano_input = input("Introduce el tamaño que tendrán las colas: ")
            tamano = int(tamano_input)
            if tamano > 0:
                break
            else:
                print("Error: El tamaño debe ser un número mayor que cero.")
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

    print("-" * 30)

    # Pedir los datos para cada cola
    cola_a = Cola()
    cola_b = Cola()

    print(f"\nAhora, introduce los {tamano} elementos para la COLA A:")
    for i in range(tamano):
        while True:
            try:
                elemento_input = input(f"   Elemento {i + 1}: ")
                elemento = int(elemento_input)
                cola_a.encolar(elemento)
                break
            except ValueError:
                print("   Error: Introduce un número entero válido.")

    print(f"\nPerfecto. Ahora, introduce los {tamano} elementos para la COLA B:")
    for i in range(tamano):
        while True:
            try:
                elemento_input = input(f"   Elemento {i + 1}: ")
                elemento = int(elemento_input)
                cola_b.encolar(elemento)
                break
            except ValueError:
                print("   Error: Introduce un número entero válido.")
    
    print("-" * 30)

    # Mostrar las colas creadas y el resultado
    print(f"\nCola A creada: {cola_a}")
    print(f"Cola B creada: {cola_b}")

    cola_final = sumar_colas(cola_a, cola_b)

    print(f"\nResultado de la suma: {cola_final}")

# Ejecutar el programa
if __name__ == "__main__":
    programa_principal()
