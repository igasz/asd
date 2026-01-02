'''Złożoność czasowa O(V + E)
Złożoność pamięciowa O(V + E)
Dla każdego nieodwiedzonego wierzchołka uruchamiana jest funkcja dfs(u, -1):
1. Zliczamy dzieci children (dla korzenia),
2. Dla każdego sąsiada v:
- jeśli nie był odwiedzony – rekurencyjne wywołanie dfs(v, u),
- aktualizacja low[u],
- warunki sprawdzające, czy u jest punktem artykulacji.
'''

def articulationpoints(G):
    n = len(G)
    visited = [False] * n #czy wierzchołek odwiedzony
    d = [float('inf')] * n #czas odwiedzenia
    low = [float('inf')] * n #najwcześniejszy osiągalny czas odwiedzenia z poddrzewa
    ap = [False] * n #czy pkt artykulacji
    time = 0

    def dfs(u, parent):
        nonlocal time
        children = 0
        visited[u] = True
        d[u] = low[u] = time
        time += 1

        for v in G[u]:
            if not visited[v]:
                children += 1
                dfs(v, u)

                low[u] = min(low[u], low[v])
                if parent != -1 and low[v] > d[u]:
                    ap[u] = True
                if parent == -1 and children > 1:
                    ap[u] = True
            elif v != parent:
                low[u] = min(low[u], d[v])

    for u in range(n):
        if not visited[u]:
            dfs(u, -1)

    return [i for i, ap in enumerate(ap) if ap]

G = [
    [1, 2],
    [0, 2],
    [0, 1, 3, 5],
    [2, 4],
    [3],
    [2, 6, 7],
    [5],
    [5]
]
print(articulationpoints(G))