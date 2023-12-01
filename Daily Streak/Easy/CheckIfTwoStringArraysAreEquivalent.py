# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/?envType=daily-question&envId=2023-12-01

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        r1 = c1 = r2 = c2 = 0
        while r1 < len(word1) and r2 < len(word2):
            if word1[r1][c1] != word2[r2][c2]:
                return False

            c1 = c1 + 1
            c2 = c2 + 1

            if c1 == len(word1[r1]):
                r1 = r1 + 1
                c1 = 0

            if c2 == len(word2[r2]):
                r2 = r2 + 1
                c2 = 0

        return r1 == len(word1) and r2 == len(word2)


print(Solution().arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
print(Solution().arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))
print(Solution().arrayStringsAreEqual(
    word1=["abc", "d", "defg"], word2=["abcddefg"]))
