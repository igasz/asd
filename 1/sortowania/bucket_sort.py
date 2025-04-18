def insertion(T):
    N = len(T)
    for i in range(1, N):
        j = i
        while T[j-1] > T[j] and j>0:
            T[j-1], T[j] = T[j], T[j-1]
            j -= 1
    return T

def bucketsort(T):
    N = len(T)
    buckets = [[] for _ in range(N)]
    for num in T:
        bi = int(N*num)
        buckets[bi].append(num)

    for bucket in buckets:
        insertion(bucket)

    idx = 0
    for bucket in buckets:
        for num in bucket:
            T[idx] = num
            idx += 1

A = [0.12, 0.94, 0.68, 0.23, 0.55]
bucketsort(A)
arr = []
for i in range(len(A)):
    arr.append(A[i])
print(arr)