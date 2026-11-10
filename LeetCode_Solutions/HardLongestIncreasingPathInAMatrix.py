"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""

class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        def lisp(i, j, memo, matrix):
            
            if memo[i][j] > 0:
                return memo[i][j]
            

            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i = i + di
                new_j = j + dj

                if not (0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0])) or not (matrix[new_i][new_j] > matrix[i][j]) :
                    continue

                memo[i][j] = max(memo[i][j], lisp(new_i, new_j, memo, matrix))
            
            memo[i][j] += 1

            return memo[i][j] 

        
        
        memo = [[0]*(len(matrix[0])) for _ in range(len(matrix))]

        max_path = 0
        for i in range(len(matrix)):

            for j in range(len(matrix[0])):

                max_path = max(max_path, lisp(i, j, memo, matrix))

        return max_path