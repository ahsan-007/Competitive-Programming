# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        i = 0
        reversed = 0
        while i < 32:
            reversed = (reversed << 1) + (n % 2)
            i = i + 1
            if n != 0:
                n = n // 2
        return reversed


print(Solution().reverseBits(43261596))
print(Solution().reverseBits(4294967293))
