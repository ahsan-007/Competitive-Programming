# https://leetcode.com/problems/smallest-missing-multiple-of-k/description/?envType=daily-question&envId=2026-08-25

from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        multiple = k
        while multiple in nums:
            multiple += k
        return multiple


print(Solution().missingMultiple(nums=[8, 2, 3, 4, 6], k=2))
print(Solution().missingMultiple(nums=[1, 4, 7, 10, 15], k=5))
