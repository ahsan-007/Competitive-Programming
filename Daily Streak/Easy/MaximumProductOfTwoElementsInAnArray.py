# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/?envType=daily-question&envId=2023-12-12

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max, second_max = nums[0], nums[1]
        if first_max < second_max:
            first_max, second_max = second_max, first_max

        for i in range(2, len(nums)):
            if nums[i] > first_max:
                second_max, first_max = first_max, nums[i]
            elif nums[i] > second_max:
                second_max = nums[i]

        return (first_max - 1) * (second_max - 1)


print(Solution().maxProduct(nums=[3, 4, 5, 2]))
print(Solution().maxProduct(nums=[1, 5, 4, 5]))
print(Solution().maxProduct(nums=[3, 7]))
