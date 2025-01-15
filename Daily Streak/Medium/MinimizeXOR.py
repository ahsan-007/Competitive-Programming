# https://leetcode.com/problems/minimize-xor/description /?envType=daily-question&envId=2025-01-15

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def countBits(num):
            bits = 0
            while num > 1:
                bits = bits + num % 2
                num = num // 2
            return bits + num

        num1Bits = countBits(num1)
        num2Bits = countBits(num2)
        num1Copy = num1
        xor = 0
        pow = 1
        while num1Bits != num2Bits:
            if num1Bits > num2Bits:
                if num1 % 2 == 1:
                    xor = xor + pow
                    num1Bits = num1Bits - 1

                num1 = num1 >> 1
                pow = pow * 2

            elif num2Bits > num1Bits:
                if num1 % 2 == 0:
                    xor = xor + pow
                else:
                    num1Bits = num1Bits - 1

                num2Bits = num2Bits - 1
                num1 = num1 >> 1
                pow = pow * 2

        return xor ^ num1Copy


print(Solution().minimizeXor(num1=3, num2=5))
print(Solution().minimizeXor(num1=1, num2=12))
