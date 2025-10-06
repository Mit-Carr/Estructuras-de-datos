# 1. Clase Pila: Representa cada una de las tres torres.
class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    
    def __str__(self):
        return f"Torre {self.nombre}: {self.items}"

contador_movimientos = 0

# 2. Nueva Función para Graficar las Torres (ASCII art)
def imprimir_torres_grafico(num_total_discos):
    altura = num_total_discos + 2
    
    for nivel in range(altura, 0, -1):
        linea_para_imprimir = ""
        for torre in [torre_A, torre_B, torre_C]:
            ancho_torre = num_total_discos * 2 + 1

            if nivel > len(torre.items):
                linea_para_imprimir += " " * num_total_discos + "|" + " " * num_total_discos
            else:
                disco = torre.items[nivel - 1]
                ancho_disco = disco * 2 - 1
                disco_str = "=" * ancho_disco
                padding = " " * ((ancho_torre - ancho_disco) // 2)
                linea_para_imprimir += padding + disco_str + padding
            
            linea_para_imprimir += "   "
        
        print(linea_para_imprimir)

    ancho_base_total = (num_total_discos * 2 + 1) * 3 + 6
    print("-" * ancho_base_total)
    print(f"{torre_A.nombre.center(num_total_discos*2+1)}   {torre_B.nombre.center(num_total_discos*2+1)}   {torre_C.nombre.center(num_total_discos*2+1)}")
    print("-" * 35)


# 3. Función Recursiva (sin cambios en la lógica)
def torres_de_hanoi(n, origen, destino, auxiliar, num_total_discos):
    global contador_movimientos

    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)
        contador_movimientos += 1
        print(f"Movimiento {contador_movimientos}: Mover disco {disco} de {origen.nombre} a {destino.nombre}")
        imprimir_torres_grafico(num_total_discos)
        return

    torres_de_hanoi(n - 1, origen, auxiliar, destino, num_total_discos)

    disco = origen.desapilar()
    destino.apilar(disco)
    contador_movimientos += 1
    print(f"Movimiento {contador_movimientos}: Mover disco {disco} de {origen.nombre} a {destino.nombre}")
    imprimir_torres_grafico(num_total_discos)

    torres_de_hanoi(n - 1, auxiliar, destino, origen, num_total_discos)


# 4. CONFIGURACIÓN Y EJECUCIÓN DEL JUEGO
torre_A = Pila("A (Origen)")
torre_B = Pila("B (Auxiliar)")
torre_C = Pila("C (Destino)")

while True:
    try:
        num_discos_str = input("¿Cuántos discos quieres usar para las Torres de Hanoi? ")
        num_discos = int(num_discos_str)
        if num_discos > 0 and num_discos < 10:
            break
        else:
            print("Por favor, introduce un número entre 1 y 9.")
    except ValueError:
        print("Error: Debes introducir un número entero.")

for i in range(num_discos, 0, -1):
    torre_A.apilar(i)

print("\n--- ESTADO INICIAL ---")
imprimir_torres_grafico(num_discos)

print("\n--- INICIANDO MOVIMIENTOS ---")
torres_de_hanoi(num_discos, torre_A, torre_C, torre_B, num_discos)

print("\n¡Puzzle completado!")
print(f"Número total de movimientos: {contador_movimientos}")
