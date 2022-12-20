class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 0 if n == 0 else 1
        a = 0
        b = 1
        c = 1
        while n > 2:
            a, b, c = b, c, a + b + c
            n = n - 1
        return c


print(Solution().tribonacci(25))
