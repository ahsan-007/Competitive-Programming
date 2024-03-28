# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/?envType=daily-question&envId=2024-03-28

from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        i = 0
        j = 0
        maxLength = 0
        while j < len(nums):
            freq[nums[j]] = freq.get(nums[j], 0) + 1

            while freq[nums[j]] > k:
                freq[nums[i]] = freq[nums[i]] - 1
                i = i + 1

            maxLength = max(maxLength, j - i + 1)
            j = j + 1
        return maxLength


print(Solution().maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
print(Solution().maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1))
print(Solution().maxSubarrayLength(nums=[5, 5, 5, 5, 5, 5, 5], k=4))
