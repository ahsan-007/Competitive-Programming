# https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2024-02-19

import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        n = abs(n)
        base = 2
        while n > 1:
            if n % base != 0:
                if base == 2:
                    return False
                else:
                    base = 2
            else:
                n = n // base
                base = base * 2

        return True

    def isPowerOfTwoV2(self, n: int) -> bool:
        def isPowerOfTwoUtil(n, base):
            if n == 1:
                return True

            if n < 1 or (n % base != 0 and n % 2 != 0):
                return False

            return isPowerOfTwoUtil(n // base, base * 2) if n % base == 0 else isPowerOfTwoUtil(n, 2)

        return isPowerOfTwoUtil(n, 2)


print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(2))
print(Solution().isPowerOfTwo(4))
print(Solution().isPowerOfTwo(8))
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(15))
print(Solution().isPowerOfTwo(-16))

print('-'*100)

print(Solution().isPowerOfTwoV2(1))
print(Solution().isPowerOfTwoV2(2))
print(Solution().isPowerOfTwoV2(4))
print(Solution().isPowerOfTwoV2(8))
print(Solution().isPowerOfTwoV2(16))
print(Solution().isPowerOfTwoV2(15))
print(Solution().isPowerOfTwoV2(-16))
