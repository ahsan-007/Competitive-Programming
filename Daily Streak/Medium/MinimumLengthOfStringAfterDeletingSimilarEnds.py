# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/?envType=daily-question&envId=2024-03-05

class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] == s[j]:
                ch = s[i]
                while i <= j and s[i] == ch:
                    i = i + 1

                while j > i and s[j] == ch:
                    j = j - 1
            else:
                return j - i + 1
        return j - i + 1


print(Solution().minimumLength(s="ca"))
print(Solution().minimumLength(s="cabaabac"))
print(Solution().minimumLength(s="aabccabba"))
