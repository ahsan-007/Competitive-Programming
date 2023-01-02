# https://leetcode.com/problems/minimum-path-sum/

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.minPathSumR(grid, 0, 0)

    def minPathSumR(self, grid, i, j, computed_sums={}):
        if i == len(grid) - 1 and j == len(grid[i])-1:
            return grid[i][j]
        if i >= len(grid) or j >= len(grid[i]):
            return -1
        if (i, j) not in computed_sums:
            computed_sums[(i, j)] = {"right": self.minPathSumR(grid, i+1, j, computed_sums),
                                     "down": self.minPathSumR(grid, i, j+1, computed_sums)}

        # print(sum_left, sum_right)
        if computed_sums[(i, j)]["right"] == -1 and computed_sums[i, j]["down"] == -1:
            return -1
        if computed_sums[(i, j)]["right"] == -1:
            return grid[i][j] + computed_sums[(i, j)]["down"]
        elif computed_sums[(i, j)]["down"] == -1:
            return grid[i][j] + computed_sums[(i, j)]["right"]
        else:
            return grid[i][j] + computed_sums[(i, j)]["right"] if computed_sums[(i, j)]["right"] < computed_sums[(i, j)]["down"] else grid[i][j] + computed_sums[(i, j)]["down"]
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     i = j = 0
    #     sum = 0
    #     while i < len(grid) and j < len(grid[i]):
    #         sum = sum + grid[i][j]
    #         if i == len(grid) - 1:
    #             j = j + 1
    #         elif j == len(grid) - 1:
    #             i = i + 1
    #         else:
    #             if grid[i+1][j] < grid[i][j+1]:
    #                 i = i + 1
    #             else:
    #                 j = j + 1
    #     return sum


# print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(Solution().minPathSum([[1,2,3],[4,5,6]]))
