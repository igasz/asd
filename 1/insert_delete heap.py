'''Proszę zaimplementować operację wstawiania elementu do kopca binarnego'''
#left(i) = 2i+1
#right(i) = 2i
#parent(i) = podloga(i-1/2)

def parent(i):
    return (i - 1) // 2

def heapify(T, n, i):
    L = 2*i+1
    R = 2*i+2
    max_i = i
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

def insertion(T, key):
    T.append(key)
    n = len(T)
    i = n - 1
    while i > 0 and T[parent(i)] < T[i]:
        T[i], T[parent(i)] = T[parent(i)], T[i]
        i = parent(i)

def deleteroot(T):
    n = len(T)
    last = T[n-1]
    T[0] = last
    n = n-1
    heapify(T, n, 0)

def deletionidx(T, idx):
    n = len(T)
    if n == 0 and idx >= n:
        return
    T[idx], T[-1] = T[-1], T[idx]
    T.pop()
    if idx<len(T):
        p = parent(idx)
        if idx>0 and T[p] < T[idx]:
            T[p], T[idx] = T[idx], T[p]
            idx = parent(idx)
        else:
            heapify(T, len(T), idx)


T = [10, 5, 3, 2, 4]
n = len(T)
key = 15

#deleteroot(T)
deletionidx(T, 2)
#insertion(T, key)
print(T)

