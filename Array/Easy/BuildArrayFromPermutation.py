# https://leetcode.com/problems/build-array-from-permutation/

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]


print(Solution().buildArray(nums=[0, 2, 1, 5, 3, 4]))
print(Solution().buildArray(nums=[5, 0, 1, 2, 3, 4]))
