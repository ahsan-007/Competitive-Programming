# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2026-01-24

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        maxPairSum = float("-inf")
        while i < len(nums) // 2:
            maxPairSum = max(maxPairSum, nums[i] + nums[len(nums) - i - 1])
            i = i + 1
        return maxPairSum


print(Solution().minPairSum(nums=[3, 5, 2, 3]))
print(Solution().minPairSum(nums=[3, 5, 4, 2, 4, 6]))
