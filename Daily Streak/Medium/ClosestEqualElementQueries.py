# https://leetcode.com/problems/closest-equal-element-queries/description/?envType=daily-question&envId=2026-04-16

from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        pos = {}

        for i in range(-n, n):
            if i >= 0:
                left[i] = pos.get(nums[i], -n)
            pos[nums[(i + n) % n]] = i

        pos.clear()
        for i in range(2 * n - 1, -1, -1):
            if i < n:
                right[i] = pos.get(nums[i], 2 * n)
            pos[nums[i % n]] = i

        for i in range(len(queries)):
            x = queries[i]
            if x - left[x] == n:
                queries[i] = -1
            else:
                queries[i] = min(x - left[x], right[x] - x)

        return queries


print(Solution().solveQueries(nums=[1, 3, 1, 4, 1, 3, 2], queries=[0, 3, 5]))
print(Solution().solveQueries(nums=[1, 2, 3, 4], queries=[0, 1, 2, 3]))
