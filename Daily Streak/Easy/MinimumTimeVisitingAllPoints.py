# https://leetcode.com/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2026-01-12

from typing import List


class Solution:
    # Time: O(N), Space: O(1)
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            time = time + \
                max(abs(points[i][0] - points[i-1][0]),
                    abs(points[i][1] - points[i-1][1]))
        return time

    # one liner
    def minTimeToVisitAllPointsV2(self, points: List[List[int]]) -> int:
        return sum(max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1])) for i in range(1, len(points))) if len(points) > 1 else 0


print(Solution().minTimeToVisitAllPoints(points=[[1, 1], [3, 4], [-1, 0]]))
print(Solution().minTimeToVisitAllPoints(points=[[3, 2], [-2, 2]]))

print('-' * 100)

print(Solution().minTimeToVisitAllPointsV2(points=[[1, 1], [3, 4], [-1, 0]]))
print(Solution().minTimeToVisitAllPointsV2(points=[[3, 2], [-2, 2]]))
