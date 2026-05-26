# https://leetcode.com/problems/count-the-number-of-special-characters-i/description/?envType=daily-question&envId=2026-05-26

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = [False] * 52
        for ch in word:
            if ord('a') <= ord(ch) <= ord('z'):
                chars[ord(ch) - ord('a')] = True
            else:
                chars[ord(ch) - ord('A') + 26] = True

        count = 0
        for i in range(26):
            if chars[i] and chars[i+26]:
                count += 1
        return count


print(Solution().numberOfSpecialChars(word="aaAbcBC"))
print(Solution().numberOfSpecialChars(word="abc"))
print(Solution().numberOfSpecialChars(word="abBCab"))
