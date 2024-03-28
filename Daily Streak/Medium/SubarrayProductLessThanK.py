# https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=daily-question&envId=2024-03-27

from typing import List
import math


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        i = j = 0
        prod = None

        while j < len(nums):
            prod = (prod * nums[j]) if prod else nums[j]

            while i < j and prod >= k:
                prod = prod // nums[i]
                i = i + 1
            if prod < k:
                count = count + (j - i + 1)

            j = j + 1

        return count


print(Solution().numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
print(Solution().numSubarrayProductLessThanK(nums=[2, 3, 4, 5, 6, 7], k=120))
print(Solution().numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
