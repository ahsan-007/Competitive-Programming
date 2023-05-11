# https://leetcode.com/problems/uncrossed-lines/

from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        return self.maxUncrossedLinesUtil(nums1, nums2, memo, 0, 0)

    def maxUncrossedLinesUtil(self, nums1: List[int], nums2: List[int], memo, ind1, ind2) -> int:
        if ind1 >= len(nums1) or ind2 >= len(nums2):
            return 0
        if ((ind1, ind2)) in memo:
            return memo[(ind1, ind2)]
        i = ind2
        while i < len(nums2) and nums2[i] != nums1[ind1]:
            i = i + 1

        res = self.maxUncrossedLinesUtil(nums1, nums2, memo, ind1+1, ind2)
        if i != len(nums2):
            res = max(res, self.maxUncrossedLinesUtil(
                nums1, nums2, memo, ind1+1, i+1) + 1)
        memo[(ind1, ind2)] = res
        return res


print(Solution().maxUncrossedLines(nums1=[1, 4, 2], nums2=[1, 2, 4]))
print(Solution().maxUncrossedLines(
    nums1=[2, 5, 1, 2, 5], nums2=[10, 5, 2, 1, 5, 2]))
print(Solution().maxUncrossedLines(
    nums1=[1, 3, 7, 1, 7, 5], nums2=[1, 9, 2, 5, 1]))
print(Solution().maxUncrossedLines(
    nums1=[1, 3, 7, 1, 7, 5]*70, nums2=[1, 9, 2, 5, 1]*71))
