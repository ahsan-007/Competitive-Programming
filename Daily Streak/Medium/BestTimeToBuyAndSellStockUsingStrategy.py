# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/description/?envType=daily-question&envId=2025-12-18

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        totalSumOfProduct = sum(prices[i]*strategy[i]
                                for i in range(len(prices)))
        sumWithoutMod = 0
        sumWithMod = 0
        i = 0
        maxSumOfProduct = totalSumOfProduct
        while i < len(prices):
            if i < k:
                sumWithoutMod += prices[i] * strategy[i]
                if i >= k // 2:
                    sumWithMod += prices[i]

                if i == k - 1:
                    maxSumOfProduct = max(maxSumOfProduct,
                                          totalSumOfProduct - sumWithoutMod + sumWithMod)
            else:
                sumWithoutMod += prices[i] * strategy[i]
                sumWithoutMod -= prices[i-k] * strategy[i-k]

                sumWithMod += prices[i]
                sumWithMod -= prices[i-k//2]

                maxSumOfProduct = max(maxSumOfProduct,
                                      totalSumOfProduct - sumWithoutMod + sumWithMod)

            i = i + 1

        return maxSumOfProduct


print(Solution().maxProfit(prices=[4, 2, 8], strategy=[-1, 0, 1], k=2))
