# https://leetcode.com/problems/reorganize-string/

from collections import Counter
import math


class Solution:
    def reorganizeString(self, s: str) -> str:
        characters = [[key, value] for key, value in Counter(s).items()]
        characters.sort(key=lambda pair: pair[1], reverse=True)

        if characters[0][1] > math.ceil(len(s) / 2):
            return ""

        rearranged = ""
        ch = None
        i = 0
        while i < len(s):
            if not ch or ch[1] == 0:
                ch = characters.pop(0)
            rearranged += ch[0]
            ch[1] -= 1
            i = i + 2

        i = 1
        while i < len(s):
            if not ch or ch[1] == 0:
                ch = characters.pop(0)
            rearranged = rearranged[:i] + ch[0] + rearranged[i:]
            ch[1] -= 1
            i = i + 2

        return rearranged


print(Solution().reorganizeString("aab"))
print(Solution().reorganizeString("aaabbbcc"))
print(Solution().reorganizeString("ccba"))
print(Solution().reorganizeString("aaabbbccc"))
print(Solution().reorganizeString("aaab"))
print(Solution().reorganizeString("aabcc"))
print(Solution().reorganizeString("vvvlo"))
print(Solution().reorganizeString("baaba"))
print(Solution().reorganizeString("aaa"))
