'''find kth largest'''
import random

def findKthLargest1(nums, k):
    k = len(nums) - k

    def quickSelect(left, right):
        pivot = nums[right]
        i = left
        j = right

        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if k <= j:
            return quickSelect(left, j)
        elif k >= i:
            return quickSelect(i, right)
        else:
            return nums[k]

    return quickSelect(0, len(nums) - 1)

def findKthLargest2(nums, k):
    k = len(nums) - k

    def quickselect(l, r):
       pivot_idx = random.randint(l, r)
       pivot = nums[pivot_idx]
       nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
       p = l
       for i in range(l, r):
            if nums[i] <= pivot:
                 nums[p], nums[i] = nums[i], nums[p]
                 p += 1
       nums[p], nums[r] = nums[r], nums[p]

       if p > k:
            return quickselect(l, p - 1)
       elif p < k:
            return quickselect(p + 1, r)
       else:
            return nums[p]

    return quickselect(0, len(nums) - 1)

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest1(nums, k))
print(findKthLargest2(nums, k))