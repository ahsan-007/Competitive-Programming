# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/?envType=daily-question&envId=2026-03-18

from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i != 0 or j != 0:
                    if i == 0 or j == 0:
                        if i == 0:
                            grid[i][j] = grid[i][j] + grid[i][j-1]
                        else:
                            grid[i][j] = grid[i][j] + grid[i-1][j]
                    else:
                        grid[i][j] = grid[i-1][j] + grid[i][j-1] + \
                            grid[i][j] - grid[i-1][j-1]

                if grid[i][j] <= k:
                    count += 1
        return count


print(Solution().countSubmatrices(grid=[[7, 6, 3], [6, 6, 1]], k=18))
print(Solution().countSubmatrices(
    grid=[[7, 2, 9], [1, 5, 0], [2, 6, 6]], k=20))
