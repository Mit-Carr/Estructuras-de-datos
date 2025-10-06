# PARTE 1: DEFINICIÓN DE LA CLASE COLA
class Cola:
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

    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        return None

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return f"En espera: {self.items}"

# PARTE 2: IMPLEMENTACIÓN DEL SISTEMA DE ATENCIÓN
def sistema_de_atencion():
    print("### Sistema de Atención al Cliente - Compañía de Seguros ###")
    print("Comandos disponibles:")
    print("  - 'C' + [número de servicio] (ej: C1) -> Nuevo cliente llega.")
    print("  - 'A' + [número de servicio] (ej: A2) -> Atender próximo cliente.")
    print("  - Escriba 'SALIR' para terminar la simulación.")
    print("-" * 60)

    colas_de_servicio = {}

    while True:
        comando = input("Ingrese un comando: ").upper()

        if comando == 'SALIR':
            print("\nSimulación finalizada. ¡Hasta luego!")
            break

        if len(comando) < 2 or comando[0] not in ['C', 'A'] or not comando[1:].isdigit():
            print("Error: Comando no válido. Por favor, use el formato correcto (ej: C1, A2).")
            continue

        accion = comando[0]
        servicio_num = comando[1:]

        if accion == 'C':
            if servicio_num not in colas_de_servicio:
                colas_de_servicio[servicio_num] = Cola()

            if not hasattr(colas_de_servicio[servicio_num], 'contador_ticket'):
                 colas_de_servicio[servicio_num].contador_ticket = 1
            
            ticket_actual = colas_de_servicio[servicio_num].contador_ticket
            colas_de_servicio[servicio_num].encolar(ticket_actual)
            
            print(f"-> Cliente con ticket '{servicio_num}-{ticket_actual}' añadido a la cola del servicio {servicio_num}.")
            
            colas_de_servicio[servicio_num].contador_ticket += 1

        elif accion == 'A':
            if servicio_num in colas_de_servicio and not colas_de_servicio[servicio_num].esta_vacia():
                ticket_atendido = colas_de_servicio[servicio_num].desencolar()
                print(f"** Llamando al cliente con ticket '{servicio_num}-{ticket_atendido}' del servicio {servicio_num}. **")
            else:
                print(f"-> No hay clientes en espera para el servicio {servicio_num}.")

        print("\n--- Estado Actual de las Colas ---")
        if not colas_de_servicio:
            print("No hay colas activas.")
        else:
            for servicio, cola in colas_de_servicio.items():
                if cola.esta_vacia():
                    print(f"Servicio {servicio}: 0 clientes en espera.")
                else:
                    print(f"Servicio {servicio}: {cola.tamano()} cliente(s). {cola}")
        print("-" * 34 + "\n")

if __name__ == "__main__":
    sistema_de_atencion()
