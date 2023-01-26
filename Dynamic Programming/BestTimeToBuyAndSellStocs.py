# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum = prices[0]
        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            max_profit = max(max_profit, prices[i] - minimum)
        return max_profit


print(Solution().maxProfit([7,6,4,3,1]))
