# https://leetcode.com/problems/missing-number/description/?envType=daily-question&envId=2024-02-20

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return ((len(nums) * (len(nums) + 1)) // 2) - sum(nums)


print(Solution().missingNumber(nums=[3, 0, 1]))
print(Solution().missingNumber(nums=[0, 1]))
print(Solution().missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
