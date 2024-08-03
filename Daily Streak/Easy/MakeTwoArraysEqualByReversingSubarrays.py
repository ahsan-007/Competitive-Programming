# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description /?envType=daily-question&envId=2024-08-03

from typing import List
from collections import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        targetFreq = Counter(target)
        arrFreq = Counter(arr)
        for ele in targetFreq:
            if targetFreq[ele] != arrFreq.get(ele, 0):
                return False
        return True

    def canBeEqualV2(self, target: List[int], arr: List[int]) -> bool:
        frequency = {}
        for ele in target:
            frequency[ele] = frequency.get(ele, 0) + 1

        for ele in arr:
            frequency[ele] = frequency.get(ele, 0) - 1
            if frequency[ele] == 0:
                del frequency[ele]

        return len(frequency) == 0

    def canBeEqualV3(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return target == arr


print(Solution().canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
print(Solution().canBeEqual(target=[7], arr=[7]))
print(Solution().canBeEqual(target=[3, 7, 9], arr=[3, 7, 11]))

print()

print(Solution().canBeEqualV2(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
print(Solution().canBeEqualV2(target=[7], arr=[7]))
print(Solution().canBeEqualV2(target=[3, 7, 9], arr=[3, 7, 11]))

print()

print(Solution().canBeEqualV3(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
print(Solution().canBeEqualV3(target=[7], arr=[7]))
print(Solution().canBeEqualV3(target=[3, 7, 9], arr=[3, 7, 11]))
