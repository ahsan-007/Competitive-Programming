# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=daily-question&envId=2026-05-15

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findMinUtil(lb, ub):
            if lb > ub:
                return float("+inf")

            mid = lb + (ub - lb) // 2

            if nums[lb] <= nums[mid]:
                return min(nums[lb], findMinUtil(mid + 1, ub))
            else:
                return min(nums[mid], findMinUtil(lb, mid - 1))

        return findMinUtil(0, len(nums)-1)


print(Solution().findMin(nums=[3, 4, 5, 1, 2]))
print(Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
print(Solution().findMin(nums=[11, 13, 15, 17]))
