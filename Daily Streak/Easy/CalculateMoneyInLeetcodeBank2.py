# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2025-10-25

class Solution:
    def totalMoney(self, n: int) -> int:
        def sumOfArithmeticSeries(x):
            return (x * (x + 1)) // 2

        weeks = n // 7
        days = n % 7

        # sum of money for weeks (quotient) + sum of money for days (modulus)
        # week1: 1+2+3+4+5+6+7 --> 28 + 0 = 28 --> 28
        # week2: 2+3+4+5+6+7+8 --> 28 + 7 = 35 --> 63
        # week3: 3+4+5+6+7+8+9 --> 28 + 14 = 42 --> 105
        # weekn: f(7) * n//7 + f(n-1 if n >0 else 0) * 7
        # This will generate the sum for the weeks, then add the money for days to calculate the total money
        # dayn: (n%7) + n//7, e.g. for day 23, money is 2 + 3
        # money for remaining days can be calculated by taking the sum of series from 1 to di and then adding the offset which is (n//7)*(n%7)
        return ((sumOfArithmeticSeries(7) * weeks) + sumOfArithmeticSeries(weeks-1 if weeks > 0 else 0) * 7) + (sumOfArithmeticSeries(days) + (weeks * days))


print(Solution().totalMoney(n=4))
print(Solution().totalMoney(n=10))
print(Solution().totalMoney(n=20))
