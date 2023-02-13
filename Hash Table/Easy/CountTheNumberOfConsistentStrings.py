# https://leetcode.com/problems/count-the-number-of-consistent-strings/

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_map = {}
        for ch in allowed:
            allowed_map[ch] = True

        consistent_words = 0
        for word in words:
            should_continue = True
            i = 0
            while i < len(word) and should_continue:
                if word[i] not in allowed_map:
                    should_continue = False
                i = i + 1
            if should_continue:
                consistent_words = consistent_words + 1
        return consistent_words


print(Solution().countConsistentStrings(
    "ab", ["ad", "bd", "aaab", "baa", "badab"]))
