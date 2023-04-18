# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        i = vowels = 0
        mid = len(s) // 2
        for i in range(len(s)):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels = vowels + 1 if i < mid else vowels - 1
        return vowels == 0


print(Solution().halvesAreAlike(s="book"))
print(Solution().halvesAreAlike(s="textbook"))
