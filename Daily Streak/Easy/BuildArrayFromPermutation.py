# https://leetcode.com/problems/build-array-from-permutation/description/?envType=daily-question&envId=2025-05-06

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


print(Solution().buildArray(nums=[0, 2, 1, 5, 3, 4]))
print(Solution().buildArray(nums=[5, 0, 1, 2, 3, 4]))
