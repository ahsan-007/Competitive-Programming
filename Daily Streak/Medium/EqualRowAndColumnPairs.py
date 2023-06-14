# https://leetcode.com/problems/equal-row-and-column-pairs/

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        for r in range(n):
            for c in range(n):
                similar = True
                k = 0
                while similar and k < n:
                    if grid[r][k] != grid[k][c]:
                        similar = False
                    k = k + 1
                if similar:
                    count = count + 1
        return count


print(Solution().equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
print(Solution().equalPairs(
    grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
