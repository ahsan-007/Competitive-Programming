# https://leetcode.com/problems/length-of-last-word/description/?envType=daily-question&envId=2024-04-01

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        while i >= 0 and (length == 0 or s[i] != ' '):
            if s[i] != ' ':
                length = length + 1
            i = i - 1
        return length


print(Solution().lengthOfLastWord(s="Hello World"))
print(Solution().lengthOfLastWord(s="   fly me   to   the moon  "))
print(Solution().lengthOfLastWord(s="luffy is still joyboy"))
