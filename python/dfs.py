def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()   # Set to keep track of visited vertices

    visited.add(start)   # Mark the current vertex as visited
    print(start, end=' ')  # Process the current vertex

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursively call DFS for unvisited neighbors

# Example graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2]
}

# Start DFS from vertex 0
print("DFS Traversal:")
dfs(graph, 0)
