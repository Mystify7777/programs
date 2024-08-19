class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

def bellman_ford(vertices, edges, source):
    # Initialize the distance to all vertices as infinite and distance to the source as 0
    dist = [float('inf')] * vertices
    dist[source] = 0

    # Relax all edges |V| - 1 times
    for _ in range(vertices - 1):
        for edge in edges:
            if dist[edge.u] + edge.weight < dist[edge.v]:
                dist[edge.v] = dist[edge.u] + edge.weight

    # Check for negative-weight cycles
    for edge in edges:
        if dist[edge.u] + edge.weight < dist[edge.v]:
            print("Graph contains negative weight cycle")
            return None

    return dist

# Example usage:
vertices = 5
edges = [
    Edge(0, 1, -1),
    Edge(0, 2, 4),
    Edge(1, 2, 3),
    Edge(1, 3, 2),
    Edge(1, 4, 2),
    Edge(3, 2, 5),
    Edge(3, 1, 1),
    Edge(4, 3, -3)
]
source = 0

distances = bellman_ford(vertices, edges, source)

if distances:
    print("Vertex Distance from Source")
    for i in range(vertices):
        print(f"{i}\t\t{distances[i]}")
