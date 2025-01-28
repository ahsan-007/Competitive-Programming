# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/?envType=daily-question&envId=2025-01-28

from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def findMaxFishUtil(grid, i, j, seen):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in seen or grid[i][j] == 0:
                return 0
            seen.add((i, j))
            return grid[i][j] + findMaxFishUtil(grid, i + 1, j, seen) + findMaxFishUtil(grid, i - 1, j, seen) + findMaxFishUtil(grid, i, j + 1, seen) + findMaxFishUtil(grid, i, j - 1, seen)

        seen = set()
        maxFish = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxFish = max(maxFish, findMaxFishUtil(grid, i, j, seen))
        return maxFish


print(Solution().findMaxFish(
    grid=[[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]))
print(Solution().findMaxFish(
    grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))
