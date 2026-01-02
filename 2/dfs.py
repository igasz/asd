'''Złożenie czasowe:
1. Start z węzła początkowego (np. A).
2. Odwiedź ten węzeł i oznacz jako odwiedzony.
3. Dla każdego sąsiada: Jeśli nie był odwiedzony, wejdź głębiej (rekurencyjnie lub przez stos).
4.Po wyczerpaniu ścieżki, cofasz się i eksplorujesz kolejnych sąsiadów.
Zastosowanie:
- Sprawdzanie cykli w grafie.
- Topologiczne sortowanie w grafie skierowanym acyklicznym (DAG).
- Sprawdzanie spójności i liczby składowych grafu.'''


def dfs_rec(G, s, visited=None):
    n = len(G)
    if visited is None:
        visited = [False] * n
    visited[s] = True
    for v in G[s]:
        if not visited[v]:
            visited[v] = True
            dfs_rec(G, v, visited)
    return visited

G = [
    [1, 2],    # sąsiedzi wierzchołka 0
    [0, 3],    # sąsiedzi wierzchołka 1
    [0],       # sąsiedzi wierzchołka 2
    [1, 4],    # sąsiedzi wierzchołka 3
    []         # sąsiedzi wierzchołka 4
]

print(dfs_rec(G, 0))

def dfs_it(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}

print(dfs_it(graph, 'A'))