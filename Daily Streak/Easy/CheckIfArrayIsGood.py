# https://leetcode.com/problems/check-if-array-is-good/description/?envType=daily-question&envId=2026-05-14

from typing import List
from collections import defaultdict


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        base = {}
        for num in nums:
            base[num] = base.get(num, 0) + 1

        n = len(nums) - 1
        for i in range(1, n):
            if base.get(i, 0) != 1:
                return False
        return base.get(n, 0) == 2


print(Solution().isGood(nums=[2, 1, 3]))
print(Solution().isGood(nums=[1, 3, 3, 2]))
print(Solution().isGood(nums=[1, 1]))
print(Solution().isGood(nums=[3, 4, 4, 1, 2, 1]))
