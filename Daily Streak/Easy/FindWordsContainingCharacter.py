# https://leetcode.com/problems/find-words-containing-character/description/?envType=daily-question&envId=2025-05-24

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i in range(len(words)) if x in words[i]]


print(Solution().findWordsContaining(words=["leet", "code"], x="e"))
print(Solution().findWordsContaining(
    words=["abc", "bcd", "aaaa", "cbc"], x="a"))
print(Solution().findWordsContaining(
    words=["abc", "bcd", "aaaa", "cbc"], x="z"))
