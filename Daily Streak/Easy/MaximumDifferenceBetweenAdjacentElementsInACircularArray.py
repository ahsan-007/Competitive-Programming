# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/?envType=daily-question&envId=2025-06-12

from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        i = 0
        diff = float("-inf")
        while i < len(nums):
            diff = max(diff, abs(nums[i] - nums[(i+1) % len(nums)]))
            i = i + 1
        return diff

    def maxAdjacentDistanceV2(self, nums: List[int]) -> int:
        i = 1
        diff = abs(nums[0] - nums[-1])
        while i < len(nums):
            diff = max(diff, abs(nums[i] - nums[i-1]))
            i = i + 1
        return diff


print(Solution().maxAdjacentDistance(nums=[1, 2, 4]))
print(Solution().maxAdjacentDistance(nums=[-5, -10, -5]))


print(Solution().maxAdjacentDistanceV2(nums=[1, 2, 4]))
print(Solution().maxAdjacentDistanceV2(nums=[-5, -10, -5]))
