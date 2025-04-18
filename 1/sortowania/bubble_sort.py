def bubble(T):
    N = len(T)
    for i in range(N):
        for j in range(i+1, N):
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]
    return T

T = [10, 5, 3, 4, 2]
print(bubble(T))