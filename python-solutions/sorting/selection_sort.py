from typing import List


# compare 1 element with all
# find the smallest element in unsorted list
# second time we locate the smallest item in the list starting from the second element in the list
def selection_sort(nums: List[int]):
    l = len(nums)

    for i in range(l-1): # works with l also
        for j in range(i+1, l):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


n = [4, 5, 9, 8, 6, 7, 3, 2]
selection_sort(n)
print(n)

'''
for i in range(len(A)): 
    min_idx = i # assume first is min
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j # find mind
                      
    A[i], A[min_idx] = A[min_idx], A[i] 

'''
