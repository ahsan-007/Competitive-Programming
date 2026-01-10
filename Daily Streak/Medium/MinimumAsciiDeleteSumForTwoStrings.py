# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/?envType=daily-question&envId=2026-01-10

class Solution:
    # Top Down with Memoization
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}

        def minimumDeleteSumUtil(s1, s2, i, j):
            if i >= len(s1) or j >= len(s2):
                return sum(ord(s2[k]) for k in range(j, len(s2))) + sum(ord(s1[k]) for k in range(i, len(s1)))

            if (i, j) not in memo:
                if s1[i] == s2[j]:
                    memo[(i, j)] = minimumDeleteSumUtil(s1, s2, i+1, j+1)

                else:
                    memo[(i, j)] = min(minimumDeleteSumUtil(s1, s2, i + 1, j) + ord(s1[i]),
                                       minimumDeleteSumUtil(s1, s2, i, j + 1) + ord(s2[j]))

            return memo[(i, j)]

        return minimumDeleteSumUtil(s1, s2, 0, 0)

    # Bottom Up
    def minimumDeleteSumV2(self, s1: str, s2: str) -> int:
        grid = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

        for i in range(1, len(grid)):
            grid[i][0] = grid[i-1][0] + ord(s2[i-1])

        for j in range(1, len(grid[0])):
            grid[0][j] = grid[0][j-1] + ord(s1[j-1])

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if s1[j-1] != s2[i-1]:
                    grid[i][j] = min(grid[i-1][j] + ord(s2[i-1]),
                                     grid[i][j-1] + ord(s1[j-1]))
                else:
                    grid[i][j] = grid[i-1][j-1]

        return grid[i][j]


print(Solution().minimumDeleteSum(s1="sea", s2="eat"))
print(Solution().minimumDeleteSum(s1="delete", s2="leet"))

print('-' * 100)

print(Solution().minimumDeleteSumV2(s1="sea", s2="eat"))
print(Solution().minimumDeleteSumV2(s1="delete", s2="leet"))
