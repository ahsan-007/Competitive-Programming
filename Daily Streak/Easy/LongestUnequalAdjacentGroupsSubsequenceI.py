# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/?envType=daily-question&envId=2025-05-15

from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        longestSequence = []
        lastGroup = None
        for i in range(len(words)):
            if groups[i] != lastGroup:
                longestSequence.append(words[i])
                lastGroup = groups[i]
        return longestSequence


print(Solution().getLongestSubsequence(
    words=["e", "a", "b"], groups=[0, 0, 1]))
print(Solution().getLongestSubsequence(
    words=["a", "b", "c", "d"], groups=[1, 0, 1, 1]))
