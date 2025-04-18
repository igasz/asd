def countsort(T):
    N = len(T)
    M = max(T)
    count = [0]*(M+1)

    for num in T:
        count[num] += 1

    for i in range(1, M+1):
        count[i] += count[i-1]

    result = [0]*N
    for i in range(N-1, -1, -1):
        result[count[T[i]]-1] = T[i]
        count[T[i]] -= 1

    return result

T = [10, 5, 3, 4, 2]
print(countsort(T))