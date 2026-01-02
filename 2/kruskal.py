'''Złożoność czasowa: O(E log E)
1. Sortujemy wszystkie krawędzie w grafie rosnąco według ich wag
2. tworzymy zbiór rozłączny (Union-Find) dla każdego wierzchołka
3. Przechodzimy przez posortowane krawędzie:
Dla każdej krawędzi (waga, u, v):
Jeśli u i v należą do różnych zbiorów, dodaj tę krawędź do MST i połącz zbiory.
Jeśli są w tym samym zbiorze, pomijamy (bo utworzyłby się cykl).
4. Powtarzamy krok 3, aż MST zawiera dokładnie n-1 krawędzi (dla n wierzchołków).
find(x) – znajdź reprezentanta zbioru
union(x, y) – połącz dwa zbiory'''

class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
    return True


def kruskal(nodes, edges):
    mst = []
    edges.sort()

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((weight, u.value, v.value))

    return mst

if __name__ == "__main__":
    a, b, c, d, e = Node('A'), Node('B'), Node('C'), Node('D'), Node('E')
    nodes = [a, b, c, d, e]

    edges = [
        (1, a, b),
        (3, a, c),
        (4, b, c),
        (2, b, d),
        (5, c, d),
        (7, c, e),
        (6, d, e)
    ]

    mst = kruskal(nodes, edges)
    print("Minimalne drzewo rozpinające (MST):")
    for weight, u, v in mst:
        print(f"{u} -- {v} == {weight}")