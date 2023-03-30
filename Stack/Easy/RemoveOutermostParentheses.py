# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        filtered_parenthesis = ''
        i = bracket = j = 0
        while i < len(s):
            bracket = bracket + 1 if s[i] == '(' else bracket - 1
            if bracket == 0:
                filtered_parenthesis = filtered_parenthesis + s[j+1: i]
                j = i + 1
                bracket = 0
            i = i + 1
        return filtered_parenthesis


print(Solution().removeOuterParentheses('(()())(())'))
print(Solution().removeOuterParentheses('(()())(())(()(()))'))
print(Solution().removeOuterParentheses('()()'))
