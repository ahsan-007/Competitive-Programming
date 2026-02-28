# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/?envType=daily-question&envId=2026-02-28

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        num = 0
        bits = 0
        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                bits += 1
            num = ((num << bits) + i) % (pow(10, 9) + 7)
        return num

    def concatenatedBinaryV2(self, n: int) -> int:
        num = 0
        for i in range(1, n + 1):
            num = ((num << i.bit_length()) + i) % (pow(10, 9) + 7)
        return num


print(Solution().concatenatedBinary(n=1))
print(Solution().concatenatedBinary(n=3))
print(Solution().concatenatedBinary(n=12))

print('-'*100)

print(Solution().concatenatedBinary(n=1))
print(Solution().concatenatedBinary(n=3))
print(Solution().concatenatedBinary(n=12))
