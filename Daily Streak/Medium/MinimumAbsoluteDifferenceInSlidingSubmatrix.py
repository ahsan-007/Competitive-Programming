# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/description/?envType=daily-question&envId=2026-03-20

from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def findMinAbsDiffUtil(elements):
            if len(elements) == 1:
                return 0

            elements = sorted(elements)
            diff = float("+inf")
            for i in range(1, len(elements)):
                diff = min(diff, abs(elements[i] - elements[i-1]))
            return diff

        ans = []
        for i in range((len(grid) - k) + 1):
            differences = []
            for j in range((len(grid[i]) - k) + 1):
                elements = set()
                for row in range(i, i + k):
                    for col in range(j, j + k):
                        elements.add(grid[row][col])
                differences.append(findMinAbsDiffUtil(elements))
            ans.append(differences)
        return ans


print(Solution().minAbsDiff(grid=[[1, -2, 3], [2, 3, 5]], k=2))
print(Solution().minAbsDiff(grid=[[1, 8], [3, -2]], k=2))
print(Solution().minAbsDiff(grid=[[3, -1]], k=1))
