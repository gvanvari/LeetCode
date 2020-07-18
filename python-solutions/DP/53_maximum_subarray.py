from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 0:
            return 0

        if size == 1:
            return nums[0]

        dp = [0] * size

        dp[0] = nums[0]
        # dp[1] = max(nums[0]+nums[1],nums[1])

        for i in range(1, size):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            # the sum is max of
            # sum so far calculated plus the current one or
            # the sum is starting from current one

        return max(dp)
