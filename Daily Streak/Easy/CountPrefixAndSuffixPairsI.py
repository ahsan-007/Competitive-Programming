# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description /?envType=daily-question&envId=2025-01-08

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixSuffix(source, target):
            if len(source) > len(target):
                return False

            i = 0
            while i < len(source):
                if source[i] != target[i] or source[-(i+1)] != target[-(i+1)]:
                    return False
                i = i + 1
            return True

        countPairs = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixSuffix(words[i], words[j]):
                    countPairs = countPairs + 1
        return countPairs


print(Solution().countPrefixSuffixPairs(words=["a", "aba", "ababa", "aa"]))
print(Solution().countPrefixSuffixPairs(words=["pa", "papa", "ma", "mama"]))
print(Solution().countPrefixSuffixPairs(words=["abab", "ab"]))
print(Solution().countPrefixSuffixPairs(words=["a", "abb"]))
