# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum_price = None
        for price in prices:
            if minimum_price is None or price < minimum_price:
                minimum_price = price
            else:
                max_profit = max(max_profit, price - minimum_price)
        return max_profit


print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit(prices=[7, 6, 4, 3, 1]))
