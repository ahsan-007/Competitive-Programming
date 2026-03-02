# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/?envType=daily-question&envId=2026-03-02
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        zeroes = [0] * len(grid)
        for i in range(len(grid)):
            j = len(grid[i]) - 1
            while j >= 0 and grid[i][j] == 0:
                zeroes[i] += 1
                j = j - 1

        swaps = 0
        i = 0
        while i < len(zeroes):
            j = i
            while j < len(zeroes) and zeroes[j] < len(zeroes) - (i + 1):
                j = j + 1

            if j == len(zeroes):
                return -1

            zeroes = zeroes[:i] + zeroes[j:j+1] + zeroes[i:j] + zeroes[j+1:]
            swaps += j - i
            i = i + 1
        return swaps


print(Solution().minSwaps(grid=[[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
print(Solution().minSwaps(
    grid=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]))
print(Solution().minSwaps(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 1]]))
print(Solution().minSwaps(
    grid=[[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]))
print(Solution().minSwaps(
    grid=[[1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0]]))
