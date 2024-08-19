class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal(graph):
    n = len(graph)
    edges = []
    for u in range(n):
        for v in range(u + 1, n):
            if graph[u][v] != 0:
                edges.append((u, v, graph[u][v]))
    edges.sort(key=lambda x: x[2])

    min_spanning_tree = []
    uf = UnionFind(n)

    for edge in edges:
        u, v, weight = edge
        if uf.find(u) != uf.find(v):
            min_spanning_tree.append(edge)
            uf.union(u, v)

    return min_spanning_tree

# Example usage:
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

min_spanning_tree = kruskal(graph)
total_cost = sum(weight for _, _, weight in min_spanning_tree)
print("Minimum Spanning Tree (edges and costs):", min_spanning_tree)
print("Total cost of the minimum spanning tree:", total_cost)
