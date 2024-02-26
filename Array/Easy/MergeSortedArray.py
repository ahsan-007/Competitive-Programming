# https://leetcode.com/problems/merge-sorted-array/description/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        if m > 0:
            offset = len(nums1) - m
            i = m - 1
            while i >= 0:
                nums1[i + offset] = nums1[i]
                i = i - 1

        i = len(nums1) - m
        j = 0
        k = 0
        while k < len(nums1):
            if i > 0 and i < len(nums1) and (j == len(nums2) or nums1[i] <= nums2[j]):
                nums1[k] = nums1[i]
                i = i + 1
            else:
                nums1[k] = nums2[j]
                j = j + 1

            k = k + 1

    def mergeV2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = len(nums1) - 1
        while k >= 0:
            if i >= 0 and (j < 0 or nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i = i - 1
            else:
                nums1[k] = nums2[j]
                j = j - 1
            k = k - 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
Solution().merge(nums1, 3, nums2, 3)
print(nums1)

nums1 = [1, 2, 5, 0, 0, 0]
nums2 = [1, 2, 3]
Solution().merge(nums1, 3, nums2, 3)
print(nums1)

nums1 = [0]
nums2 = [1]
Solution().merge(nums1, 0, nums2, 1)
print(nums1)

nums1 = [1]
nums2 = []
Solution().merge(nums1, 1, nums2, 0)
print(nums1)

print('-' * 100)

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
Solution().mergeV2(nums1, 3, nums2, 3)
print(nums1)

nums1 = [1, 2, 5, 0, 0, 0]
nums2 = [1, 2, 3]
Solution().mergeV2(nums1, 3, nums2, 3)
print(nums1)

nums1 = [0]
nums2 = [1]
Solution().mergeV2(nums1, 0, nums2, 1)
print(nums1)

nums1 = [1]
nums2 = []
Solution().mergeV2(nums1, 1, nums2, 0)
print(nums1)
