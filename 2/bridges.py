'''Złożoność czasowa O(V + E)
Złożoność pamięciowa O(V)
Most - krawędź, której usunięcie zwiększa liczbę spójnych składowych grafu
1. Dla każdego nieodwiedzonego wierzchołka u uruchamiana jest funkcja dfs(u, -1).
2. W DFS:
- Zaznaczamy u jako odwiedzone, zapisuje czas odwiedzenia.
- Przechodzimy po sąsiadach v:
-- Jeśli v nie było odwiedzone – rekurencyjnie wywołujemy dfs(v, u).
-- Po powrocie z DFS aktualizujemy low[u].
-- Jeżeli low[v] > d[u], to (u, v) jest mostem.
-- Jeśli v było już odwiedzone i nie jest rodzicem u, aktualizujemy low[u] = min(low[u], d[v]).
'''

def bridge(G):
    n = len(G)
    visited = [False] * n #czy wierzchołek odwiedzony
    d = [float('inf')] * n #czas odwiedzenia
    low = [float('inf')] * n #najwcześniejszy osiągalny czas odwiedzenia z poddrzewa
    time = 0
    bridges = [] #tablica mostów

    def dfs(u, parent):
        nonlocal time
        visited[u] = True
        d[u] = low[u] = time
        time += 1

        for v in G[u]:
            if not visited[v]:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > d[u]:
                    bridges.append((u, v))
            elif v != parent:
                low[u] = min(low[u], d[v])

    for u in range(n):
        if not visited[u]:
            dfs(u, -1)

    return bridges


n = 5
edges = [
    (1, 0),
    (0, 2),
    (2, 1),
    (0, 3),
    (3, 4)
]

graph = [[] for _ in range(n)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print("Mosty w grafie:", bridge(graph))