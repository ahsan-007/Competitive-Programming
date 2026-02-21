# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/?envType=daily-question&envId=2026-02-21

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            if n <= 1:
                return False

            divisor = 1
            while divisor <= n // 2:
                if n % divisor == 0 and divisor != 1:
                    return False
                divisor += 1
            return True

        count = 0
        for num in range(left, right+1):
            bits = bin(num).count("1")
            if isPrime(bits):
                count += 1
        return count

    def countPrimeSetBitsV2(self, left: int, right: int) -> int:
        count = 0
        for num in range(left, right+1):
            # 1 <= left <= right <= 10^6
            # log(10^6, 2) is 19, so a num can have 19 bits at max
            if bin(num).count("1") in {2, 3, 5, 7, 11, 13, 17, 19}:
                count += 1
        return count

    # one liner
    def countPrimeSetBitsV3(self, left: int, right: int) -> int:
        return sum(1 if bin(num).count("1") in {2, 3, 5, 7, 11, 13, 17, 19} else 0 for num in range(left, right+1))


print(Solution().countPrimeSetBits(left=6, right=10))
print(Solution().countPrimeSetBits(left=10, right=15))

print('-'*100)

print(Solution().countPrimeSetBitsV2(left=6, right=10))
print(Solution().countPrimeSetBitsV2(left=10, right=15))

print('-'*100)

print(Solution().countPrimeSetBitsV3(left=6, right=10))
print(Solution().countPrimeSetBitsV3(left=10, right=15))
