# https://leetcode.com/problems/triangle/description/

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def minmumTotalUtil(triangle, i, j, memo):
            if i >= len(triangle) or j >= len(triangle[i]) or j < 0:
                return 0

            if (i, j) not in memo:
                memo[(i, j)] = triangle[i][j] + min(minmumTotalUtil(triangle,
                                                                    i+1, j, memo), minmumTotalUtil(triangle, i+1, j+1, memo))

            return memo[(i, j)]

        return minmumTotalUtil(triangle, 0, 0, {})


print(Solution().minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(Solution().minimumTotal(triangle=[[-10]]))
