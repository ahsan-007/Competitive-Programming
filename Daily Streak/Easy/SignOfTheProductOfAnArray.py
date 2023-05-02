# https://leetcode.com/problems/sign-of-the-product-of-an-array/

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative_numbers = 0
        for num in nums:
            if num < 0:
                negative_numbers = negative_numbers + 1
            elif num == 0:
                return 0
        return 1 if negative_numbers % 2 == 0 else -1


print(Solution().arraySign(nums=[-1, -2, -3, -4, 3, 2, 1]))
print(Solution().arraySign(nums=[1, 5, 0, 2, -3]))
print(Solution().arraySign(nums=[-1, 1, -1, 1, -1]))
