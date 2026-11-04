"""
https://leetcode.com/problems/valid-sudoku/?envType=problem-list-v2&envId=array

"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                seen = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] == ".":
                            continue
                        if board[k][l] in seen:
                            print(k, l)
                            return False
                        seen.add(board[k][l])

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    print(i, j)
                    return False
                seen.add(board[i][j])

        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    print(i, j)
                    return False
                seen.add(board[i][j])

        return True