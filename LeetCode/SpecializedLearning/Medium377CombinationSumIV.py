"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

"""



"""

1,  1,  2,  4,  7


"""


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:

        dp = [0]*(target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]

        return dp[-1]
        