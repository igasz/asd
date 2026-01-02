'''Złożoność czasowa: O(VE)
Złożoność pamieciowa: O(V+E)
1. Relaksację krawędzi powtarzamy n - 1 razy, ponieważ w najgorszym przypadku najkrótsza ścieżka do wierzchołka może zawierać
n - 1 krawędzi.
2. Dla każdej krawędzi (u, v, w) sprawdzamy, czy da się poprawić wartość d[v] przez u, i aktualizujemy.
3. Zwracamy tablice d.
'''

def bellman_ford(G, s):
    n = len(G)
    d = [float('inf')] * n #tablica odleglosci od s
    d[s] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, w in G[u]:
                if d[u] != float('inf'):
                    if d[u] + w < d[v]:
                        d[v] = d[u] + w

    for u in range(n):
        for v, w in G[u]:
            if d[u] != float('inf') and d[u] + w < d[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return d

G = [
    [(1, 6), (2, 7)],      # 0 → 1 (6), 0 → 2 (7)
    [(2, 8), (3, 5), (4, -4)],  # 1 → 2 (8), 1 → 3 (5), 1 → 4 (-4)
    [(3, -3), (4, 9)],     # 2 → 3 (-3), 2 → 4 (9)
    [(1, -2)],             # 3 → 1 (-2)
    [(0, 2), (3, 7)]       # 4 → 0 (2), 4 → 3 (7)
]

print(bellman_ford(G, 0))