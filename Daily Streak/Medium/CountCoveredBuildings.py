# https://leetcode.com/problems/count-covered-buildings/description/?envType=daily-question&envId=2025-12-11

from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        coveredXAxis = {}
        coveredYAxis = {}
        for building in buildings:
            x, y = building
            if x not in coveredXAxis:
                coveredXAxis[x] = [y, y]
            else:
                if y < coveredXAxis[x][0]:
                    coveredXAxis[x][0] = y
                elif y > coveredXAxis[x][1]:
                    coveredXAxis[x][1] = y

            if y not in coveredYAxis:
                coveredYAxis[y] = [x, x]
            else:
                if x < coveredYAxis[y][0]:
                    coveredYAxis[y][0] = x
                elif x > coveredYAxis[y][1]:
                    coveredYAxis[y][1] = x

        coveredBuidings = 0
        for building in buildings:
            x, y = building
            if coveredXAxis[x][0] < y < coveredXAxis[x][1] and coveredYAxis[y][0] < x < coveredYAxis[y][1]:
                coveredBuidings += 1
        return coveredBuidings


print(Solution().countCoveredBuildings(
    n=3, buildings=[[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]))
print(Solution().countCoveredBuildings(
    n=3, buildings=[[1, 1], [1, 2], [2, 1], [2, 2]]))
print(Solution().countCoveredBuildings(
    n=5, buildings=[[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]))
