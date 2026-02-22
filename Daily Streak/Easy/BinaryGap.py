# https://leetcode.com/problems/binary-gap/description/?envType=daily-question&envId=2026-02-22

import math


class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        prevIndex = None
        maxGap = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                if prevIndex is not None:
                    maxGap = max(maxGap, i - prevIndex)
                prevIndex = i
        return maxGap

    def binaryGapV2(self, n: int) -> int:
        prevIndex = None
        maxGap = 0
        i = 0
        while n > 0:
            if n % 2 == 1:
                if prevIndex is not None:
                    maxGap = max(maxGap, i - prevIndex)
                prevIndex = i
            n = n // 2
            i = i + 1
        return maxGap


print(Solution().binaryGap(n=22))
print(Solution().binaryGap(n=8))
print(Solution().binaryGap(n=5))

print('-' * 100)

print(Solution().binaryGapV2(n=22))
print(Solution().binaryGapV2(n=8))
print(Solution().binaryGapV2(n=5))
