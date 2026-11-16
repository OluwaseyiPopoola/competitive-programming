"""
https://leetcode.com/problems/count-servers-that-communicate/
"""

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        
        rowServer = [grid[i][0] for i in range(len(grid))]
        colServer = [grid[0][j] for j in range(len(grid[0]))]

        for j in range(1, len(grid[0])):
            for i in range(len(rowServer)):
                rowServer[i] += grid[i][j]

        for i in range(1, len(grid)):
            for j in range(len(colServer)):
                colServer[j] += grid[i][j]

        res = 0



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or (rowServer[i] < 2 and colServer[j] < 2) : 
                    continue 
                
                res += 1
                

        return res

        




        