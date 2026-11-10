# https://leetcode.com/problems/climbing-stairs-ii/description/?envType=daily-question&envId=2026-11-10

from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        def climbStairsUtil(costs, i, j, memo):
            if j > len(costs):
                return float("+inf")

            if (i, j) not in memo:
                if j > 0:
                    memo[(i, j)] = costs[j - 1] + (j - i) ** 2
                else:
                    memo[(i, j)] = 0

                if j < len(costs):
                    memo[(i, j)] += min(
                        climbStairsUtil(costs, j, j + 1, memo),
                        climbStairsUtil(costs, j, j + 2, memo),
                        climbStairsUtil(costs, j, j + 3, memo)
                    )
            return memo[(i, j)]

        return climbStairsUtil(costs, 0, 0, {})


print(Solution().climbStairs(n=4, costs=[1, 2, 3, 4]))
print(Solution().climbStairs(n=4, costs=[5, 1, 6, 2]))
print(Solution().climbStairs(n=3, costs=[9, 8, 3]))
