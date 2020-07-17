from typing import List


# In merge sort, the divide step does hardly anything, and all the real work happens in the combine step
def merge_sort(nums: List[int]):
    if len(nums) > 1:
        mid = len(nums) // 2  # Finding the mid of the array
        L = nums[:mid]  # Dividing the array elements
        R = nums[mid:]  # into 2 halves

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1


n = [4, 5, 9, 8, 6, 7, 3, 2]
merge_sort(n)
print(n)

'''
# only works if both lists are sorted
def merge_sort(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_len = len(nums1)
    nums2_len = len(nums2)

    k = i = j = 0

    nums3 = [0] * (nums1_len + nums2_len)

    while i < nums1_len and j < nums2_len:
        if nums1[i] < nums2[j]:
            nums3[k] = nums1[i]
            k += 1
            i += 1
        elif nums1[i] > nums2[j]:
            nums3[k] = nums2[j]
            k += 1
            j += 1
        elif nums1[i] == nums2[j]:
            nums3[k] = nums1[i]
            k += 1
            i += 1
            nums3[k] = nums2[j]
            k += 1
            j += 1

    if i < nums1_len:
        while i < nums1_len:
            nums3[k] = nums1[i]
            k += 1
            i += 1

    if j < nums2_len:
        while j < nums2_len:
            nums3[k] = nums2[j]
            k += 1
            j += 1

    return nums3

'''