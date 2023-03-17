# https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        characters = {}
        for ch in s:
            if ch in characters:
                return ch
            characters[ch] = True


print(Solution().repeatedCharacter('abccbaacz'))
print(Solution().repeatedCharacter('abcdd'))
