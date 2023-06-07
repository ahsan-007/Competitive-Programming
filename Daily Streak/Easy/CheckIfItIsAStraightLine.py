# https://leetcode.com/problems/check-if-it-is-a-straight-line/

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # To check if points lie on a straight line we can compare slope
        # For Example: if there are three points P1, P2 and P3, we can compare slope of P1, P2 and slope of P1, P3
        # m1 = deltaY(P1, P2) / deltaX(P1, P2)
        # m2 = deltaY(P1, P3) / deltaX(P1, P3)
        # if m1 == m2 then points lie on the same line
        # if x is 0 or deltaX is 0, calculation of slope can result in division by zero error
        # so instead of division, it can be converted to multiplication
        # Points lie on same line if m1 == m2
        #                            deltaY1 / deltaX1 == deltaY2 / deltaX2
        #                            deltaY1 * deltaX2 == deltaY2 * deltaX1
        deltaX = coordinates[1][0] - coordinates[0][0]
        deltaY = coordinates[1][1] - coordinates[0][1]
        for i in range(2, len(coordinates)):
            if deltaX * (coordinates[i][1] - coordinates[0][1]) != deltaY * (coordinates[i][0] - coordinates[0][0]):
                return False
        return True


print(Solution().checkStraightLine(coordinates=[
      [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))

print(Solution().checkStraightLine(coordinates=[
      [1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))

print(Solution().checkStraightLine(coordinates=[[0, 0], [0, 1], [0, -1]]))
print(Solution().checkStraightLine(coordinates=[[2, 1], [4, 2], [6, 3]]))
print(Solution().checkStraightLine(coordinates=[[2, 4], [2, 5], [2, 8]]))
