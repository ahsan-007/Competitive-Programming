# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/?envType=daily-question&envId=2026-08-11

from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        j = 1
        while j < len(nums) and nums[j] == nums[j-1] + 1
            prefix_sum += nums[j]
            j = j + 1

        while prefix_sum in nums:
            prefix_sum += 1
        return prefix_sum


print(Solution().missingInteger(nums=[1, 2, 3, 2, 5]))
print(Solution().missingInteger(nums=[3, 4, 5, 1, 12, 14, 13]))
