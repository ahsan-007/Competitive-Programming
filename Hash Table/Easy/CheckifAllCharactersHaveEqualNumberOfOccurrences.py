# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequency = {}
        for ch in s:
            if ch in frequency:
                frequency[ch] = frequency[ch] + 1
            else:
                frequency[ch] = 1

        occurrence_count = frequency[s[0]]
        for key in frequency:
            if frequency[key] != occurrence_count:
                return False
        return True

print(Solution().areOccurrencesEqual("abacbc"))
print(Solution().areOccurrencesEqual("aaabb"))
