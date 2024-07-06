# https://leetcode.com/problems/pass-the-pillow/description /?envType=daily-question&envId=2024-07-06

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time % ((n - 1) * 2)
        return (time + 1) if time < n else (n - (time - (n - 1)))


print(Solution().passThePillow(n=4, time=1))
print(Solution().passThePillow(n=4, time=2))
print(Solution().passThePillow(n=4, time=3))
print(Solution().passThePillow(n=4, time=4))
print(Solution().passThePillow(n=4, time=5))
print(Solution().passThePillow(n=4, time=6))
print(Solution().passThePillow(n=4, time=7))
print(Solution().passThePillow(n=4, time=8))
