# https://leetcode.com/problems/finding-3-digit-even-numbers/description/?envType=daily-question&envId=2025-05-12

from typing import List
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def getValidPermutations(digits, i):
            if i >= len(digits):
                if digits[0] != 0 and digits[2] % 2 == 0:
                    return [digits[0] * 100 + digits[1] * 10 + digits[2]]
                else:
                    return []

            permutations = []

            for j in range(i, len(digits)):
                digits[i], digits[j] = digits[j], digits[i]
                permutations.extend(getValidPermutations(digits, i + 1))
                digits[j], digits[i] = digits[i], digits[j]

            return permutations

        done = set()
        evenNumbers = []
        for i in range(len(digits)):
            for j in range(i+1, len(digits)):
                for k in range(j+1, len(digits)):
                    if tuple(sorted((digits[i], digits[j], digits[k]))) not in done:
                        evenNumbers.extend(getValidPermutations(
                            [digits[i], digits[j], digits[k]], 0))

                        done.add(
                            tuple(sorted((digits[i], digits[j], digits[k]))))

        return sorted(set(evenNumbers))

    def findEvenNumbersV2(self, digits: List[int]) -> List[int]:
        digitsSet = Counter(digits)
        eventNumebrs = []
        for num in range(100, 1000, 2):
            isNumValid = True
            numFreq = Counter(str(num))
            keys = list(numFreq.keys())
            i = 0
            while i < len(keys) and isNumValid:
                if numFreq[keys[i]] > digitsSet[int(keys[i])]:
                    isNumValid = False
                i = i + 1

            if isNumValid:
                eventNumebrs.append(num)

        return eventNumebrs


print(Solution().findEvenNumbers(digits=[2, 2, 8, 8, 2]))
print(Solution().findEvenNumbersV2(digits=[2, 2, 8, 8, 2]))
