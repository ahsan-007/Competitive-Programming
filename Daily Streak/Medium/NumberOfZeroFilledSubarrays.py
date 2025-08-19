# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/?envType=daily-question&envId=2025-08-19

from typing import List
import math


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
                total += zeroes
            else:
                zeroes = 0
        return total

    def zeroFilledSubarrayV2(self, nums: List[int]) -> int:
        count = 0
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
            elif zeroes > 0:
                count = count + (zeroes * (zeroes + 1)) // 2
                zeroes = 0

        if zeroes > 0:
            count = count + (zeroes * (zeroes + 1)) // 2

        return count


print(Solution().zeroFilledSubarray(nums=[1, 3, 0, 0, 2, 0, 0, 4]))
print(Solution().zeroFilledSubarray(nums=[0, 0, 0, 2, 0, 0]))
print(Solution().zeroFilledSubarray(nums=[2, 10, 2019]))
