# https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        characters = {}
        for ch in s:
            characters[ch] = characters.get(ch, 0) + 1

        return self.longestNiceSubstringUtil(s, characters, {})

    def longestNiceSubstringUtil(self, s: str, characters, memo) -> str:
        if len(s) == 0:
            return ""

        if s in memo:
            return memo[s]

        i = 0
        isNice = True
        while isNice and i < len(s):
            if s[i].isupper():
                if characters.get(s[i].lower(), 0) == 0:
                    isNice = False
            else:
                if characters.get(s[i].upper(), 0) == 0:
                    isNice = False
            i = i + 1

        if isNice:
            memo[s] = s
            return s

        characters[s[-1]] = characters[s[-1]] - 1
        left = self.longestNiceSubstringUtil(s[:-1], characters)

        characters[s[-1]] = characters[s[-1]] + 1
        characters[s[0]] = characters[s[0]] - 1

        right = self.longestNiceSubstringUtil(s[1:], characters)
        characters[s[0]] = characters[s[0]] + 1

        memo[s] = left if len(left) >= len(right) else right
        return memo[s]


print(Solution().longestNiceSubstring(s="YazaAay"))
print(Solution().longestNiceSubstring(s="Bb"))
print(Solution().longestNiceSubstring(s="c"))
