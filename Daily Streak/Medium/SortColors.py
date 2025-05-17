# https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2025-05-17

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                i = i + 1
                left = left + 1

            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right = right - 1
            else:
                i = i + 1


nums = [2, 0, 2, 1, 1, 0]
print(nums)
Solution().sortColors(nums)
print(nums)

nums = [2, 0, 1]
print(nums)
Solution().sortColors(nums)
print(nums)
