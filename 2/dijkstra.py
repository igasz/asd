'''Złożoność czasowa: O((V + E) log V)
Złożoność pamieciowa: O(V+E)
1. ustawiamy wszystkie odleglosci na nieskonczonosc
2. Używamy kopca (heapq) do wybierania wierzchołka o najmniejszej znanej odległości.
3. Aktualizujemy odległości do sąsiadów, jeśli znajdujemy krótszą ścieżkę.
'''
import heapq

def dijkstra(G, s):
    n = len(G)
    d = [float('inf')] * n #tablica odlegosci od s
    visited = [False] * n #czy wierzcholek odwiedzony
    d[s] = 0
    heap = [(0, s)]

    while heap:
        dist, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True

        for v, w in G[u]:
            if d[u] + w < d[v]: #relaksacja
                d[v] = d[u] + w
                heapq.heappush(heap, (d[v], v))

    return d

graph = [
    [(1, 5), (2, 1)],            # 0 -> 1 (5), 0 -> 2 (1)
    [(0, 5), (2, 2), (3, 1)],
    [(0, 1), (1, 2), (3, 4), (4, 8)],
    [(1, 1), (2, 4), (4, 3)],
    [(2, 8), (3, 3)]
]

dist = dijkstra(graph, 0)

print("lepsza. Odległości od wierzchołka 0:")
for i in range(len(dist)):
    print(f"{i}: {dist[i]}")


'''Złożoność czasowa: O(V^2)
Złożoność obliczeniowa: O(V+E)
1. W każdej iteracji wybierany jest nieodwiedzony wierzchołek u o najmniejszej wartości d[u]. Zaznaczamy u jako odwiedzonego.
2. Dla każdej krawędzi wychodzącej z u wykonujemy relaksację: jeśli przez u można dojść do v krótszą drogą niż znana wcześniej,
aktualizujemy d[v] i parent[v].
3. Gdy nie da się znaleźć więcej nieodwiedzonych wierzchołków z d[v] < inf, pętla się kończy.
'''

def dijkstra1(G, s):
    n = len(G)
    d = [float('inf')] * n #tablica odlegosci od s
    visited = [False] * n #czy wierzcholek odwiedzony
    parent = [None] * n #poprzednik
    d[s] = 0

    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

    while True:
        min_d = float('inf')
        u = -1
        for v in range(n):
            if not visited[v] and d[v] < min_d:
                min_d = d[v]
                u = v
        if u == -1:
            break

        visited[u] = True
        for v, w in G[u]:
            relax(u, v, w)

    return d, parent

def get_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    path.reverse()
    return path

graph = [
    [(1, 5), (2, 1)],            # 0 -> 1 (5), 0 -> 2 (1)
    [(0, 5), (2, 2), (3, 1)],
    [(0, 1), (1, 2), (3, 4), (4, 8)],
    [(1, 1), (2, 4), (4, 3)],
    [(2, 8), (3, 3)]
]

dist, prev = dijkstra1(graph, 0)

print("gorsza. Odległości od wierzchołka 0:")
for i in range(len(dist)):
    print(f"{i}: {dist[i]}")

path = get_path(prev, 4)
print("Ścieżka z 0 do 4:", path)
