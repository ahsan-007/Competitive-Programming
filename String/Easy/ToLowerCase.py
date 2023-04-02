# https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, s: str) -> str:
        i = 0
        while i < len(s):
            if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
                # ascii code of space is 32 which can be used to convert
                # lower case letter into uppercase or vice versa
                s = s[:i] + chr(ord(s[i]) + ord(' ')) + s[i+1:]
            i = i + 1
        return s


print(Solution().toLowerCase(s="Hello"))
print(Solution().toLowerCase(s="here"))
print(Solution().toLowerCase(s="LOVELY"))
