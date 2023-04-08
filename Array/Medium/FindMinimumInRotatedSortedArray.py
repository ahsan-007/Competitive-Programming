# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lb = 0
        ub = len(nums) - 1
        minimum = nums[0]
        while lb <= ub:
            if nums[lb] <= nums[ub]:
                return min(minimum, nums[lb])
            mid = lb + (ub - lb) // 2
            minimum = min(minimum, nums[mid])
            if nums[mid] <= nums[ub]:
                ub = mid - 1
            else:
                lb = mid + 1


print(Solution().findMin(nums=[3, 4, 5, 1, 2]))
print(Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
print(Solution().findMin(nums=[11, 13, 15, 17]))
print(Solution().findMin(nums=[3, 1]))
print(Solution().findMin(nums=[3, 1, 2]))
