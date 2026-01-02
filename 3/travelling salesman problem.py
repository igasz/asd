'''travelling salesman problem'''

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

'''wersja bitoniczna - miasta są w R^2 i najpierw wędrujemy tylko w prawo a potem tylko w lewo
złożoność czasowa: O(n^3)'''

def tsp_bitonic(d):
    n = len(d)
    F = [[float('inf')] * n for _ in range(n)]

    def tspf(i, j):
        if F[i][j] != float('inf'): return F[i][j]
        if i == j - 1:  # case b
            best = float('inf')
            for k in range(j - 1):
                best = min(best, tspf(k, j - 1) + d[k][j])
            F[j - 1][j] = best
        else:  # case a
            F[i][j] = tspf(i, j - 1) + d[j - 1][j]

        return F[i][j]

    F[0][1] = d[0][1]

    min_cost = float('inf')
    for k in range(n - 1):
        min_cost = min(min_cost, tspf(k, n - 1) + d[k][n - 1])

    return min_cost


print(tsp_bitonic(dist))


'''brute-force
złożoność O(n*n!)'''

def generate_permutations(A, r, l, res):
    if l == r:
        res.append(A[:])
    else:
        for i in range(l, r + 1):
            A[l], A[i] = A[i], A[l]
            generate_permutations(A, l + 1, r, res)
            A[l], A[i] = A[i], A[l]

def tsp(G):
    n = len(G)
    cities = [i for i in range(1, n)]
    all_perms = []
    generate_permutations(cities, 0, n-2, all_perms)

    min_path = float('inf')
    best = []

    for perm in all_perms:
        current = 0 #cost
        k = 0 #start
        for city in perm:
            current += G[k][city]
            k = city
        current += G[k][0]

        if current < min_path:
            min_path = current
            best = [0] + perm + [0]

    return min_path, best

print(tsp(dist))