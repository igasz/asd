'''zaimplementować algorytm wyszukujący w grafie cykl Eulera (macierzowa)'''
#krawedzie

def euler_cycle(G, s):
    n = len(G)
    idx = [0] * n
    euler = []
    for u in range(n): #czy parzysty stopień
        if sum(G[u])%2 != 0:
            return None

    def euler_visit(u):
        while idx[u] < n:
            v = idx[u]
            idx[u] += 1
            if G[u][v] > 0:
                G[u][v] -= 1
                G[v][u] -= 1
                euler_visit(v)
        euler.append(u)

    euler_visit(s)
    return euler

G = [
    [0, 1, 1, 0],  # 0
    [1, 0, 0, 1],  # 1
    [1, 0, 0, 1],  # 2
    [0, 1, 1, 0]   # 3
]

start = 0
cycle = euler_cycle(G, start)
print("Euler cycle:", cycle)