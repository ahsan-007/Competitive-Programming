# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description /?envType=daily-question&envId=2026-03-23
from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        def maxProductPathUtil(grid, i, j, prod, memo):
            if i >= len(grid) or j >= len(grid[0]):
                return -1

            prod = prod * grid[i][j]

            if prod == 0:
                return 0

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return prod if prod >= 0 else -1

            if (i, j, prod) not in memo:
                memo[(i, j, prod)] = max(
                    maxProductPathUtil(grid, i + 1, j, prod, memo),
                    maxProductPathUtil(grid, i, j + 1, prod, memo),
                )
            return memo[(i, j, prod)]

        max_poduct = maxProductPathUtil(grid, 0, 0, 1, memo={})
        return (max_poduct % (pow(10, 9) + 7)) if max_poduct >= 0 else -1


print(Solution().maxProductPath(
    grid=[[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]))
print(Solution().maxProductPath(grid=[[1, -2, 1], [1, -2, 1], [3, -4, 1]]))
print(Solution().maxProductPath(grid=[[1, 3], [0, -4]]))
