def max_subsum(T):
    n = len(T)
    best =  float('-inf')
    current = T[0]

    for i in range(1, n):
        current = max(T[i], current+T[i])
        best = max(current, best)

    return best

T = [2, 3, -8, 7, -1, 2, 3]
print(max_subsum(T))