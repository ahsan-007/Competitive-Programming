# https://leetcode.com/problems/count-total-number-of-colored-cells/description/?envType=daily-question&envId=2025-03-05


class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n * (n - 1) * 2


print(Solution().coloredCells(n=1))
print(Solution().coloredCells(n=2))
print(Solution().coloredCells(n=3))
print(Solution().coloredCells(n=100))
print(Solution().coloredCells(n=100000))
