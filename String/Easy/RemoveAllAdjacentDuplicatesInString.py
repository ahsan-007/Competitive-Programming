# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                s = s[:i] + (s[i+2:] if i + 2 < len(s) else "")
                if i != 0:
                    i = i - 1
            else:
                i = i + 1
        return s


print(Solution().removeDuplicates("axzzxy"))
print(Solution().removeDuplicates("aababaab"))
print(Solution().removeDuplicates("aaaaaaaaa"))
