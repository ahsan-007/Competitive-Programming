# https://leetcode.com/problems/permutations/

from typing import List
from copy import deepcopy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permuteUtil(nums, permutations, [])
        return permutations

    def permuteUtil(self, nums, permutations, perm):
        if len(nums) == 0:
            permutations.append(deepcopy(perm))
        for i in range(len(nums)):
            perm.append(nums[i])
            num = nums.pop(i)
            self.permuteUtil(nums, permutations, perm)
            nums.insert(i, num)
            perm.pop()


print(Solution().permute([1, 2, 3]))
print(Solution().permute([1, 2, 3, 4, 5, 6]))
