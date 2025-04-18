def quicksort1(T):
    if len(T) < 2:
        return T
    else:
        pivot = T[0]
        less = [i for i in T[1:] if i <= pivot]
        greater = [i for i in T[1:] if i > pivot]
        return quicksort1(less) + [pivot] + quicksort1(greater)

T = [10, 5, 3, 4, 2]
print(quicksort1(T))

import random

def quicksort2(T, L, R):
    if L < R:
        p = partition(T, L, R)
        quicksort2(T, L, p-1)
        quicksort2(T, p+1, R)

def partition(T, left, right):
    x = random.randint(left, right)
    i = left
    pivot = T[x]
    T[x], T[right] = T[right], T[x]

    for j in range(left, right):
        if T[j] < pivot:
            T[i], T[j] = T[j], T[i]
            i += 1

    T[i], T[right] = T[right], T[i]

    return i

A = [11, 4, 6, 8, 2]
quicksort2(A, 0, len(A)-1)
print(A)