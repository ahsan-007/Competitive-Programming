# https://leetcode.com/problems/unique-3-digit-even-numbers/description/?envType=daily-question&envId=2026-09-11

from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()
        for i in range(len(digits)):
            if digits[i] % 2 == 0:
                for j in range(len(digits)):
                    if j != i:
                        for k in range(len(digits)):
                            if digits[k] != 0 and k != i and k != j:
                                numbers.add(digits[k]*100 +
                                            digits[j]*10+digits[i])
        return len(numbers)


print(Solution().totalNumbers(digits=[1, 2, 3, 4]))
print(Solution().totalNumbers([0, 2, 2]))
print(Solution().totalNumbers([6, 6, 6]))
print(Solution().totalNumbers([1, 3, 5]))
