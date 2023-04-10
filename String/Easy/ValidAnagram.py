# https://leetcode.com/problems/valid-anagram/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = Counter(s)
        t_freq = Counter(t)
        for key in t_freq:
            if s_freq.get(key, 0) != t_freq[key]:
                return False
        return True


print(Solution().isAnagram(s="anagram", t="nagaram"))
print(Solution().isAnagram(s="rat", t="car"))
