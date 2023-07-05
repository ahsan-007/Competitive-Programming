# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left_ones = right_ones = 0
        zero_found = False
        maximum_length = 0
        for num in nums:
            if num == 0:
                if zero_found:
                    maximum_length = max(
                        maximum_length, left_ones + right_ones)
                    left_ones = right_ones
                    right_ones = 0
                else:
                    zero_found = True
            else:
                if zero_found:
                    right_ones = right_ones + 1
                else:
                    left_ones = left_ones + 1
        return max(maximum_length, left_ones + right_ones) - (1 if not zero_found else 0)


print(Solution().longestSubarray(nums=[1, 1, 0, 1]))
print(Solution().longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(Solution().longestSubarray(nums=[1, 1, 1]))
