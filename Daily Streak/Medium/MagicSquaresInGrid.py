# https://leetcode.com/problems/magic-squares-in-grid/description/?envType=daily-question&envId=2025-12-30

from typing import List
from enum import Enum

MAGIC_SQUARE_SIZE = 3


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def getColumnSum(c, i):
            return sum(grid[k][c] for k in range(i, i + MAGIC_SQUARE_SIZE))

        def getRowSum(r, i):
            return sum(grid[r][i:i + MAGIC_SQUARE_SIZE])

        def getDiagonalSum(r, c, isForward):
            diagonalSum = 0
            for i in range(MAGIC_SQUARE_SIZE):
                diagonalSum += grid[r][c]
                r = r + 1
                c = c + (-1 if isForward else 1)
            return diagonalSum

        count = 0
        for i in range(len(grid) - (MAGIC_SQUARE_SIZE - 1)):
            for j in range(len(grid[i]) - (MAGIC_SQUARE_SIZE - 1)):
                elements = [*grid[i][j:j+MAGIC_SQUARE_SIZE],
                            *grid[i+1][j:j+MAGIC_SQUARE_SIZE],
                            *grid[i+2][j:j+MAGIC_SQUARE_SIZE]]
                if len(set(elements)) == len(elements) and all(1 <= ele <= 9 for ele in elements):
                    square = [
                        getRowSum(i, j),
                        getRowSum(i + 1, j),
                        getRowSum(i + 2, j),
                        getColumnSum(j, i),
                        getColumnSum(j+1, i),
                        getColumnSum(j+2, i),
                        getDiagonalSum(i, j + MAGIC_SQUARE_SIZE-1, True),
                        getDiagonalSum(i, j, False)
                    ]
                    if all(square[i] == square[i-1] for i in range(1, len(square))):
                        count += 1
        return count

print(Solution().numMagicSquaresInside(
    grid=[[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
print(Solution().numMagicSquaresInside(grid=[[8]]))
