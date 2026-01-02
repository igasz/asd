from collections import deque

def topological_sort(G): #kahna
    n = len(G)
    in_degree = [0] * n #ile krawedzi wchodzi do wierzcholka

    for u in range(n):
        for v in G[u]:
            in_degree[v] += 1

    q = deque([u for u in range(n) if in_degree[u] == 0]) #do kolejki dajemy wierzcholki do ktorych nic nie wchodzi [0, 1, 1, 1]
    result = []

    while q: #przetwarzamy kolejke
        node = q.popleft()
        result.append(node)
        for v in G[node]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(result) != n: #bład jesli cykl, sortowanie niemozliwe
        raise ValueError("cykl")

    return result

def topological_sort_dfs(G):
    n = len(G)
    visited = [False] * n
    result = []

    def dfs(u):
        if visited[u] == True:
            return
        visited[u] = True
        for v in G[u]:
            dfs(v)
        result.append(u)

    for u in range(n):
        dfs(u)

    return result[::-1]


graph = [
    [1],    # 0
    [2, 3], # 1
    [],     # 2
    []      # 3
]

print(topological_sort(graph)) #[0, 1, 2, 3]
print(topological_sort_dfs(graph))

'''
0 → 1 → 2
    ↓
    3
'''