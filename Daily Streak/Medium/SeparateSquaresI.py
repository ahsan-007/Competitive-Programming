# https://leetcode.com/problems/separate-squares-i/editorial/?envType=daily-question&envId=2026-01-13

from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def getAreaUnder(y):
            area = 0
            for square in squares:
                _, y1, s = square
                if y1 < y:
                    area += s * min(s, y - y1)
            return area

        def binarySearch(lb, ub, totalArea):
            if lb > ub:
                return float("+inf")

            mid = lb + (ub - lb) / 2
            areaUnderY = getAreaUnder(mid)
            if ((totalArea / 2) - 1e5) <= areaUnderY <= ((totalArea / 2) + 1e5):
                return min(mid, binarySearch(lb, mid, totalArea))

            elif areaUnderY < (totalArea / 2):
                return binarySearch(mid, ub, totalArea)

            return binarySearch(lb, mid, totalArea)

        maxY = float("-inf")
        totalArea = 0
        for square in squares:
            maxY = max(maxY, square[1] + square[2])
            totalArea += square[2] ** 2

        lb = 0
        ub = maxY
        while abs(ub - lb) > 1e-5:
            mid = lb + (ub - lb) / 2
            area = getAreaUnder(mid)
            if area >= (totalArea / 2):
                ub = mid
            else:
                lb = mid
        return ub


print(Solution().separateSquares(squares=[[0, 0, 1], [2, 2, 1]]))
print(Solution().separateSquares(squares=[[0, 0, 2], [1, 1, 1]]))
print(Solution().separateSquares(squares=[[15, 20, 10], [8, 15, 9]]))
