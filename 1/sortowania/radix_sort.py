def radixsort(T):
    max1 = max(T)
    exp = 1
    while max1/exp >= 1:
        countingsort(T, exp)
        exp *= 10

def countingsort(T, exp1):
    n = len(T)
    output = [0]*n
    count = [0]*10

    for i in range(0, n):
        idx = T[i]//exp1
        count[idx%10] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n-1
    while i>=0:
        idx = T[i]//exp1
        output[count[idx%10]-1] = T[i]
        count[idx%10] -= 1
        i -= 1

    for i in range(0, n):
        T[i] = output[i]

T = [10, 5, 3, 4, 2]
radixsort(T)
print(T)