# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3": "def", "4": "ghi",
                   "5": "jkl", "6": "mno", "7": "pqrs",
                   "8": "tuv", "9": "wxyz"}

        combinations = [letter for letter in mapping[digits[-1]]]
        for i in range(len(digits)-2, -1, -1):
            updated_combinatios = []
            for letter in mapping[digits[i]]:
                updated_combinatios.extend(
                    [letter + comb for comb in combinations])
            combinations = updated_combinatios
        return combinations


print(Solution().letterCombinations("2333"))
