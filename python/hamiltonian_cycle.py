def is_valid(v, graph, path, pos):
    # Check if this vertex is adjacent to the previously added vertex
    if graph[path[pos-1]][v] == 0:
        return False

    # Check if this vertex has already been included in the path
    if v in path:
        return False

    return True

def hamiltonian_cycle_util(graph, path, pos, n):
    # Base case: if all vertices are included in the path, check if it's a Hamiltonian cycle
    if pos == n:
        # Check if there is an edge from the last added vertex to the first vertex
        if graph[path[pos-1]][path[0]] == 1:
            return True
        else:
            return False

    # Try all vertices as the next vertex of Hamiltonian cycle
    for v in range(1, n):
        if is_valid(v, graph, path, pos):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1, n):
                return True
            path[pos] = -1

    return False

def hamiltonian_cycle(graph):
    n = len(graph)
    path = [-1] * n
    path[0] = 0  # Start from vertex 0

    if not hamiltonian_cycle_util(graph, path, 1, n):
        print("No Hamiltonian cycle exists")
        return False

    print("Hamiltonian cycle exists:")
    print("Path:", path)
    return True

# Example usage:
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hamiltonian_cycle(graph)
