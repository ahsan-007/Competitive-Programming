# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/description/?envType=daily-question&envId=2026-03-16

from typing import List
import heapq


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        maxDistinctSum = []
        for size in range((len(grid) // 2) + 1):
            for i in range(size, len(grid) - size):
                for j in range(len(grid[i]) - (2 * size)):
                    if size > 0:
                        currSum = grid[i][j]
                        k = i - 1
                        l = i + 1
                        j = j + 1
                        while k >= 0 and l <= i + size:
                            currSum += grid[k][j] + grid[l][j]
                            k = k - 1
                            l = l + 1
                            j = j + 1

                        k = k + 2
                        l = l - 2
                        while k != i and l != i:
                            currSum += grid[k][j] + grid[l][j]
                            k = k + 1
                            l = l - 1
                            j = j + 1

                        currSum = currSum + grid[k][j]
                    else:
                        currSum = grid[i][j]

                    if currSum not in maxDistinctSum:
                        heapq.heappush(maxDistinctSum, currSum)
                        if len(maxDistinctSum) > 3:
                            heapq.heappop(maxDistinctSum)
        return sorted(maxDistinctSum, reverse=True)


print(Solution().getBiggestThree(grid=[[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [
      20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]))
print(Solution().getBiggestThree(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().getBiggestThree(grid=[[7, 7, 7]]))
