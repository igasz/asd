def selection(T):
    N = len(T)
    for i in range(N):
        mini_idx = i
        for j in range(i+1, N):
            if T[j] < T[mini_idx]:
                mini_idx = j
        T[i], T[mini_idx] = T[mini_idx], T[i]
    return T

T = [10, 5, 3, 4, 2]
print(selection(T))