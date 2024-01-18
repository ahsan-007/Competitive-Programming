# https://leetcode.com/problems/climbing-stairs/description/?envType=daily-question&envId=2024-01-18

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n if n == 1 or n == 2 else 0

        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairsV2(self, n: int) -> int:
        if n <= 2:
            return n if n == 1 or n == 2 else 0

        nMinus1 = 1
        nMinus2 = 2

        i = 3
        while i < n:
            nMinus1, nMinus2 = nMinus2, nMinus1 + nMinus2
            i = i + 1

        return nMinus2 + nMinus1

    def climbStairsV3(self, n: int) -> int:
        a = b = 1
        for i in range(1, n):
            a, b = b, a + b
        return b


print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))

print(Solution().climbStairsV2(3))
print(Solution().climbStairsV2(4))
print(Solution().climbStairsV2(5))

print(Solution().climbStairsV3(3))
print(Solution().climbStairsV3(4))
print(Solution().climbStairsV3(5))
