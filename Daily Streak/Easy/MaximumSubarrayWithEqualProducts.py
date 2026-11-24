# https://leetcode.com/problems/maximum-subarray-with-equal-products/description/?envType=daily-question&envId=2026-11-24

from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def getGCD(a, b):
            if a > b:
                return getGCD(b, a)

            mod = b % a
            if mod == 0:
                return a

            return getGCD(mod, a)

        def getLCM(a, b):
            return a * b // getGCD(a, b)

        def getGCDOfList(nums, i, j):
            gcd = nums[i]
            i = i + 1
            while i <= j:
                gcd = getGCD(gcd, nums[i])
                i = i + 1
            return gcd

        def getLCMOfList(nums, i, j):
            lcm = nums[i]
            i = i + 1
            while i <= j:
                lcm = getLCM(lcm, nums[i])
                i = i + 1
            return lcm

        def getProduct(nums, i, j):
            prod = 1
            while i <= j:
                prod = prod * nums[i]
                i = i + 1
            return prod

        length = 0
        for i in range(len(nums)):
            j = len(nums) - 1
            while j - i + 1 > length and i < j:
                lcm = getLCMOfList(nums, i, j)
                gcd = getGCDOfList(nums, i, j)
                product = getProduct(nums, i, j)

                if product == lcm * gcd:
                    length = j - i + 1
                j = j - 1
        return length


print(Solution().maxLength(nums=[1, 2, 1, 2, 1, 1, 1]))
print(Solution().maxLength(nums=[2, 3, 4, 5, 6]))
print(Solution().maxLength(nums=[1, 2, 3, 1, 4, 5, 1]))
