# https://leetcode.com/problems/last-day-where-you-can-still-cross/description/?envType=daily-question&envId=2025-12-31

from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def isCrossedUtil(i, j, floodedCells, visited):
            if (i, j) in floodedCells or (i, j) in visited or i < 1 or j < 1 or j > col:
                return False

            if i == row:
                return True

            visited.add((i, j))
            return isCrossedUtil(i + 1, j, floodedCells, visited) or isCrossedUtil(i - 1, j, floodedCells, visited) or isCrossedUtil(i, j + 1, floodedCells, visited) or isCrossedUtil(i, j - 1, floodedCells, visited)

        def isCrossed(day):
            floodedCells = set(tuple(cell) for cell in cells[:day])
            visited = set()
            for j in range(1, col + 1):
                if isCrossedUtil(1, j, floodedCells, visited):
                    return True
            return False

        lb = 1
        ub = len(cells)
        lastDayToCross = 0
        while lb <= ub and lastDayToCross < ub:
            mid = lb + (ub - lb) // 2
            if isCrossed(mid):
                lastDayToCross = max(lastDayToCross, mid)
                lb = mid + 1
            else:
                ub = mid - 1
        return lastDayToCross


print(Solution().latestDayToCross(row=2, col=2,
      cells=[[1, 1], [2, 1], [1, 2], [2, 2]]))

print(Solution().latestDayToCross(row=2, col=2,
      cells=[[1, 1], [1, 2], [2, 1], [2, 2]]))

print(Solution().latestDayToCross(row=3, col=3, cells=[
      [1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]))
