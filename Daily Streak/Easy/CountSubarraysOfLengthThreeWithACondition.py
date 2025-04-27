# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/?envType=daily-question&envId=2025-04-27

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        i = 2
        count = 0
        while i < len(nums):
            if nums[i-2] + nums[i] == nums[i - 1] / 2:
                count = count + 1
            i = i + 1
        return count


print(Solution().countSubarrays(nums=[1, 2, 1, 4, 1]))
print(Solution().countSubarrays(nums=[1, 1, 1]))
