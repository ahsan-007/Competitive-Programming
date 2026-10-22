# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/editorial/?envType=daily-question&envId=2026-10-22

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        is_increasing = True
        is_decreasing = True

        start_ind = nums.index(0)

        i = 1
        while i < n and (is_increasing or is_decreasing):
            num = nums[(start_ind + i) % n]

            if num != i:
                is_increasing = False

            if num != n - i:
                is_decreasing = False

            i = i + 1

        if not is_increasing and not is_decreasing:
            return - 1

        if is_increasing:
            return min(start_ind, n - start_ind + 2)

        return min(n - start_ind, start_ind + 2)


print(Solution().minOperations(nums=[0, 2, 1]))
print(Solution().minOperations(nums=[1, 0, 2]))
print(Solution().minOperations(nums=[2, 0, 1, 3]))
