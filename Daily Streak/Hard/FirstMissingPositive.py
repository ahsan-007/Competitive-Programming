# https://leetcode.com/problems/first-missing-positive/description/?envType=daily-question&envId=2024-03-26

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if not (0 < nums[i] <= n):
                nums[i] = n + 1
        for i in range(n):
            x = abs(nums[i])
            if 0 < x <= n:
                nums[x - 1] = abs(nums[x - 1]) * -1
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


print(Solution().firstMissingPositive(nums=[1, 2, 0]))
print(Solution().firstMissingPositive(nums=[3, 4, -1, 1]))
print(Solution().firstMissingPositive(nums=[7, 8, 9, 11, 12]))
