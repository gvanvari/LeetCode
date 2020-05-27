from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        return_index = [None] * 2

        for i in range(len(nums)):
            diff = target - nums[i];
            if diff not in m:
                m[nums[i]] = i
            else:
                return_index[0] = m[diff]
                return_index[1] = i
                break
        return return_index