# https://leetcode.com/problems/sequential-digits/description/?envType=daily-question&envId=2024-02-02

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        sequentialDigitNumbers = []

        low_copy = low
        length = 0
        while low_copy:
            low_copy = low_copy // 10
            length = length + 1

        while length <= len(digits):
            i = 0
            while i <= (len(digits) - length):
                num = int(digits[i:i+length])
                if num >= low:
                    if num <= high:
                        sequentialDigitNumbers.append(num)
                    else:
                        return sequentialDigitNumbers
                i = i + 1
            length = length + 1

        return sequentialDigitNumbers


print(Solution().sequentialDigits(low=10, high=1000000000))
print(Solution().sequentialDigits(low=58, high=155))
