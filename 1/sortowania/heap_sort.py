def parent(i):
    return (i - 1) // 2

def heapify(T, n, i):
    L = 2 * i + 1
    R = 2 * i + 2
    max_i =  i
    if L < n and T[L] > T[max_i]:
        max_i = L
    if R < n and T[R] > T[max_i]:
        max_i = R
    if max_i != i:
        T[i], T[max_i] = T[max_i], T[i]
        heapify(T, n, max_i)

def buildheap(T):
    n = len(T)
    for i in range(parent(n-1), -1, -1):
        heapify(T, n, i)

def heapsort(T):
    n = len(T)
    buildheap(T)
    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)

T = [4, 10, 3, 5, 1]
heapsort(T)
print(T)