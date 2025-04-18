def binary_search(T, x):
    L, R = 0, len(T)-1
    while L <= R:
        m = L + (R - L)//2
        if T[m] > x:
            R = m - 1
        elif T[m] < x:
            L = m + 1
        else:
            return m
    return -1

T = [-1, 0, 3, 5, 9, 12]
x = 9
print(binary_search(T, x))