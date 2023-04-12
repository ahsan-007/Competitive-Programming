# https://leetcode.com/problems/coin-change/

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        return self.coinChangeUtil(coins, amount, memo)

    def coinChangeUtil(self, coins, amount, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in memo:
            return memo[amount]
        change = -1
        for coin in coins:
            remaining_ammount = amount - coin
            if remaining_ammount >= 0:
                remaining_coins = self.coinChangeUtil(
                    coins, remaining_ammount, memo) + 1
                if remaining_coins > 0:
                    change = min(remaining_coins,
                                 change) if change != -1 else remaining_coins
                    memo[remaining_ammount] = remaining_coins - 1
        memo[amount] = change
        return change


print(Solution().coinChange([1, 2, 5], 11))
print(Solution().coinChange([186, 419, 83, 408], 6249))
print(Solution().coinChange([5, 8], 58))
print(Solution().coinChange([5, 6], 16))
print(Solution().coinChange([5, 4], 8))
