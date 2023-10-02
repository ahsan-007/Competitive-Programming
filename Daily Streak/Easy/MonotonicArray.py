# https://leetcode.com/problems/monotonic-array/description/?envType=daily-question&envId=2023-09-29

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = None
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                if increasing is None:
                    increasing = nums[i] < nums[i+1]
                else:
                    if (nums[i] > nums[i+1] and increasing) or (nums[i] < nums[i+1] and not increasing):
                        return False
            i = i + 1
        return True


print(Solution().isMonotonic(nums=[1, 2, 2, 3]))
print(Solution().isMonotonic(nums=[6, 5, 4, 4]))
print(Solution().isMonotonic(nums=[1, 3, 2]))
