# https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=daily-question&envId=2024-03-14

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        arrays = 0
        curr_sum = 0
        freq = {}
        for num in nums:
            curr_sum = curr_sum + num
            if curr_sum == goal:
                arrays = arrays + 1
            if curr_sum - goal in freq:
                arrays = arrays + freq[curr_sum - goal]
            freq[curr_sum] = freq.get(curr_sum, 0) + 1
        return arrays


print(Solution().numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
print(Solution().numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))
print(Solution().numSubarraysWithSum(nums=[0, 0, 0]*1000, goal=0))
print(Solution().numSubarraysWithSum(nums=[1, 0]*1000, goal=5))
