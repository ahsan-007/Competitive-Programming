# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=daily-question&envId=2024-03-18

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        i = 0
        arrows = 0
        start = float("+inf")
        end = float("-inf")
        while i < len(points):
            if start <= points[i][0] <= end or start <= points[i][1] <= end:
                start = max(start, points[i][0])
                end = min(end, points[i][1])
            else:
                start = points[i][0]
                end = points[i][1]
                arrows = arrows + 1
            i = i + 1
        return arrows

    def findMinArrowShotsV2(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 0
        print(points)
        end = float("-inf")
        i = 0
        while i < len(points):
            if points[i][0] > end:
                arrows += 1
                end = points[i][1]
            else:
                end = min(end, points[i][1])
            i = i + 1
        return arrows


print(Solution().findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
print(Solution().findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))
print(Solution().findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]))
print(Solution().findMinArrowShots(points=[[3, 9], [7, 12], [3, 8], [
      6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]))

print('-'*100)

print(Solution().findMinArrowShotsV2(
    points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
print(Solution().findMinArrowShotsV2(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))
print(Solution().findMinArrowShotsV2(points=[[1, 2], [2, 3], [3, 4], [4, 5]]))
print(Solution().findMinArrowShotsV2(points=[[3, 9], [7, 12], [3, 8], [
      6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]))
