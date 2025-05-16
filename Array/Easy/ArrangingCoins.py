# https://leetcode.com/problems/arranging-coins/description/


class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        rows = 0
        while n >= i:
            rows = rows + 1
            n = n - i
            i = i + 1
        return rows


print(Solution().arrangeCoins(n=5))
print(Solution().arrangeCoins(n=8))
print(Solution().arrangeCoins(n=6))
