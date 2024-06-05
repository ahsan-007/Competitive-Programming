# https://leetcode.com/problems/find-common-characters/description /?envType=daily-question&envId=2024-06-05

from typing import List
from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commanCharacters = []
        words = [Counter(word) for word in words]

        for ch in words[0]:
            minCount = words[0][ch]
            i = 0
            while i < len(words) and minCount != 0:
                minCount = min(minCount, words[i].get(ch, 0))
                i = i + 1

            if minCount != 0:
                commanCharacters.extend([ch] * minCount)

        return commanCharacters


print(Solution().commonChars(words=["bella", "label", "roller"]))
print(Solution().commonChars(words=["cool", "lock", "cook"]))
