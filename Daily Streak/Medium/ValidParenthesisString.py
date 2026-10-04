# https://leetcode.com/problems/valid-parenthesis-string/description/?envType=daily-question&envId=2026-10-04

class Solution:
    def checkValidString(self, s: str) -> bool:
        def checkValidStringUtil(s, i, brackets, memo):
            if brackets < 0:
                return False

            if i == len(s):
                return brackets == 0

            if (i, brackets) not in memo:
                if s[i] == '(':
                    memo[(i, brackets)] = checkValidStringUtil(
                        s, i+1, brackets+1, memo)
                elif s[i] == ')':
                    memo[(i, brackets)] = checkValidStringUtil(
                        s, i+1, brackets-1, memo)
                else:
                    memo[(i, brackets)] = checkValidStringUtil(s, i+1, brackets+1, memo) or checkValidStringUtil(
                        s, i+1, brackets-1, memo) or checkValidStringUtil(s, i+1, brackets, memo)
            return memo[(i, brackets)]
        return checkValidStringUtil(s, 0, 0, {})


print(Solution().checkValidString(s="()"))
print(Solution().checkValidString(s="(*)"))
print(Solution().checkValidString(s="(*))"))
print(Solution().checkValidString(s="("))
print(Solution().checkValidString(
    s="(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
