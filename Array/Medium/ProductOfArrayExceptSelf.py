# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    # Without using division operator
    # Time: O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]
        multiple = nums[0]
        for i in range(1, len(nums)):
            product.append(multiple)
            multiple = multiple * nums[i]

        multiple = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            product[i] = product[i] * multiple
            multiple = multiple * nums[i]

        return product


print(Solution().productExceptSelf(nums=[1, 2, 3, 4]))
print(Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]))
