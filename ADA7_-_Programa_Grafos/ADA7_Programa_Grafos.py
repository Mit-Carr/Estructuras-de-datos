import networkx as nx
import matplotlib.pyplot as plt

#el networkx es para facilitar la visualizacion de los grafos 
# grafo no dirigido 
def calcular_costo_recorrido(g, recorrido):
    """
    Calcula el costo total de un recorrido dado en el grafo.
    El recorrido es una lista de nodos (estados).
    """
    costo_total = 0
    # Iteramos (estado_actual, estado_siguiente)
    for i in range(len(recorrido) - 1):
        u = recorrido[i]
        v = recorrido[i+1]
        
        # Verificamos si la arista (conexión) existe
        # u son los nodos y v son las conexiones/aristas
        if g.has_edge(u, v):
            # Obtenemos el costo (peso) de la arista
            costo = g[u][v]['weight']
            costo_total += costo
            print(f"  > De {u} a {v}: {costo} hrs")
        else:
            print(f"ERROR: No hay conexión directa entre {u} y {v}")
            return None
            
    return costo_total

# --- 1. Definición del Grafo (Estados y Conexiones) ---
# 7 estados del sureste de México pos por yucatan
# esto es para facilitar, por lo que se define la ruta, si no seria usar fuerza bruta mediante un camino hamiltoniano
estados = [
    'Yucatán', 'Campeche', 'Quintana Roo', 'Tabasco', 
    'Chiapas', 'Veracruz', 'Oaxaca'
]

# Definimos las conexiones (aristas) y sus costos (pesos)
# Usaremos horas de viaje aproximadas como "costo"
conexiones = [
    ('Yucatán', 'Campeche', 2.5),
    ('Yucatán', 'Quintana Roo', 4),
    ('Campeche', 'Tabasco', 4.5),
    ('Campeche', 'Quintana Roo', 5), # Conexión por el sur
    ('Tabasco', 'Chiapas', 3),
    ('Tabasco', 'Veracruz', 5),
    ('Chiapas', 'Veracruz', 7),
    ('Chiapas', 'Oaxaca', 6),
    ('Veracruz', 'Oaxaca', 6.5)
]

# Crear el grafo
G = nx.Graph()

# Añadir los nodos (estados)
G.add_nodes_from(estados)

# Añadir las aristas (conexiones) con sus pesos (costos)
for u, v, w in conexiones:
    G.add_edge(u, v, weight=w)

# --- 2. Mostrar Estados y Relaciones ---
print("--- ESTADOS Y RELACIONES (CONEXIONES) ---")
print(f"Estados (Nodos): {list(G.nodes())}")
print("Conexiones (Aristas con costos en horas):")
for (u, v, data) in G.edges(data=True):
    print(f"- {u} <--> {v} (Costo: {data['weight']} hrs)")
print("-" * 40)


# --- 3. Recorrido a) Sin repetir estados ---
# Un recorrido que visita todos los 7 estados sin repetir
# Esto es seleccionado manualmente
# se podrian usar metodos heuristicos o geneticos pero se vuelve mas complejo
recorrido_a = [
    'Quintana Roo', 'Yucatán', 'Campeche', 'Tabasco', 
    'Chiapas', 'Oaxaca', 'Veracruz'
]

print("\n--- RECORRIDO A (Sin repetir estados) ---")
print(f"Recorrido propuesto: {' -> '.join(recorrido_a)}")
print("Cálculo del costo:")

# Calcular y mostrar el costo total
costo_a = calcular_costo_recorrido(G, recorrido_a)
if costo_a is not None:
    print(f"\n==> Costo total del recorrido A: {costo_a:.2f} horas")
print("-" * 40)


# --- 4. Recorrido b) Repitiendo al menos un estado ---
# Un recorrido que visita todos los 7 estados, pero repite 'Tabasco'
recorrido_b = [
    'Quintana Roo', 'Yucatán', 'Campeche', 'Tabasco', 
    'Chiapas', 'Tabasco', 'Veracruz', 'Oaxaca'
]

# Verificamos que se visitan todos
estados_visitados_b = set(recorrido_b)
print("\n--- RECORRIDO B (Repitiendo al menos un estado) ---")
print(f"Recorrido propuesto: {' -> '.join(recorrido_b)}")
print(f"Estados únicos visitados: {len(estados_visitados_b)} (Todos los {len(estados)})")
print("Cálculo del costo:")

# mostrar el costo total
costo_b = calcular_costo_recorrido(G, recorrido_b)
if costo_b is not None:
    print(f"\n==> Costo total del recorrido B: {costo_b:.2f} horas")
print("-" * 40)



print("\nGenerando el dibujo del grafo...")

# Definir una posición para los nodos para que se vea bien
pos = nx.spring_layout(G, seed=42) 

# Obtener las etiquetas de los pesos (costos)
edge_labels = nx.get_edge_attributes(G, 'weight')

# Dibujar el grafo
plt.figure(figsize=(12, 8))
nx.draw(
    G, 
    pos, 
    with_labels=True, 
    node_color='red', 
    node_size=2700, 
    font_size=10, 
    font_weight='bold',
    width=2 # Ancho de las aristas
)
# Dibujar las etiquetas de los costos en las aristas
nx.draw_networkx_edge_labels(
    G, 
    pos, 
    edge_labels=edge_labels, 
    font_color='red'
)

plt.title("Grafo de Estados de México y Costos de Viaje (hrs)")
plt.show()
