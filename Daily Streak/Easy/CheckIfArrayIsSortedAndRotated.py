# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2026-05-23

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        out_of_place_count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                out_of_place_count += 1

        if nums[0] < nums[-1]:
            out_of_place_count += 1
        return out_of_place_count <= 1


print(Solution().check(nums=[3, 4, 5, 1, 2]))
print(Solution().check(nums=[2, 1, 3, 4]))
print(Solution().check(nums=[1, 2, 3]))
