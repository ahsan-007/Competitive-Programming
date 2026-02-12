# https://leetcode.com/problems/longest-balanced-substring-i/description/?envType=daily-question&envId=2026-02-12

class Solution:
    def longestBalanced(self, s: str) -> int:
        maxLength = 0
        for i in range(len(s)):
            chracterCount = [0] * 26
            for j in range(i, len(s)):
                ind = ord(s[j]) - ord('a')
                chracterCount[ind] += 1
                if all(count == 0 or count == chracterCount[ind] for count in chracterCount):
                    maxLength = max(maxLength, j - i + 1)
        return maxLength


print(Solution().longestBalanced(s="abbac"))
print(Solution().longestBalanced(s="zzabccy"))
print(Solution().longestBalanced(s="aba"))
