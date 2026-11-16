"""
279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, 
it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.


"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")]*(n + 1)
        dp[0] = 0
        i = 0
        while i < n + 1:
            pow = 1
            while i + pow*pow < n + 1:
                dp[i + pow*pow] = min(dp[i + pow*pow], dp[i] + 1)
                pow += 1

            i += 1

        return dp[-1]