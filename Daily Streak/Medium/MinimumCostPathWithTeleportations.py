# https://leetcode.com/problems/minimum-cost-path-with-teleportations/description/?envType=daily-question&envId=2026-01-28

from typing import List


class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        points = [(i, j) for i in range(m) for j in range(n)]
        points.sort(key=lambda p: grid[p[0]][p[1]])
        costs = [[float("inf")] * n for _ in range(m)]
        for t in range(k + 1):
            minCost = float("inf")
            j = 0
            for i in range(len(points)):
                minCost = min(minCost, costs[points[i][0]][points[i][1]])
                if (
                    i + 1 < len(points)
                    and grid[points[i][0]][points[i][1]]
                    == grid[points[i + 1][0]][points[i + 1][1]]
                ):
                    i += 1
                    continue
                for r in range(j, i + 1):
                    costs[points[r][0]][points[r][1]] = minCost
                j = i + 1
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if i == m - 1 and j == n - 1:
                        costs[i][j] = 0
                        continue
                    if i != m - 1:
                        costs[i][j] = min(
                            costs[i][j], costs[i + 1][j] + grid[i + 1][j]
                        )
                    if j != n - 1:
                        costs[i][j] = min(
                            costs[i][j], costs[i][j + 1] + grid[i][j + 1]
                        )
        return costs[0][0]


print(Solution().minCost(grid=[[1, 3, 3], [2, 5, 4], [4, 3, 5]], k=2))
print(Solution().minCost(grid=[[1, 2], [2, 3], [3, 4]], k=1))
print(Solution().minCost(grid=[[6, 7, 1, 20, 11], [4, 5, 18, 23, 28]], k=3))
print(Solution().minCost(grid=[[8, 10, 14, 23, 26, 34], [34, 30, 40, 24, 33, 12], [36, 17, 18, 21, 31, 43],
                               [42, 26, 26, 23, 33, 46], [56, 49, 40, 55, 54, 44], [54, 51, 62, 36, 44, 57]], k=4))
print(Solution().minCost(grid=[[3, 0, 0], [3, 1, 2], [4, 4, 3], [5, 4, 6], [8, 6, 4], [9, 8, 6], [11, 8, 8], [11, 7, 12], [12, 10, 9]],
                         k=6))
print(Solution().minCost(grid=[[21, 32, 6, 14, 26, 23], [14, 25, 44, 22, 47, 47]],
                         k=3))
