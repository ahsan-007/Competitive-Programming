# https://leetcode.com/problems/create-target-array-in-the-given-order/

from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for num, ind in zip(nums, index):
            target.insert(ind, num)
        return target


print(Solution().createTargetArray(
    nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
print(Solution().createTargetArray(
    nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]))
print(Solution().createTargetArray(nums=[1], index=[0]))
