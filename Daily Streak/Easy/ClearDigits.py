# https://leetcode.com/problems/clear-digits/description /?envType=daily-question&envId=2025-02-10

class Solution:
    def clearDigits(self, s: str) -> str:
        charInd = -1
        i = 0
        while i < len(s):
            if s[i].isdigit() and charInd != -1:
                s = s[:charInd] + s[charInd+1:]
                i = i - 1
                s = s[:i] + s[i+1:]
                charInd = charInd - 1
            else:
                if s[i].isalpha():
                    charInd = i
                i = i + 1
        return s


print(Solution().clearDigits(s="abc"))
print(Solution().clearDigits(s="cb34"))
