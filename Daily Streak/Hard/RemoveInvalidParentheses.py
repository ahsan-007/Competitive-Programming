# https://leetcode.com/problems/remove-invalid-parentheses/description/?envType=daily-question&envId=2026-10-07

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def removeInvalidParenthesesUtil(s, i, combination, balance, memo):
            if i == len(s):
                if balance == 0:
                    return {combination}
                else:
                    return set()

            if balance < 0:
                return set()

            if (i, combination, balance) not in memo:
                combinations = removeInvalidParenthesesUtil(
                    s, i+1, combination, balance, memo)

                if s[i] == '(':
                    balance += 1
                elif s[i] == ')':
                    balance -= 1

                memo[(i, combination, balance)] = combinations.union(
                    removeInvalidParenthesesUtil(s, i+1, combination + s[i], balance, memo))
            return memo[(i, combination, balance)]

        combinations = removeInvalidParenthesesUtil(s, 0, "", 0, {})
        max_length = max(len(combination)
                         for combination in combinations) if combinations else 0
        return [combination for combination in combinations if len(combination) == max_length]


print(Solution().removeInvalidParentheses(s="()())()"))
print(Solution().removeInvalidParentheses(s="(a)())()"))
print(Solution().removeInvalidParentheses(s=")("))
print(Solution().removeInvalidParentheses(s="(((((((((((((((aaaa)))))"))
