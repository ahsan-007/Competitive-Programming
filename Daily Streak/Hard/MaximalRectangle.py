# https://leetcode.com/problems/maximal-rectangle/description/?envType=daily-question&envId=2026-01-11

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def getMaxRectangleArea(arr):
            area = 0
            for i in range(len(arr)):
                area = max(area, arr[i])
                minVal = float("+inf")
                for j in range(i, len(arr)):
                    minVal = min(arr[j], minVal)
                    area = max(area, (j - i + 1) * minVal)
            return area

        rectangle = []
        maxArea = 0
        for row in matrix:
            if not rectangle:
                rectangle.extend([int(ele) for ele in row])
            else:
                for i in range(len(row)):
                    rectangle[i] = (rectangle[i] + int(row[i])
                                    )if row[i] != "0" else 0
            maxArea = max(maxArea, getMaxRectangleArea(rectangle))
        return maxArea


print(Solution().maximalRectangle(
    matrix=[["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]]))
print(Solution().maximalRectangle(matrix=[["0"]]))
print(Solution().maximalRectangle(matrix=[["1"]]))
