# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/?envType=daily-question&envId=2026-11-22

class Solution:
    def checkString(self, s: str) -> bool:
        bFound = False
        for ch in s:
            if bFound:
                if ch == 'a':
                    return False
            elif ch == 'b':
                bFound = True
        return True


print(Solution().checkString(s="aaabbb"))
print(Solution().checkString(s="abab"))
print(Solution().checkString(s="bbb"))
