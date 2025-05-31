# https://leetcode.com/problems/find-the-difference/description/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sFreq = {}
        for ch in s:
            sFreq[ch] = sFreq.get(ch, 0) + 1

        for ch in t:
            if sFreq.get(ch, 0) == 0:
                return ch
            sFreq[ch] = sFreq[ch] - 1


print(Solution().findTheDifference(s="abcd", t="abcde"))
print(Solution().findTheDifference(s="", t="y"))
