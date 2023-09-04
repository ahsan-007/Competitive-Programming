# https://leetcode.com/problems/unique-paths/?envType=daily-question&envId=2023-09-03

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePathsUtil(m, n, 1, 1, {})

    def uniquePathsUtil(self, m, n, i, j, memo):
        if i > m or j > n:
            return 0

        if i == m and j == n:
            return 1

        if (i, j) not in memo:
            memo[(i, j)] = self.uniquePathsUtil(m, n, i + 1, j, memo) + \
                self.uniquePathsUtil(m, n, i, j+1, memo)

        return memo[(i, j)]


print(Solution().uniquePaths(m=3, n=7))
print(Solution().uniquePaths(m=3, n=2))
