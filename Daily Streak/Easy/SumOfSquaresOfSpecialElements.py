# https://leetcode.com/problems/sum-of-squares-of-special-elements/description/?envType=daily-question&envId=2026-10-11

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(nums[i - 1] ** 2 for i in range(1, len(nums) + 1) if len(nums) % i == 0)


print(Solution().sumOfSquares(nums=[1, 2, 3, 4]))
print(Solution().sumOfSquares(nums=[2, 7, 1, 19, 18, 3]))
