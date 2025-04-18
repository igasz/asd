def merge(T):
    N = len(T)
    if N > 1:
        left_T = T[:N//2]
        right_T = T[N//2:]

        merge(left_T)
        merge(right_T)

        i = 0 #left_T idx
        j = 0 #right_T idx
        k = 0 #merged_T idx
        while i < len(left_T) and j < len(right_T):
            if left_T[i] < right_T[j]:
                T[k] = left_T[i]
                i += 1
            else:
                T[k] = right_T[j]
                j += 1
            k += 1

        while i < len(left_T):
            T[k] = left_T[i]
            i += 1
            k += 1

        while j < len(right_T):
            T[k] = right_T[j]
            j += 1
            k += 1
    return T

T = [10, 5, 3, 4, 2]
print(merge(T))