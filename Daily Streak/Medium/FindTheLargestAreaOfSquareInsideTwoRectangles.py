# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description/?envType=daily-question&envId=2026-01-17

from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        maxSide = 0
        for i in range(len(bottomLeft)):
            for j in range(i + 1, len(topRight)):
                w = min(topRight[i][0], topRight[j][0]) - \
                    max(bottomLeft[i][0], bottomLeft[j][0])
                l = min(topRight[i][1], topRight[j][1]) - \
                    max(bottomLeft[i][1], bottomLeft[j][1])
                maxSide = max(maxSide, min(l, w))
        return maxSide * maxSide


print(Solution().largestSquareArea(
    bottomLeft=[[1, 1], [2, 2], [3, 1]],
    topRight=[[3, 3], [4, 4], [6, 6]])
)

print(Solution().largestSquareArea(
    bottomLeft=[[1, 1], [1, 3], [1, 5]],
    topRight=[[5, 5], [5, 7], [5, 9]]))

print(Solution().largestSquareArea(
    bottomLeft=[[1, 1], [2, 2], [1, 2]],
    topRight=[[3, 3], [4, 4], [3, 4]]))

print(Solution().largestSquareArea(
    bottomLeft=[[1, 1], [3, 3], [3, 1]],
    topRight=[[2, 2], [4, 4], [4, 2]]))

print(Solution().largestSquareArea(
    bottomLeft=[[1, 2], [1, 2]],
    topRight=[[4, 5], [2, 3]]))

print(Solution().largestSquareArea(
    bottomLeft=[[1, 3], [4, 3]],
    topRight=[[5, 4], [5, 5]]))

print(Solution().largestSquareArea(
    bottomLeft=[[1, 4], [1, 1], [3, 8]],
    topRight=[[6, 9], [6, 4], [8, 10]]))

print(Solution().largestSquareArea(
    bottomLeft=[[2, 1], [4, 3]],
    topRight=[[4, 4], [5, 4]]))

print(Solution().largestSquareArea(
    bottomLeft=[[2, 2], [2, 3]],
    topRight=[[4, 3], [3, 4]]))
