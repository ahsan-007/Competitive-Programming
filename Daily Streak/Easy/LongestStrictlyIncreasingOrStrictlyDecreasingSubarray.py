# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2026-11-12

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest_increasing = longest_decreasing = increasing = decreasing = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] == nums[i - 1]:
                longest_increasing = max(longest_increasing, increasing)
                longest_decreasing = max(longest_decreasing, decreasing)
                increasing = decreasing = 1

            elif nums[i] > nums[i - 1]:
                increasing += 1

                longest_decreasing = max(longest_decreasing, decreasing)
                decreasing = 1
            else:
                decreasing += 1

                longest_increasing = max(longest_increasing, increasing)
                increasing = 1

        longest_increasing = max(longest_increasing, increasing)
        longest_decreasing = max(longest_decreasing, decreasing)

        return max(longest_increasing, longest_decreasing)



print(Solution().longestMonotonicSubarray(nums = [1,4,3,3,2]))
print(Solution().longestMonotonicSubarray(nums = [3,3,3,3]))
print(Solution().longestMonotonicSubarray(nums = [3,2,1]))
print(Solution().longestMonotonicSubarray(nums = [1,10,10]))