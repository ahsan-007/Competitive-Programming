# https://leetcode.com/problems/words-within-two-edits-of-dictionary/description /?envType=daily-question&envId=2026-04-22

from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for i in range(len(queries)):
            j = 0
            is_appeneded = False
            while j < len(dictionary) and not is_appeneded:
                diff = 0
                k = 0
                while k < len(dictionary[j]) and diff < 3:
                    if queries[i][k] != dictionary[j][k]:
                        diff += 1
                    k = k + 1

                if diff < 3:
                    ans.append(queries[i])
                    is_appeneded = True
                j = j + 1
        return ans


print(Solution().twoEditWords(
    queries=["word", "note", "ants", "wood"], dictionary=["wood", "joke", "moat"]))
print(Solution().twoEditWords(queries=["yes"], dictionary=["not"]))
