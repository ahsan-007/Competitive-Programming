# https://leetcode.com/problems/number-of-good-pairs/description/?envType=daily-question&envId=2023-10-03

from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        goodPairs = 0
        for count in frequency.values():
            goodPairs = goodPairs + (count * (count - 1) // 2)
        return goodPairs


print(Solution().numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
print(Solution().numIdenticalPairs(nums=[1, 1, 1, 1]))
print(Solution().numIdenticalPairs(nums=[1, 2, 3]))
