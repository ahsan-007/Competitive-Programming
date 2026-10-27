# https://leetcode.com/problems/create-grid-with-exactly-one-path/description/?envType=daily-question&envId=2026-10-27

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ['.' + '#' * (n - 1)] * (m - 1) + ['.' * n]


print(Solution().createGrid(m=2, n=3))
print(Solution().createGrid(m=3, n=3))
print(Solution().createGrid(m=1, n=4))
