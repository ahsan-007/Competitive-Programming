# https://leetcode.com/problems/profitable-schemes/

from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        return self.profitableSchemesUtil(n, minProfit, group, profit, 0, 0, 0, {}) % (10**9 + 7)

    def profitableSchemesUtil(self, n: int, minProfit: int, group: List[int], profits: List[int], i, count, profit, memo):
        if i == len(profits):
            return 1 if profit >= minProfit else 0

        if (i, count, profit) not in memo:
            memo[i, count, profit] = self.profitableSchemesUtil(
                n, minProfit, group, profits, i + 1, count, profit, memo)
            if count + group[i] <= n:
                memo[i, count, profit] += self.profitableSchemesUtil(
                    n, minProfit, group, profits, i + 1, count + group[i], min(profit + profits[i], minProfit), memo)
        return memo[i, count, profit]


# class Solution:
#     def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
#         return (self.profitableSchemesUtil(n, minProfit, group, profit, 0, {}) + (1 if minProfit == 0 else 0)) % (10**9 + 7)

#     def profitableSchemesUtil(self, n: int, minProfit: int, group: List[int], profit: List[int], i, memo):
#         if n < 0 or i >= len(group):
#             return 0
#         if (n, minProfit, i) not in memo:
#             memo[n, minProfit, i] = (1 if profit[i] >= minProfit and n-group[i] >= 0 else 0) + self.profitableSchemesUtil(
#                 n-group[i], minProfit-profit[i], group, profit, i + 1, memo) + self.profitableSchemesUtil(n, minProfit, group, profit, i + 1, memo)
#         return memo[n, minProfit, i]


print(Solution().profitableSchemes(
    n=5, minProfit=3, group=[2, 2], profit=[2, 3]))


print(Solution().profitableSchemes(
    n=10, minProfit=5, group=[2, 3, 5], profit=[6, 7, 8]))

print(Solution().profitableSchemes(
    n=64, minProfit=0, group=[80, 40], profit=[88, 88]))
