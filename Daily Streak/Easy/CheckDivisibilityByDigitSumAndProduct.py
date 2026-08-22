# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description/?envType=daily-question&envId=2026-08-22

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def getDigitSum(n):
            digit_sum = 0
            while n:
                digit_sum += n % 10
                n = n // 10
            return digit_sum

        def getDigitProduct(n):
            product = min(1, n)
            while n:
                product *= n % 10
                n = n // 10
            return product

        return n % (getDigitSum(n) + getDigitProduct(n)) == 0


print(Solution().checkDivisibility(n=90))
print(Solution().checkDivisibility(n=23))
