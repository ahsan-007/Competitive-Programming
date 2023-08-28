# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 2
        goodStrings = 0
        while i < len(s):
            if s[i] != s[i-1] and s[i] != s[i-2] and s[i-1] != s[i-2]:
                goodStrings += 1
            i = i + 1
        return goodStrings


print(Solution().countGoodSubstrings(s="xyzzaz"))
print(Solution().countGoodSubstrings(s="aababcabc"))
print(Solution().countGoodSubstrings(s="a"))
print(Solution().countGoodSubstrings(s="ab"))
print(Solution().countGoodSubstrings(s="abc"))
print(Solution().countGoodSubstrings(s="aba"))
