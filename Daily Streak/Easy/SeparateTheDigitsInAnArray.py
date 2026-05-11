# https://leetcode.com/problems/separate-the-digits-in-an-array/description/?envType=daily-question&envId=2026-05-11

from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def getDigits(num):
            digits = []
            while num:
                digits.insert(0, num % 10)
                num = num // 10
            return digits

        digits = []
        for num in nums:
            digits.extend(getDigits(num))
        return digits


print(Solution().separateDigits(nums=[13, 25, 83, 77]))
print(Solution().separateDigits(nums=[7, 1, 3, 9]))
