# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/?envType=daily-question&envId=2025-04-08

from typing import List
import math


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        i = len(nums) - 1
        while i < len(nums):
            if nums[i] in seen:
                return i//3 + 1
            seen.add(nums[i])
            i = i - 1
        return 0


print(Solution().minimumOperations(nums=[1, 2, 3, 4, 2, 3, 3, 5, 7]))
print(Solution().minimumOperations(nums=[4, 5, 6, 4, 4]))
print(Solution().minimumOperations(nums=[6, 7, 8, 9]))
print(Solution().minimumOperations(nums=[6, 6, 13, 2, 6, 13]))
print(Solution().minimumOperations(nums=[5, 7, 11, 12, 12]))
