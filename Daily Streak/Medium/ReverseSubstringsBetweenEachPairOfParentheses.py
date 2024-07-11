# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description /?envType=daily-question&envId=2024-07-11

class Solution:
    def reverseParentheses(self, s: str) -> str:
        openBrackets = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                openBrackets.append(i)
            elif s[i] == ')':
                openBracketInd = openBrackets.pop(-1)
                s = s[:openBracketInd+1] + s[openBracketInd+1:i][::-1] + s[i:]
            i = i + 1
        return s.replace("(", "").replace(")", "")


print(Solution().reverseParentheses(s="(abcd)"))
print(Solution().reverseParentheses(s="(u(love)i)"))
print(Solution().reverseParentheses("(ed(et(oc))el)"))
