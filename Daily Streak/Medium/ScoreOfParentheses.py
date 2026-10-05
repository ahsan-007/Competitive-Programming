# https://leetcode.com/problems/score-of-parentheses/description/?envType=daily-question&envId=2026-10-05

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def scoreOfParenthesesUtil(s: str, i: int, j: int) -> int:
            if i > j:
                return 0

            brackets = 0
            k = i
            while k <= j and (k == i or brackets != 0):
                if s[k] == '(':
                    brackets += 1
                else:
                    brackets -= 1
                k = k + 1

            if k - i == 2:
                return 1 + scoreOfParenthesesUtil(s, k, j)

            return (2 * scoreOfParenthesesUtil(s, i+1, k-2)) + scoreOfParenthesesUtil(s, k, j)
        return scoreOfParenthesesUtil(s, 0, len(s)-1)

    def scoreOfParenthesesV2(self, s: str) -> int:
        score = 0
        depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i-1] == "(":
                    score += pow(2, depth)
        return score


print(Solution().scoreOfParentheses(s="()"))
print(Solution().scoreOfParentheses(s="(())"))
print(Solution().scoreOfParentheses(s="()()"))
print(Solution().scoreOfParentheses(s="(())()"))
print(Solution().scoreOfParentheses(s="(()(()))"))

print('-' * 100)

print(Solution().scoreOfParenthesesV2(s="()"))
print(Solution().scoreOfParenthesesV2(s="(())"))
print(Solution().scoreOfParenthesesV2(s="()()"))
print(Solution().scoreOfParenthesesV2(s="(())()"))
print(Solution().scoreOfParenthesesV2(s="(()(()))"))
