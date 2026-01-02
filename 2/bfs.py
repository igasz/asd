'''Złożenie czasowe: O(V + E)
1.Start z węzła początkowego
2. Odwiedź ten węzeł i oznacz jako odwiedzony.
3. Dodaj sąsiadów tego węzła do kolejki.
4. Powtarzaj:
- Z kolejki zdejmij pierwszy węzeł.
- Jeśli nie był odwiedzony — oznacz go i dodaj jego sąsiadów do kolejki.
5. Kończysz, gdy kolejka będzie pusta lub znajdziesz to, czego szukasz (np. dany węzeł).
Zastosowania:
- Znajdowanie najkrótszej ścieżki w grafach bez wag (np. w labiryntach).
- Sprawdzanie spójności grafu.'''

def bfs(G, s):
    n = len(G)
    visited = [False] * n
    visited[s] = True
    queue = [s]
    while queue:
        u = queue.pop(0)
        if not visited[u]:
            visited[u] = True
            for v in G[u]:
                if not visited[v]:
                    queue.append(v)
    return visited

graph = {
  5 : [3,7],
  3 : [2, 4],
  7 : [8],
  2 : [],
  4 : [8],
  8 : []
}

print(bfs(graph, 5))