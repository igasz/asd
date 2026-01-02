'''Złożoność czasowa: O(V^3)
Złożoność pamięciowa: O(V^2)
Dla każdego wierzchołka k sprawdzamy czy ścieżka z i do j przez k jest krótsza.
Jeśli tak, aktualizujemy odległość
'''

def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]  # Kopia macierzy

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

inf = float('inf')
graph = [
    [0,   3,   inf, 5],
    [2,   0,   inf, 4],
    [inf, 1,   0,   inf],
    [inf, inf, 2,   0]
]

result = floyd_warshall(graph)

for row in result:
    print(row)
