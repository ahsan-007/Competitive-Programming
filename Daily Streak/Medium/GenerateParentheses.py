# https://leetcode.com/problems/generate-parentheses/description/?envType=daily-question&envId=2026-10-02

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def generateParenthesisUtil(open, close, combination):
            if close == 0 and open == 0:
                return [combination]

            combinations = []
            if open > 0:
                combinations.extend(generateParenthesisUtil(
                    open - 1, close, combination + "("))

            if close > open:
                combinations.extend(generateParenthesisUtil(
                    open, close - 1, combination + ")"))

            return combinations

        return generateParenthesisUtil(n, n, "")


print(Solution().generateParenthesis(n=3))
print(Solution().generateParenthesis(n=1))
