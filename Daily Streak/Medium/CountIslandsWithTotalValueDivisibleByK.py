# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/description/?envType=daily-question&envId=2026-10-26

from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def getIslandSum(grid, i, j, visited):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0 or visited[i][j]:
                return 0

            visited[i][j] = True

            return grid[i][j] + getIslandSum(grid, i + 1, j, visited) + getIslandSum(grid, i - 1, j, visited) + getIslandSum(grid, i, j + 1, visited) + getIslandSum(grid, i, j - 1, visited)

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                island_sum = getIslandSum(grid, i, j, visited)
                if island_sum != 0 and island_sum % k == 0:
                    count += 1
        return count


print(Solution().countIslands(grid=[[0, 2, 1, 0, 0], [0, 5, 0, 0, 5], [
      0, 0, 1, 0, 0], [0, 1, 4, 7, 0], [0, 2, 0, 0, 8]], k=5))
print(Solution().countIslands(
    grid=[[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], k=3))
