# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal_sum = 0
        for i in range(len(mat)):
            diagonal_sum = diagonal_sum + mat[i][i]

        row = 0
        col = len(mat) - 1
        while row < len(mat):
            if row != col:
                diagonal_sum = diagonal_sum + mat[row][col]
            row = row + 1
            col = col - 1
        return diagonal_sum


print(Solution().diagonalSum(mat=[[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]]))

print(Solution().diagonalSum(mat=[[1, 1, 1, 1],
                                  [1, 1, 1, 1],
                                  [1, 1, 1, 1],
                                  [1, 1, 1, 1]]))

print(Solution().diagonalSum(mat=[[5]]))
