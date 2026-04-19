# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/?envType=daily-question&envId=2026-04-19

from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def getFarthestGreaterOrEqual(nums, lb, ub, target):
            if lb > ub:
                return -1
            mid = lb + (ub - lb) // 2
            if target > nums[mid]:
                return getFarthestGreaterOrEqual(nums, lb, mid-1, target)
            return max(mid if target <= nums[mid] else -1, getFarthestGreaterOrEqual(nums, mid+1, ub, target))

        max_distance = 0
        i = 0
        while i < len(nums1) and i < len(nums2):
            max_distance = max(max_distance,
                               getFarthestGreaterOrEqual(nums2, i, len(nums2)-1, nums1[i]) - i)
            i = i + 1
        return max_distance


print(Solution().maxDistance(
    nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]))
print(Solution().maxDistance(nums1=[2, 2, 2], nums2=[10, 10, 1]))
print(Solution().maxDistance(
    nums1=[30, 29, 19, 5], nums2=[25, 25, 25, 25, 25]))
