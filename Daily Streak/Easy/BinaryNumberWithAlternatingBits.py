# https://leetcode.com/problems/binary-number-with-alternating-bits/description/?envType=daily-question&envId=2026-02-18

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prevBit = None
        while n > 0:
            bit = n & 1
            if bit == prevBit:
                return False
            prevBit = bit
            n = n >> 1
        return True

    def hasAlternatingBitsV2(self, n: int) -> bool:
        return n & (n >> 1) == 0 and n | (n >> 2) == n


print(Solution().hasAlternatingBits(1))
print(Solution().hasAlternatingBits(2))
print(Solution().hasAlternatingBits(3))
print(Solution().hasAlternatingBits(4))
print(Solution().hasAlternatingBits(5))
print(Solution().hasAlternatingBits(6))

print('-'*100)

print(Solution().hasAlternatingBitsV2(1))
print(Solution().hasAlternatingBitsV2(2))
print(Solution().hasAlternatingBitsV2(3))
print(Solution().hasAlternatingBitsV2(4))
print(Solution().hasAlternatingBitsV2(5))
print(Solution().hasAlternatingBitsV2(6))
