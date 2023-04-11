# https://leetcode.com/problems/counting-bits/description/

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # x * 2 == x << 1
        # if x has 2 bits then x * 2 will have 2 + x % 2 bits
        bits = [0]
        for i in range(1, n+1):
            bits.append(bits[i//2] + (i % 2))
        return bits


print(Solution().countBits(2))
print(Solution().countBits(5))
print(Solution().countBits(7))
