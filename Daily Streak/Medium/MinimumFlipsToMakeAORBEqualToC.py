# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bits_to_flip = 0
        while a or b or c:
            bits_to_flip = bits_to_flip + \
                self.getBitsToFlip(a % 2, b % 2, c % 2)
            a, b, c = a//2, b//2, c//2
        return bits_to_flip

    def getBitsToFlip(self, b1, b2, t):
        return 0 if b1 | b2 == t else b1+b2+t


print(Solution().minFlips(a=2, b=6, c=5))
print(Solution().minFlips(a=4, b=2, c=7))
print(Solution().minFlips(a=1, b=2, c=3))
