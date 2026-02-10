# https://leetcode.com/problems/longest-balanced-subarray-i/description/?envType=daily-question&envId=2026-02-10

from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        maxLength = 0
        for i in range(len(nums)):
            even = set()
            odd = set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                if len(odd) == len(even):
                    maxLength = max(maxLength, j-i+1)
        return maxLength


print(Solution().longestBalanced(nums=[2, 5, 4, 3]))
print(Solution().longestBalanced(nums=[3, 2, 2, 5, 4]))
print(Solution().longestBalanced(nums=[1, 2, 3, 2]))
print(Solution().longestBalanced(nums=[37, 37, 4, 21, 11, 23, 24]))
