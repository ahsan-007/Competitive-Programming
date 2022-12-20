class Solution:
    # Bottom Up
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

    # Top Down
    def tribonacciBU(self, n: int, numbers=[0, 1, 1]):
        if n < len(numbers):
            return numbers[n]
        numbers.append(self.tribonacciBU(
            n-1, numbers) + self.tribonacciBU(n-2, numbers) + self.tribonacciBU(n-3, numbers))
        return numbers[n]


print(Solution().tribonacciBU(25))
