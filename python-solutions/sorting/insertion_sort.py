from typing import List


# similar to playing cards
# create an imaginary partition , the left side of partition you keep sorted
# create a small sorted growing list on the left side of the partition
# starting point = assume array starts from the 1st element not 0th , since only 1 element is on the left == left side
# is sorted
def insertion_sort(nums: List[int]):
    l = len(nums)

    for i in range(1, l):  # works with (0, l)
        j = i-1
        temp = nums[i]
        while temp < nums[j] and j >= 0:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = temp


n = [4, 5, 9, 8, 6, 7, 3, 2]
insertion_sort(n)
print(n)
