from typing import List


# comparing 2 adjacent elements, biggest value will settle at the bottom
def bubble_sort(nums: List[int]):
    l = len(nums)

    for i in range(l):
        for j in range(l-1-i):  # works with l-1 also
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


n = [4, 5, 9, 8, 6, 7, 3, 2]
bubble_sort(n)
print(n)
