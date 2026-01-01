# https://leetcode.com/problems/plus-one/description/?envType=daily-question&envId=2026-01-01

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while i >= 0 and carry > 0:
            digSum = digits[i] + carry
            digits[i] = digSum % 10
            carry = digSum // 10
            i = i - 1

        return [carry, *digits] if carry else digits


print(Solution().plusOne(digits=[1, 2, 3]))
print(Solution().plusOne(digits=[4, 3, 2, 1]))
print(Solution().plusOne(digits=[9]))
