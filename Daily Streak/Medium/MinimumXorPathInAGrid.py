# https://leetcode.com/problems/minimum-xor-path-in-a-grid/description/?envType=daily-question&envId=2026-10-28

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        def minCostUtil(grid, i, j, xor, memo):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                return float("+inf")

            if i == len(grid) - 1 and j == len(grid[i]) - 1:
                return xor ^ grid[i][j]

            if (xor, i, j) not in memo:
                right_xor = minCostUtil(grid, i + 1, j, xor ^ grid[i][j], memo)
                memo[(xor, i, j)] = right_xor if right_xor == 0 else min(
                    right_xor,
                    minCostUtil(grid, i, j + 1, xor ^ grid[i][j], memo)
                )

            return memo[(xor, i, j)]

        return minCostUtil(grid, 0, 0, 0, {})


print(Solution().minCost(grid=[[1, 2], [3, 4]]))
print(Solution().minCost(grid=[[6, 7], [5, 8]]))
