# https://leetcode.com/problems/construct-k-palindrome-strings/description/?envType=daily-question&envId=2025-01-11

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        frequency = Counter(s)
        oddFrequencies = sum([1 for ch in frequency if frequency[ch] % 2 != 0])
        return oddFrequencies <= k <= len(s)


print(Solution().canConstruct(s="annabelle", k=2))
print(Solution().canConstruct(s="leetcode", k=3))
print(Solution().canConstruct(s="true", k=4))
print(Solution().canConstruct(s="cr", k=7))
