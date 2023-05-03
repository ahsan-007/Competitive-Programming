# https://leetcode.com/problems/find-the-difference-of-two-arrays/

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_elements = set(nums1)
        answer = [set(), set()]
        nums2_elements = set()

        for num in nums2:
            if num not in nums1_elements:
                answer[1].add(num)
            nums2_elements.add(num)

        for num in nums1:
            if num not in nums2_elements:
                answer[0].add(num)

        return [list(answer[0]), list(answer[1])]


print(Solution().findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
print(Solution().findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))
