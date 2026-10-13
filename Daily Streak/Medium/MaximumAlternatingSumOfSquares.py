# https://leetcode.com/problems/maximum-alternating-sum-of-squares/description/?envType=daily-question&envId=2026-10-13

from typing import List
import math


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted([num ** 2 for num in nums], reverse=True)
        k = math.ceil(len(nums) / 2)
        return sum(nums[:k]) - sum(nums[k:])


print(Solution().maxAlternatingSum(nums=[1, 2, 3]))
print(Solution().maxAlternatingSum(nums=[1, -1, 2, -2, 3, -3]))
