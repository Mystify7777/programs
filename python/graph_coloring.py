def graph_coloring_dynamic(graph, m):
    n = len(graph)
    memo = {}

    def is_safe(v, color, c):
        for i in range(n):
            if graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_coloring_util(v, color):
        if v == n:
            return True

        if (v, tuple(color)) in memo:
            return memo[(v, tuple(color))]

        for c in range(1, m + 1):
            if is_safe(v, color, c):
                color[v] = c
                if graph_coloring_util(v + 1, color):
                    memo[(v, tuple(color))] = True
                    return True
                color[v] = 0

        memo[(v, tuple(color))] = False
        return False

    color = [0] * n
    if graph_coloring_util(0, color):
        return color
    else:
        return None

# Example usage:
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3  # Number of colors

result = graph_coloring_dynamic(graph, m)
if result:
    print("Solution exists: Following are the assigned colors")
    for idx, color in enumerate(result):
        print(f"Vertex {idx} ---> Color {color}")
else:
    print("No solution exists")
