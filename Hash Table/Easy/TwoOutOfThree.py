# https://leetcode.com/problems/two-out-of-three/

from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        elements = {num: [1, 0, 0] for num in nums1}
        for num in nums2:
            if num in elements:
                elements[num][1] = 1
            else:
                elements[num] = [0, 1, 0]
        for num in nums3:
            if num in elements:
                elements[num][2] = 1
            # no need to initialize with [0, 0, 1] in case not found
            # becauase element was not found in first 2 arrays so it is not going to be included in result set

        return [ele for ele in elements if sum(elements[ele]) > 1]


print(Solution().twoOutOfThree(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3]))
print(Solution().twoOutOfThree(nums1=[3, 1], nums2=[2, 3], nums3=[1, 2]))
print(Solution().twoOutOfThree(nums1=[1, 2, 2], nums2=[4, 3, 3], nums3=[5]))
