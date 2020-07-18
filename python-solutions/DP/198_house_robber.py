from typing import List


# In DP, you need 3 things:
# 1. base condition
# 2. create an array
# 3. make an equation
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 0:
            return 0

        if size == 1:
            return nums[0]

        house = [0] * size
        house[0] = nums[0]
        house[1] = max(nums[0], nums[1])

        for i in range(2, size):
            house[i] = max(nums[i] + house[i - 2], house[i - 1])

        return house[-1]
