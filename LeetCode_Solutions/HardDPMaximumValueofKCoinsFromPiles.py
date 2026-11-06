"""
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
"""

class Solution:  # TLE ^(0_^_0)^
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        def mValHelper(state, k, memo, piles):
            tupledState = tuple(state)

            if tupledState in memo:
                return memo[tupledState]

            maxPath = 0
            for i in range(len(state)):
                if state[i] > len(piles[i]) - 1:
                    continue

                j = state[i]
                val = piles[i][j]

                state[i] += 1

                if k - 1 > 0:
                    val += mValHelper(state, k - 1, memo, piles)
      
                maxPath = max(maxPath, val)

                state[i] -= 1

            memo[tupledState] = maxPath
            return memo[tupledState]

        
        n = len(piles) # 2
        memo = {}
        state = [0]*n # [0 ,0]
        return mValHelper(state, k, memo, piles)
        