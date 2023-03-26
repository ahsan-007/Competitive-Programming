# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i1 = j1 = i2 = j2 = 0

        while i1 < len(word1) and i2 < len(word2):
            if word1[i1][j1] != word2[i2][j2]:
                return False
            j1 = j1 + 1
            j2 = j2 + 1
            if j1 >= len(word1[i1]):
                i1 = i1 + 1
                j1 = 0
            if j2 == len(word2[i2]):
                i2 = i2 + 1
                j2 = 0

        return True if i1 == len(word1) and i2 == len(word2) else False


print(Solution().arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
print(Solution().arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))
print(Solution().arrayStringsAreEqual(
    word1=["abc", "d", "defg"], word2=["abcddefg"]))
