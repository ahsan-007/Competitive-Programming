# https://leetcode.com/problems/intersection-of-two-arrays-ii/description /?envType=daily-question&envId=2024-07-02

from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Freq = Counter(nums1)
        nums2Freq = Counter(nums2)
        intersection = []
        for ele in nums1Freq:
            if ele in nums2Freq:
                intersection.extend(
                    [ele] * min(nums1Freq[ele], nums2Freq[ele]))
        return intersection


print(Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
