# https://leetcode.com/problems/wildcard-matching/description/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.isMatchUtil(s, p, 0, 0, {})

    def isMatchUtil(self, s, p, i, j, memo):
        if i == len(s) and j == len(p):
            return True

        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s) and j < len(p) and p[j] == '*':
            memo[(i, j)] = self.isMatchUtil(s, p, i, j + 1, memo)
            return memo[(i, j)]

        if i >= len(s) or j >= len(p):
            memo[(i, j)] = False
            return memo[(i, j)]

        if s[i] == p[j] or p[j] == '?':
            memo[(i, j)] = self.isMatchUtil(s, p, i+1, j+1, memo)
            return memo[(i, j)]

        elif p[j] == '*':
            memo[(i, j)] = self.isMatchUtil(s, p, i+1, j,
                                            memo) or self.isMatchUtil(s, p, i, j+1, memo)
            return memo[(i, j)]

        return False


print(Solution().isMatch(s="aa", p="a"))
print(Solution().isMatch(s="aa", p="*"))
print(Solution().isMatch(s="cb", p="?a"))
print(Solution().isMatch(s="adceb", p="*a*b"))
print(Solution().isMatch(s="", p="******"))
