import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    min_spanning_tree = []

    # Start Prim's algorithm from vertex 0
    start_vertex = 0
    visited[start_vertex] = True
    edges = [(cost, start_vertex, neighbor) for neighbor, cost in enumerate(graph[start_vertex]) if cost > 0]
    heapq.heapify(edges)

    # Continue until all vertices are visited
    while len(min_spanning_tree) < n - 1:
        cost, u, v = heapq.heappop(edges)
        if visited[v]:
            continue

        visited[v] = True
        min_spanning_tree.append((u, v, cost))

        for neighbor, edge_cost in enumerate(graph[v]):
            if edge_cost > 0 and not visited[neighbor]:
                heapq.heappush(edges, (edge_cost, v, neighbor))

    return min_spanning_tree

# Example usage:
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

min_spanning_tree = prim(graph)
total_cost = sum(cost for _, _, cost in min_spanning_tree)
print("Minimum Spanning Tree (edges and costs):", min_spanning_tree)
print("Total cost of the minimum spanning tree:", total_cost)
