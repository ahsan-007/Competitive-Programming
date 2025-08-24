# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=daily-question&envId=2025-08-24

from typing import List


class Solution:
    # Time: O(N), Space: O(1)
    def longestSubarray(self, nums: List[int]) -> int:
        rightCount = 0
        leftCount = 0
        totalCount = 0
        for i, num in enumerate(nums):
            if num == 0:
                totalCount = max(totalCount, leftCount + rightCount)
                leftCount, rightCount = rightCount, 0
            else:
                rightCount += 1

        totalCount = max(totalCount, leftCount + rightCount)

        return totalCount if totalCount != len(nums) else totalCount - 1


print(Solution().longestSubarray(nums=[1, 1, 0, 1]))
print(Solution().longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(Solution().longestSubarray(nums=[1, 1, 1]))
