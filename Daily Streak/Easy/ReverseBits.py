# https://leetcode.com/problems/reverse-bits/description/?envType=daily-question&envId=2026-02-16

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(abs(n))[2:].zfill(32)
        return int(binary[::-1], 2)


print(Solution().reverseBits(n=43261596))
print(Solution().reverseBits(n=2147483644))
