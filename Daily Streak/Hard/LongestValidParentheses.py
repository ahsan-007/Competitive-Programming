# https://leetcode.com/problems/longest-valid-parentheses/description/?envType=daily-question&envId=2026-10-03

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def longestValidParenthesesUtil(s, i):
            if i >= len(s):
                return 0

            parenthesis = 0
            j = i
            lastBalancedAtInd = j
            while j < len(s) and parenthesis >= 0:
                parenthesis = parenthesis + (1 if s[j] == "(" else -1)

                if parenthesis == 0:
                    lastBalancedAtInd = j
                j = j + 1

            return max((lastBalancedAtInd - i + 1) if lastBalancedAtInd != i else 0,
                       longestValidParenthesesUtil(s, lastBalancedAtInd + 1) if parenthesis <= 0 else 0)

        reversedInvertedS = "".join(
            "(" if ch == ")" else ")" for ch in s[::-1])
        return max(longestValidParenthesesUtil(s, 0), longestValidParenthesesUtil(reversedInvertedS, 0))


print(Solution().longestValidParentheses(s="(()"))
print(Solution().longestValidParentheses(s=")()())"))
