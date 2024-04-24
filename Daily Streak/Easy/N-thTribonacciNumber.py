# https://leetcode.com/problems/n-th-tribonacci-number/description /?envType=daily-question&envId=2024-04-24

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        a, b, c = 0, 1, 1
        n = n - 2
        while n > 0:
            a, b, c = b, c, a+b+c
            n = n - 1
        return c

    def tribonacciV2(self, n: int) -> int:
        def tribonacciUtil(n, memo):
            if n not in memo:
                memo[n] = tribonacciUtil(
                    n-1, memo) + tribonacciUtil(n-2, memo) + tribonacciUtil(n-3, memo)
            return memo[n]

        return tribonacciUtil(n, {0: 0, 1: 1, 2: 1})


print(Solution().tribonacci(n=1))
print(Solution().tribonacci(n=4))
print(Solution().tribonacci(n=25))


print(Solution().tribonacciV2(n=1))
print(Solution().tribonacciV2(n=4))
print(Solution().tribonacciV2(n=25))
