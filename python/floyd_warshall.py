def floyd_warshall(graph):
    # Number of vertices in the graph
    V = len(graph)
    
    # Initialize the solution matrix the same as input graph matrix
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # Add vertices individually
    for k in range(V):
        # Pick all vertices as source one by one
        for i in range(V):
            # Pick all vertices as destination for the above picked source
            for j in range(V):
                # If vertex k is on the shortest path from i to j,
                # then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Return the shortest path matrix
    return dist

# Example usage:
# Define the graph as a 2D list
# INF represents a large number signifying no direct path between nodes
INF = float('inf')
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

# Run Floyd-Warshall algorithm
shortest_paths = floyd_warshall(graph)

# Print the result
print("Shortest distance matrix:")
for row in shortest_paths:
    print(row)
