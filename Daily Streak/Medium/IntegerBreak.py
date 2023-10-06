# https://leetcode.com/problems/integer-break/description/?envType=daily-question&envId=2023-10-06


class Solution:
    def integerBreak(self, n: int) -> int:
        return self.integerBreakUtil(n, {})

    def integerBreakUtil(self, n, memo):
        if n == 1:
            return n

        if n not in memo:
            max_product = 0
            for i in range(1, n//2 + 1):
                max_product = max(
                    max_product, i * self.integerBreakUtil(n-i, memo), i * (n - i))
            memo[n] = max_product
        return memo[n]


print(Solution().integerBreak(n=2))
print(Solution().integerBreak(n=10))
print(Solution().integerBreak(n=58))
