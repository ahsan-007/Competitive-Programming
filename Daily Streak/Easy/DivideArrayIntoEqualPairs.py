# https://leetcode.com/problems/divide-array-into-equal-pairs/description/?envType=daily-question&envId=2025-03-17

from typing import List
from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(frequency % 2 == 0 for frequency in Counter(nums).values())


print(Solution().divideArray(nums=[3, 2, 3, 2, 2, 2]))
print(Solution().divideArray(nums=[1, 2, 3, 4]))
