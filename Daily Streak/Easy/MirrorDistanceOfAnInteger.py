9  # https://leetcode.com/problems/mirror-distance-of-an-integer/description/?envType=daily-question&envId=2026-04-18


class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))

    def mirrorDistanceV2(self, n: int) -> int:
        def reverse_int(n):
            reversed_int = 0
            while n:
                reversed_int = (reversed_int * 10) + (n % 10)
                n = n // 10
            return reversed_int
        return abs(n - reverse_int(n))


print(Solution().mirrorDistance(25))
print(Solution().mirrorDistance(10))
print(Solution().mirrorDistance(7))

print('-'*100)

print(Solution().mirrorDistanceV2(25))
print(Solution().mirrorDistanceV2(10))
print(Solution().mirrorDistanceV2(7))
