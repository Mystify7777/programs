import heapq

def dijkstra(graph, source):
    n = len(graph)
    distances = [float('inf')] * n
    distances[source] = 0
    pq = [(0, source)]  # Priority queue to store (distance, vertex) pairs
    visited = [False] * n

    while pq:
        dist_u, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v, weight in enumerate(graph[u]):
            if weight > 0 and not visited[v]:
                alt = dist_u + weight
                if alt < distances[v]:
                    distances[v] = alt
                    heapq.heappush(pq, (alt, v))

    return distances

# Example usage:
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
source = 0

shortest_distances = dijkstra(graph, source)
print("Shortest distances from source vertex:")
for i, distance in enumerate(shortest_distances):
    print(f"Vertex {i}: {distance}")
