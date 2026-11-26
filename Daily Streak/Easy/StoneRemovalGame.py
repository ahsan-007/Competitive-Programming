# https://leetcode.com/problems/stone-removal-game/description/?envType=daily-question&envId=2026-11-26

class Solution:
    def canAliceWin(self, n: int) -> bool:
        isAliceTurn = True
        size = 10
        while n > 0 and size <= n:
            n = n - size
            size = size - 1
            isAliceTurn = not isAliceTurn
        return not isAliceTurn

print(Solution().canAliceWin(n = 12))
print(Solution().canAliceWin(n = 1))
print(Solution().canAliceWin(n = 19))