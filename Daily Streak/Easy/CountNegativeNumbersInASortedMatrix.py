# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        r = len(grid) - 1
        while r >= 0 and grid[r][-1] < 0:
            non_negative_found = False
            c = len(grid[r]) - 1
            while c >= 0 and not non_negative_found:
                if grid[r][c] < 0:
                    count = count + 1
                else:
                    non_negative_found = True
                c = c - 1
            r = r - 1
        return count

    def countNegativesV2(self, grid: List[List[int]]) -> int:
        # find index of first negative element using binary search
        def findFirstNegativeEleInd(nums, lb, ub):
            if lb > ub:
                return float("+inf")

            mid = lb + (ub - lb) // 2
            if nums[mid] >= 0:
                return findFirstNegativeEleInd(nums, mid + 1, ub)
            else:
                return min(mid, findFirstNegativeEleInd(nums, lb, mid - 1))

        count = 0
        i = 0
        while i < len(grid):
            firstNegativeEleInd = findFirstNegativeEleInd(
                grid[i], 0, len(grid[i]) - 1)
            if firstNegativeEleInd != float("+inf"):
                count += len(grid[i]) - firstNegativeEleInd
            i = i + 1
        return count


print(Solution().countNegatives(
    grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(Solution().countNegatives(grid=[[3, 2], [1, 0]]))

print('-' * 100)

print(Solution().countNegativesV2(
    grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(Solution().countNegativesV2(grid=[[3, 2], [1, 0]]))
