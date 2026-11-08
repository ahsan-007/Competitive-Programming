# https://leetcode.com/problems/count-servers-that-communicate/description/?envType=daily-question&envId=2026-11-08

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        def isAnyServerInColumn(grid, i, j, ti):
            if i >= len(grid) or j >= len(grid[i]):
                return False

            if i != ti and grid[i][j] == 1:
                return True

            return isAnyServerInColumn(grid, i + 1, j, ti)

        def isAnyServerInRow(grid, i, j, tj):
            if i >= len(grid) or j >= len(grid[i]):
                return False

            if j != tj and grid[i][j] == 1:
                return True

            return isAnyServerInRow(grid, i, j + 1, tj)

        rowMemo = {}
        columnMemo = {}
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i not in rowMemo:
                        rowMemo[i] = isAnyServerInRow(grid, i, 0, j)

                    if not rowMemo[i] and j not in columnMemo:
                        columnMemo[j] = isAnyServerInColumn(grid, 0, j, i)

                    if rowMemo[i] == 1 or columnMemo[j] == 1:
                        count += 1
        return count


print(Solution().countServers(grid=[[1, 0], [0, 1]]))
print(Solution().countServers(grid=[[1, 0], [1, 1]]))
print(Solution().countServers(
    grid=[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
