# https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=daily-question&envId=2024-03-10

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for num in nums1:
            if num in nums2 and num not in intersection:
                intersection.append(num)
        return intersection

    def intersectionV2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


print(Solution().intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(Solution().intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))

print(Solution().intersectionV2(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(Solution().intersectionV2(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
