# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1
        while lb <= ub:
            mid = lb + (ub - lb) // 2
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                if nums[mid] <= nums[ub] and target > nums[ub]:
                    ub = mid - 1
                else:
                    lb = mid + 1
            else:
                if nums[mid] >= nums[lb] and target < nums[lb]:
                    lb = mid + 1
                else:
                    ub = mid - 1
        return -1


print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=1))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=2))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=4))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=5))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=6))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=7))

print(Solution().search(nums=[1], target=0))

print(Solution().search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=8))

print(Solution().search(nums=[3, 1], target=1))
