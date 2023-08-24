# https://leetcode.com/problems/valid-number/

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        if s[0].lower() == 'e' or s[-1].lower() == 'e' or s == '.':
            return False
        splitted = s.split('e')
        if len(splitted) == 1:
            splitted = s.split('E')
        if len(splitted) > 2:
            return False
        return (self.isDecimal(splitted[0]) or self.isInteger(splitted[0])) and (len(splitted) == 1 or self.isInteger(splitted[1]))

    def isDecimal(self, s):
        match = re.search("[+-]?\d+\.\d*", s) or re.search("[+-]?\d*\.\d+", s)
        return False if not match else match.group() == s

    def isInteger(self, s):
        match = re.search("[+-]?\d+", s)
        return False if not match else match.group() == s


print(Solution().isNumber("2"))
print(Solution().isNumber("0089"))
print(Solution().isNumber("-0.1"))
print(Solution().isNumber("+3.14"))
print(Solution().isNumber("4."))
print(Solution().isNumber("-.9"))
print(Solution().isNumber("2e10"))
print(Solution().isNumber("-90E3"))
print(Solution().isNumber("3e+7"))
print(Solution().isNumber("+6e-1"))
print(Solution().isNumber("53.5e93"))
print(Solution().isNumber("-123.456e789"))
print(Solution().isNumber("abc"))
print(Solution().isNumber("1a"))
print(Solution().isNumber("1e"))
print(Solution().isNumber("e3"))
print(Solution().isNumber("99e2.5"))
print(Solution().isNumber("--6"))
print(Solution().isNumber("-+3"))
print(Solution().isNumber("95a54e53"))
print(Solution().isNumber("."))
print(Solution().isNumber("+."))
