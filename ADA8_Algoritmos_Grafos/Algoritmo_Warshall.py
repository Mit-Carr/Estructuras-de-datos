def warshall_transitive_closure(graph):
    V = len(graph)
    # Copiamos el grafo original para no modificar la entrada
    # reach[i][j] será 1 si existe un camino de i a j, 0 si no.
    reach = [row[:] for row in graph]

    # K representa el nodo intermedio
    for k in range(V):
        # I representa el nodo origen
        for i in range(V):
            # J representa el nodo destino
            for j in range(V):
                # La celda es verdadera si ya existía un camino directo (reach[i][j])
                # O si existe un camino a través de K (reach[i][k] AND reach[k][j])
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    
    return reach

if __name__ == "__main__":
    # Grafo dirigido representado como matriz de adyacencia (binaria)
    # 1 indica conexión directa, 0 indica sin conexión
    graph = [
        [1, 1, 0, 1], # Nodo 0 alcanza a 0, 1, 3
        [0, 1, 1, 0], # Nodo 1 alcanza a 1, 2
        [0, 0, 1, 1], # Nodo 2 alcanza a 2, 3
        [0, 0, 0, 1]  # Nodo 3 alcanza solo a sí mismo
    ]

    closure = warshall_transitive_closure(graph)

    print("Matriz de Clausura Transitiva (Alcanzabilidad):")
    for row in closure:
        print(row)