# https://leetcode.com/problems/equal-sum-grid-partition-i/description/?envType=daily-question&envId=2026-03-25

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row_sum = [sum(row) for row in grid]
        total_sum = sum(row_sum)
        curr_sum = 0
        for i in range(len(row_sum)):
            curr_sum += row_sum[i]
            total_sum -= row_sum[i]

            if curr_sum == total_sum:
                return True

        col_sum = []
        if len(grid) > 0:
            total_sum = 0
            for j in range(len(grid[0])):
                curr_sum = 0
                for i in range(len(grid)):
                    curr_sum += grid[i][j]
                col_sum.append(curr_sum)
                total_sum += curr_sum

            curr_sum = 0
            for j in range(len(col_sum)):
                curr_sum += col_sum[j]
                total_sum -= col_sum[j]

                if curr_sum == total_sum:
                    return True
        return False


print(Solution().canPartitionGrid(grid=[[1, 4], [2, 3]]))
print(Solution().canPartitionGrid(grid=[[1, 3], [2, 4]]))
