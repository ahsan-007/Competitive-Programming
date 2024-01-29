# https://leetcode.com/problems/distinct-subsequences/description/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def numDistinctUtil(s, t, i, j, memo):
            if j >= len(t):
                return 1

            if i >= len(s):
                return 0

            if (i, j) not in memo:
                memo[(i, j)] = (numDistinctUtil(
                    s, t, i+1, j+1, memo) if s[i] == t[j] else 0) + numDistinctUtil(s, t, i+1, j, memo)

            return memo[(i, j)]

        return numDistinctUtil(s, t, 0, 0, {})


print(Solution().numDistinct(s="rabbbit", t="rabbit"))
print(Solution().numDistinct(s="babgbag"*100, t="bag"*100))
