# https://leetcode.com/problems/number-of-islands/description /?envType=daily-question&envId=2024-04-19

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def numIslandsUtil(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != "1":
                return 0

            if grid[i][j] == "1":
                grid[i][j] = "-1"

            return numIslandsUtil(grid, i+1, j) + numIslandsUtil(grid, i-1, j) + numIslandsUtil(grid, i, j + 1) + numIslandsUtil(grid, i, j-1) + abs(int(grid[i][j]))

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if numIslandsUtil(grid, i, j) > 0:
                    count += 1
        return count


print(Solution().numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(Solution().numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
