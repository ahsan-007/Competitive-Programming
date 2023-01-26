# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        memo = {}
        min_cost = None
        for j in range(0, len(grid[0])):
            if min_cost is None:
                min_cost = self.minPathCostUtil(0, j, grid, moveCost, memo)
            else:
                min_cost = min(min_cost, self.minPathCostUtil(
                    0, j, grid, moveCost, memo))
        return min_cost

    def minPathCostUtil(self, i, j,  grid: List[List[int]], moveCost: List[List[int]], memo) -> int:
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(grid)-1:
            return grid[i][j]

        min_cost = None
        for k in range(len(grid[i+1])):
            if min_cost is None:
                min_cost = moveCost[grid[i][j]][k] + \
                    self.minPathCostUtil(i+1, k, grid, moveCost, memo)
            else:
                min_cost = min(min_cost, moveCost[grid[i][j]][k] +
                               self.minPathCostUtil(i+1, k, grid, moveCost, memo))
        memo[(i, j)] = min_cost + grid[i][j]
        return memo[(i, j)]


print(Solution().minPathCost([[5, 3], [4, 0], [2, 1]], [
      [9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]))

print(Solution().minPathCost([[5, 1, 2], [4, 0, 3]], [[12, 10, 15], [20, 23, 8], [21, 7, 1], [8, 1, 13], [9, 10, 25], [5, 3, 2]]))
