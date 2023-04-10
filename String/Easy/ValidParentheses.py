# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for bracket in s:
            if bracket in [')', '}', ']']:
                if not brackets or (bracket == ')' and brackets[-1] != '(') or (bracket == '}' and brackets[-1] != '{') or (bracket == ']' and brackets[-1] != '['):
                    return False
                brackets.pop()
            else:
                brackets.append(bracket)
        return not brackets


print(Solution().isValid(s="()"))
print(Solution().isValid(s="()[]{}"))
print(Solution().isValid(s="(}"))
print(Solution().isValid(s="{[]}"))
print(Solution().isValid(s="["))
