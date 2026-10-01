# https://leetcode.com/problems/valid-parentheses/description /?envType=daily-question&envId=2026-10-01

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parantheses = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for ch in s:
            if ch in parantheses:
                stack.append(ch)
            elif not stack or ch != parantheses[stack[-1]]:
                return False
            else:
                stack.pop()
        return not stack


print(Solution().isValid(s="()"))
print(Solution().isValid(s="()[]{}"))
print(Solution().isValid(s="(]"))
print(Solution().isValid(s="([)]"))
