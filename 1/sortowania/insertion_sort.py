def insertion(T):
    N = len(T)
    for i in range(1, N):
        j = i
        while T[j-1] > T[j] and j>0:
            T[j-1], T[j] = T[j], T[j-1]
            j -= 1
    return T

T = [10, 5, 3, 4, 2]
print(insertion(T))