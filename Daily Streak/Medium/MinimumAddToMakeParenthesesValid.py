# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=daily-question&envId=2026-10-06

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unbalancedOpeningBrackets = 0
        unbalancedClosingBrackets = 0

        for ch in s:
            if ch == '(':
                unbalancedOpeningBrackets += 1
            elif ch == ')':
                if unbalancedOpeningBrackets == 0:
                    unbalancedClosingBrackets += 1
                else:
                    unbalancedOpeningBrackets -= 1

        return unbalancedOpeningBrackets + unbalancedClosingBrackets

    def minAddToMakeValidV2(self, s: str) -> int:
        min_add = 0
        brackets = 0
        for ch in s:
            if ch == '(':
                brackets += 1
            else:
                brackets -= 1

            if brackets < 0:
                min_add += 1
                brackets = 0
        return min_add + brackets


print(Solution().minAddToMakeValid(s="())"))
print(Solution().minAddToMakeValid(s="((("))
print(Solution().minAddToMakeValid(s="()))(("))

print('-' * 100)

print(Solution().minAddToMakeValidV2(s="())"))
print(Solution().minAddToMakeValidV2(s="((("))
print(Solution().minAddToMakeValidV2(s="()))(("))
