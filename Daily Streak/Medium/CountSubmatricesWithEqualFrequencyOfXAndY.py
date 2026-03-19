# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description/?envType=daily-question&envId=2026-03-19

from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'X':
                    grid[i][j] = [1, 0]
                elif grid[i][j] == 'Y':
                    grid[i][j] = [0, 1]
                else:
                    grid[i][j] = [0, 0]

                if i > 0:
                    grid[i][j][0] += grid[i-1][j][0]
                    grid[i][j][1] += grid[i-1][j][1]
                if j > 0:
                    grid[i][j][0] += grid[i][j-1][0]
                    grid[i][j][1] += grid[i][j-1][1]

                if i > 0 and j > 0:
                    grid[i][j][0] -= grid[i-1][j-1][0]
                    grid[i][j][1] -= grid[i-1][j-1][1]

                if grid[i][j][0] > 0 and grid[i][j][0] == grid[i][j][1]:
                    count += 1
        return count


print(Solution().numberOfSubmatrices(grid=[["X", "Y", "."], ["Y", ".", "."]]))
print(Solution().numberOfSubmatrices(grid=[["X", "X"], ["X", "Y"]]))
