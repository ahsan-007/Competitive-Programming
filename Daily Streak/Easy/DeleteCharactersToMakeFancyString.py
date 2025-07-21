# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/?envType=daily-question&envId=2025-07-21


class Solution:
    def makeFancyString(self, s: str) -> str:
        fancyString = ""
        for ch in s:
            if len(fancyString) < 2 or fancyString[-1] != fancyString[-2] or ch != fancyString[-1]:
                fancyString += ch
        return fancyString
            
    
    
print(Solution().makeFancyString(s = "leeetcode")) #leetcode
print(Solution().makeFancyString(s = "aaabaaaa")) #leetcode
