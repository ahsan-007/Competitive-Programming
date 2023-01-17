# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePathsUtil(0, 0, m, n)

    def uniquePathsUtil(self, i, j, m, n, memo={}):
        if i >= m or j >= n:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        if i == (m-1) and j == (n-1):
            memo[(i, j)] = 1
            return memo[(i, j)]

        memo[(i, j)] = self.uniquePathsUtil(i+1, j, m, n, memo) + \
            self.uniquePathsUtil(i, j + 1, m, n, memo)
        return memo[(i, j)]


print(Solution().uniquePaths(15, 15))
