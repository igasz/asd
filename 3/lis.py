#longest increasing subsequence
'''wykład'''
'''złożoność czasowa: O(n^2)
złożoność pamięciowa: O(n)'''

def lis1(A):
    n = len(A)
    F = [1] * n #F[i] oznacza długość najdłuższego rosnącego podciągu kończącego się na A[i].
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                F[i] = max(F[i], F[j] + 1)
    return max(F)

'''bin search'''
'''złożoność czasowa: O(nlogn)
złożoność pamięciowa: O(n)
Szukamy w sub pozycji, gdzie x mógłby się znaleźć (pierwsze ≥ x) – używamy binary search.'''

def binary_search(T, x):
    L, R = 0, len(T)-1
    while L <= R:
        m = L + (R - L)//2
        if T[m] > x:
            R = m - 1
        else:
            L = m + 1
    return L

def lis2(A):
    sub = [] #sub[i] to najmniejszy możliwy element kończący rosnący podciąg długości i+1.
    for x in A:
        i = binary_search(sub, x)
        if i == len(sub):
            sub.append(x)
        else:
            sub[i] = x
    return len(sub)

A = [10, 9, 2, 5, 3, 7, 101, 18]
print(lis1(A))
print(lis2(A))