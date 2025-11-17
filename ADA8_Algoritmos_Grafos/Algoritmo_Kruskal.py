class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # Almacena [u, v, peso]

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Función Find con 'Path Compression'
    def find(self, parent, i):
        if parent[i] == i:
            return i
        # Optimización: Aplanamos el árbol recursivamente
        parent[i] = self.find(parent, parent[i])
        return parent[i]

    # Función Union con 'Union by Rank'
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Unimos el árbol de menor rango al de mayor rango
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []  # Almacenará el MST resultante
        i, e = 0, 0  # Índices para aristas ordenadas y aristas resultantes
        
        # 1. Ordenar todas las aristas por peso no decreciente
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Inicializar subconjuntos para cada nodo
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # 2. Iterar hasta tener V-1 aristas (condición de árbol)
        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            
            x = self.find(parent, u)
            y = self.find(parent, v)

            # 3. Si no forman ciclo (diferentes padres), incluir en el resultado
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    mst = g.kruskal_mst()
    print("Aristas en el Árbol de Expansión Mínima (MST):")
    minimum_cost = 0
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")
        minimum_cost += weight
    print(f"Costo Total del MST: {minimum_cost}")
