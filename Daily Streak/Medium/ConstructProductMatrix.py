# https://leetcode.com/problems/construct-product-matrix/description/?envType=daily-question&envId=2026-03-24

from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        grid_product = [[0] * len(grid[i]) for i in range(len(grid))]

        product = 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid_product[i][j] = product
                product = (product * grid[i][j]) % 12345

        product = 1
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[i]) - 1, -1, -1):
                grid_product[i][j] = (grid_product[i][j] * product) % 12345
                product = (product * grid[i][j]) % 12345

        return grid_product


print(Solution().constructProductMatrix(grid=[[1, 2], [3, 4]]))
print(Solution().constructProductMatrix(grid=[[12345], [2], [1]]))
print(Solution().constructProductMatrix(grid=[[1, 2, 3, 4]]))
