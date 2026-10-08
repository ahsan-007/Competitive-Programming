# https://leetcode.com/problems/remove-outermost-parentheses/description/?envType=daily-question&envId=2026-10-08

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        response = ""
        i = 0
        j = 0
        brackets = 0
        while j < len(s):
            if s[j] == "(":
                brackets += 1
            else:
                brackets -= 1

            j = j + 1
            if brackets == 0:
                response += s[i+1:j-1]
                i = j

        return response


print(Solution().removeOuterParentheses(s="(()())(())"))
print(Solution().removeOuterParentheses(s="(()())(())(()(()))"))
print(Solution().removeOuterParentheses(s="()()"))
