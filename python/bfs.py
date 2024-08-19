from collections import deque

def bfs(graph, start):
    visited = set()            # Set to keep track of visited vertices
    queue = deque([start])     # Initialize queue with the start vertex
    visited.add(start)         # Mark start vertex as visited

    while queue:
        vertex = queue.popleft()    # Dequeue a vertex from the queue
        print(vertex, end=' ')      # Process the current vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)     # Mark neighbor as visited
                queue.append(neighbor)    # Enqueue the neighbor

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

# Start BFS from vertex 0
print("BFS Traversal:")
bfs(graph, 0)
