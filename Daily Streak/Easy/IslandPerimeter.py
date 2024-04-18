# https://leetcode.com/problems/island-perimeter/description /?envType=daily-question&envId=2024-04-18

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def islandPerimeterUtil(i, j, dir, visited=set()):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0 or grid[i][j] == -1:
                return 0

            if (i, j) in visited:
                return 0

            visited.add((i, j))

            perimeter = sum([
                islandPerimeterUtil(i+1, j, 'D', visited) if dir != 'U' else 0,
                islandPerimeterUtil(i-1, j, 'U', visited) if dir != 'D' else 0,
                islandPerimeterUtil(i, j+1, 'R', visited) if dir != 'L' else 0,
                islandPerimeterUtil(i, j-1, 'L', visited) if dir != 'R' else 0,
                1 if i == len(grid)-1 or grid[i+1][j] == 0 else 0,
                1 if i == 0 or grid[i-1][j] == 0 else 0,
                1 if j == len(grid[i])-1 or grid[i][j+1] == 0 else 0,
                1 if j == 0 or grid[i][j-1] == 0 else 0,
            ])

            return perimeter

        def findLand():
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 1:
                        return i, j
        i, j = findLand()
        return islandPerimeterUtil(i, j, '')

    def islandPerimeterV2(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    perimeter = perimeter + sum([
                        1 if i == len(grid)-1 or grid[i+1][j] == 0 else 0,
                        1 if i == 0 or grid[i-1][j] == 0 else 0,
                        1 if j == len(grid[i])-1 or grid[i][j+1] == 0 else 0,
                        1 if j == 0 or grid[i][j-1] == 0 else 0])
        return perimeter


print(Solution().islandPerimeter(
    grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))

print(Solution().islandPerimeter(grid=[[1, 1], [1, 1]]))

print(Solution().islandPerimeterV2(
    grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))

print(Solution().islandPerimeterV2(grid=[[1, 1], [1, 1]]))
