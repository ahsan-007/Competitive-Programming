# https://leetcode.com/problems/minimum-common-value/?envType=daily-question&envId=2024-03-09

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]

            if nums1[i] < nums2[j]:
                i = i + 1
            else:
                j = j + 1

        return -1


print(Solution().getCommon(nums1=[1, 2, 3], nums2=[2, 4]))
print(Solution().getCommon(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]))
