# https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11

from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        frequency = Counter(s)
        sortedStr = ""

        for ch in order:
            if frequency.get(ch, 0) > 0:
                sortedStr += ch * frequency[ch]
                frequency[ch] = 0

        for ch in frequency:
            if frequency.get(ch, 0) > 0:
                sortedStr += ch * frequency[ch]

        return sortedStr


print(Solution().customSortString(order="cba", s="abcd"))
print(Solution().customSortString(order="bcafg", s="abcd"))
