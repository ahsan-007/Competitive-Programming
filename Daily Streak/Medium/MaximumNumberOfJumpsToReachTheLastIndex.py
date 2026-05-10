# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/?envType=daily-question&envId=2026-05-10

from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        def maximumJumpsUtil(nums, target, i, memo):
            if i == len(nums) - 1:
                return 0

            if i >= len(nums):
                return float("-inf")

            if i not in memo:
                max_jumps = float("-inf")
                for j in range(i+1, len(nums)):
                    if -target <= nums[j] - nums[i] <= target:
                        max_jumps = max(
                            max_jumps, maximumJumpsUtil(nums, target, j, memo) + 1)
                memo[i] = max_jumps
            return memo[i]

        return max(-1, maximumJumpsUtil(nums, target, 0, {}))


print(Solution().maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=2))
print(Solution().maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=3))
print(Solution().maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=0))
