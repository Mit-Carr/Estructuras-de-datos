# ------------------------------------------------------------------
# 1. CLASE PEDIDO (Define la estructura del dato)
# ------------------------------------------------------------------
class Pedido:
    """
    Define la estructura de un pedido, con cliente y cantidad.
    """
    def __init__(self, cliente, cantidad):
        self.cliente = cliente
        self.cantidad = cantidad

    def __str__(self):
        # Ayudante para imprimir el pedido de forma clara
        return f"[Pedido de: {self.cliente}, Cantidad: {self.cantidad}]"

# ------------------------------------------------------------------
# 2. CLASE NODO (Componente de la Lista Enlazada)
# ------------------------------------------------------------------
class Nodo:
    """
    Define el nodo de la lista enlazada.
    Contiene el dato (el pedido) y el puntero al siguiente nodo.
    """
    def __init__(self, pedido):
        self.pedido = pedido      # objeto Pedido
        self.siguiente = None   # Puntero al siguiente nodo

# ------------------------------------------------------------------
# 3. CLASE COLAPEDIDOS (Gestor de la Cola)
# ------------------------------------------------------------------
class ColaPedidos:
    """
    La lista enlazada con FIFO
    """
    def __init__(self):
        self.frente = None  # El primer nodo en la fila
        self.final = None   # El último nodo en la fila
        self.tamaño = 0

    def esta_vacia(self):
        
        return self.frente is None

    def encolar(self, pedido):
        """
        Añade un nuevo pedido al final de la cola.
        """
        nuevo_nodo = Nodo(pedido)
        
        if self.esta_vacia():
            # Si es el primer pedido, es el frente y el final
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            # Si ya hay pedidos, se añade después del 'final' actual
            self.final.siguiente = nuevo_nodo
            # Se actualiza el puntero 'final' al nuevo nodo
            self.final = nuevo_nodo
            
        self.tamaño += 1
        print(f"\n>> Pedido recibido: {pedido}")

    def desencolar(self):
        """
        elimina el pedido del frente de la cola.
        """
        if self.esta_vacia():
            print("\n>> SISTEMA: No hay pedidos pendientes.")
            return None
            
        # pedido del nodo frontal
        pedido_a_procesar = self.frente.pedido
        
        # Mover el puntero 'frente' al siguiente nodo
        self.frente = self.frente.siguiente
        
        # Si la cola quedó vacía, actualiza también el puntero 'final'
        if self.frente is None:
            self.final = None
            
        self.tamaño -= 1
        print(f"\n>> Procesando: {pedido_a_procesar}")
        return pedido_a_procesar

    def ver_siguiente(self):
        """Muestra el siguiente pedido a procesar sin quitarlo."""
        if self.esta_vacia():
            print("\n>> SISTEMA: La cola de pedidos está vacía.")
            return None
        print(f"\n>> Siguiente en la fila: {self.frente.pedido}")
        return self.frente.pedido

    def mostrar_estado(self):
        """Muestra cuántos pedidos hay en espera."""
        print(f"--- ESTADO ACTUAL: {self.tamaño} pedidos en espera ---")

    def visualizar_todos(self):
        """
        Muestra todos los elementos actuales en la cola, del frente al final.
        """
        print("\n--- Vista de la Cola (Frente a Final) ---")
        if self.esta_vacia():
            print("(Cola vacía)")
            return

        actual = self.frente
        i = 0
        while actual:
            print(f"  Posición {i}: {actual.pedido}")
            actual = actual.siguiente
            i += 1
        print("------------------------------------------")

    def obtener_Numero_lugar(self, pos):
        """
        Obtiene el N-ésimo de la cola sin borrarlo.
        """
        if pos < 0 or pos >= self.tamaño:
            print(f"\n>> ERROR: Posición {pos} fuera de rango (Tamaño actual: {self.tamaño}).")
            return None  # Devuelve None (equivalente a null)

        actual = self.frente
        for _ in range(pos):
            actual = actual.siguiente
        return actual.pedido

# ------------------------------------------------------------------
# 4. FUNCIÓN DE PRUEBA (Prueba de obtener_Numero_lugar)
# ------------------------------------------------------------------
def probar_obtener_Numero_lugar():
    """
    Esta parte es el inciso 2 del ejercicio donde pide ingresar 4 datos y buscar el tercero, pero de todas
    formas se hizo interacivo
    """
    print("--- INICIANDO PRUEBA ESPECÍFICA del ejercicio 2: obtener el n-ésimo elemento de la cola (sin borrarlo), Prueba a introducir cuatro elementos y obtener el tercero.---")
    sistema_prueba = ColaPedidos()
    
    print("\nEncolando 4 elementos...")
    sistema_prueba.encolar(Pedido("Cliente A", 10)) # Pos 0
    sistema_prueba.encolar(Pedido("Cliente B", 20)) # Pos 1
    sistema_prueba.encolar(Pedido("Cliente C", 30)) # Pos 2
    sistema_prueba.encolar(Pedido("Cliente D", 40)) # Pos 3

    # Visualizar
    sistema_prueba.visualizar_todos()

    # 2. Obtener el tercero 
    print("\nObteniendo el 3er elemento...")
    pos_a_buscar = 2
    elemento = sistema_prueba.obtener_Numero_lugar(pos_a_buscar)
    
    if elemento:
        print(f"Resultado (Pos {pos_a_buscar}): {elemento}")
    else:
        print(f"No se pudo obtener el elemento en la posición {pos_a_buscar}.")

    # 3. Prueba de caso inválido (pedir posición 10)
    print("\nIntentando obtener la posición 10 (inválida)...")
    elemento_invalido = sistema_prueba.obtener_Numero_lugar(10)
    if elemento_invalido is None:
        print("Resultado: Devuelve None (null) como se esperaba.")
    
    print("--- PRUEBA ESPECÍFICA TERMINADA, LO SIGUIENTE SERA LA INTERFAZ (NO TIENE LOS DATOS USADOS EN ESTE EJEMPLO ESPECIFICO) ---\n")

# ------------------------------------------------------------------
# 5.(Menú de usuario)
# ------------------------------------------------------------------
def interfaz():
    """
    Ejecuta el menú principal para interactuar con la cola.
    """
    sistema = ColaPedidos()
    
    while True:
        print("\n--- Sistema de Recepción de Pedidos ---")
        print("1. Agregar nuevo pedido (Encolar)")
        print("2. Procesar siguiente pedido (Desencolar)")
        print("3. Ver próximo pedido (Frente)")
        print("4. Ver estado de la cola")
        print("5. Visualizar TODOS los pedidos")
        print("6. Obtener pedido N-ésimo (por posición)")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Agregar pedido
            cliente = input("Nombre del cliente: ")
            
            # Validación simple para la cantidad
            while True:
                try:
                    cantidad = int(input("Cantidad de producto: "))
                    if cantidad > 0:
                        break
                    else:
                        print("Error: La cantidad debe ser un número positivo.")
                except ValueError:
                    print("Error: Ingrese un número válido para la cantidad.")

            nuevo_pedido = Pedido(cliente, cantidad)
            sistema.encolar(nuevo_pedido)

        elif opcion == '2':
            # Procesar pedido
            sistema.desencolar()

        elif opcion == '3':
            # Ver próximo
            sistema.ver_siguiente()

        elif opcion == '4':
            # Ver estado
            sistema.mostrar_estado()

        elif opcion == '5':
            # Visualizar todos
            sistema.visualizar_todos()

        elif opcion == '6':
            # Obtener N-ésimo
            try:
                pos = int(input("Ingrese la posición (empieza en 0): "))
                pedido = sistema.obtener_Numero_lugar(pos)
                if pedido:
                    print(f"\n>> El pedido en la posición {pos} es: {pedido}")
            except ValueError:
                print("Error: Ingrese un número válido.")

        elif opcion == '7':
            # Salir
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("\nError: Opción no válida. Intente de nuevo.")

# ------------------------------------------------------------------
# 6. EJECUCIÓN PRINCIPAL
# ------------------------------------------------------------------
if __name__ == "__main__":
    # Primero, ejecutamos la prueba específica solicitada
    probar_obtener_Numero_lugar()
    
    # Luego, iniciamos el modo interactivo
    print("\n...Ahora iniciando el modo interactivo...")
    interfaz()
