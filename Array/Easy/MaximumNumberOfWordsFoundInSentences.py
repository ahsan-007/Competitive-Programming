# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for senetnce in sentences:
            max_words = max(max_words, len(senetnce.split(' ')))
        return max_words

print(Solution().mostWordsFound(sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print(Solution().mostWordsFound(sentences = ["please wait", "continue to fight", "continue to win"]))
