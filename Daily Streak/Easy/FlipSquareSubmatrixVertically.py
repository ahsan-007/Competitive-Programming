# https://leetcode.com/problems/flip-square-submatrix-vertically/description/?envType=daily-question&envId=2026-03-21

from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        i = x
        j = x + k - 1
        while i < j:
            c = y
            while c < y + k:
                grid[i][c], grid[j][c] = grid[j][c], grid[i][c]
                c = c + 1
            i = i + 1
            j = j - 1
        return grid


print(Solution().reverseSubmatrix(grid=[[1, 2, 3, 4],
                                        [5, 6, 7, 8],
                                        [9, 10, 11, 12],
                                        [13, 14, 15, 16]],
                                  x=1, y=0, k=3))
print(Solution().reverseSubmatrix(grid=[[3, 4, 2, 3],
                                        [2, 3, 4, 2]],
                                  x=0, y=2, k=2))
