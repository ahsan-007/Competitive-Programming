# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/?envType=daily-question&envId=2025-08-26

from typing import List
import math


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        def getArea(dimension):
            return dimension[0] * dimension[1]

        maxDiagonalRectInd = 0
        maxDiagonal = 0
        for i in range(len(dimensions)):
            currDiagonal = math.sqrt(
                math.pow(dimensions[i][0], 2) + math.pow(dimensions[i][1], 2))

            if (i == 0 or
                maxDiagonal < currDiagonal or
                    (maxDiagonal == currDiagonal and
                     getArea(dimensions[maxDiagonalRectInd]) < getArea(dimensions[i]))
                ):

                maxDiagonalRectInd = i
                maxDiagonal = currDiagonal

        return getArea(dimensions[maxDiagonalRectInd])


print(Solution().areaOfMaxDiagonal(dimensions=[[9, 3], [8, 6]]))
print(Solution().areaOfMaxDiagonal(dimensions=[[3, 4], [4, 3]]))
