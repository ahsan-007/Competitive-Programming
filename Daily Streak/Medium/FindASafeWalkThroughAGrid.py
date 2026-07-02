# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=daily-question&envId=2026-07-02

from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        def findSafeWalk(grid, i, j, health, memo):
            if i >= len(grid) or j >= len(grid[i]) or i < 0 or j < 0 or health == 0 or grid[i][j] is None:
                return False

            if i == len(grid) - 1 and j == len(grid[i]) - 1 and health - (1 if grid[i][j] == 1 else 0) > 0:
                return True

            key = (i, j, health)
            if key not in memo:
                if grid[i][j] == 1:
                    health = health - 1

                val = grid[i][j]
                grid[i][j] = None
                memo[key] = (findSafeWalk(grid, i + 1, j, health, memo) or
                             findSafeWalk(grid, i - 1, j, health, memo) or
                             findSafeWalk(grid, i, j + 1, health, memo) or
                             findSafeWalk(grid, i, j - 1, health, memo))
                grid[i][j] = val
            return memo[key]
        memo = {}
        return findSafeWalk(grid, 0, 0, health, memo)


print(Solution().findSafeWalk(
    grid=[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], health=1))
print(Solution().findSafeWalk(grid=[[0, 1, 1, 0, 0, 0], [
      1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]], health=3))
print(Solution().findSafeWalk(
    grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], health=5))
