# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/?envType=daily-question&envId=2024-02-14

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        rearranged = [0] * len(nums)
        p = 0
        n = 1
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                rearranged[p] = nums[i]
                p = p + 2
            else:
                rearranged[n] = nums[i]
                n = n + 2
            i = i + 1
        return nums


print(Solution().rearrangeArray(nums=[3, 1, -2, -5, 2, -4]))
print(Solution().rearrangeArray(nums=[3, -1, -2, -5, 2, -4, 7, 8]))
print(Solution().rearrangeArray(nums=[-1, 1]))
print(Solution().rearrangeArray(
    [28, -41, 22, -8, -37, 46, 35, -9, 18, -6, 19, -26, -37, -10, -9, 15, 14, 31]))
