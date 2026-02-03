# https://leetcode.com/problems/trionic-array-i/description/?envType=daily-question&envId=2026-02-03

from typing import List
from enum import Enum


class Solution:
    # Time: O(N), Space: O(1)
    def isTrionic(self, nums: List[int]) -> bool:
        # 0...p (increasing)
        i = 1
        while i < len(nums) and nums[i] > nums[i - 1]:
            i = i + 1
        if i == 1 or i == len(nums):
            return False

        # p...q (decreasing)
        j = i
        while j < len(nums) and nums[j] < nums[j - 1]:
            j = j + 1
        if j == len(nums):
            return False

        # q...n (increasing)
        k = j
        while k < len(nums) and nums[k] > nums[k - 1]:
            k = k + 1
        return True if k == len(nums) else False

    # Time: O(N), Space: O(1)
    def isTrionicV2(self, nums: List[int]) -> bool:
        state = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return False

            if state == 0:
                if nums[i] < nums[i-1]:
                    if i == 1:
                        return False
                    state = 1

            elif state == 1:
                if nums[i] > nums[i - 1]:
                    state = 2

            elif state == 2:
                if nums[i] < nums[i - 1]:
                    return False

        return state == 2


print(Solution().isTrionic(nums=[1, 3, 5, 4, 2, 6]))
print(Solution().isTrionic(nums=[2, 1, 3]))
print(Solution().isTrionic(nums=[5, 9, 1, 7]))
print(Solution().isTrionic(nums=[1, 2, 3]))

print('-' * 100)

print(Solution().isTrionicV2(nums=[1, 3, 5, 4, 2, 6]))
print(Solution().isTrionicV2(nums=[2, 1, 3]))
print(Solution().isTrionicV2(nums=[5, 9, 1, 7]))
print(Solution().isTrionicV2(nums=[1, 2, 3]))
