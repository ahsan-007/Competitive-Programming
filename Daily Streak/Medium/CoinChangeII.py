# https://leetcode.com/problems/coin-change-ii/

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.changeUtil(0, amount, coins, {})

    def changeUtil(self, i, amount: int, coins: List[int], memo) -> int:
        if amount == 0:
            return 1

        if amount < 0 or i == len(coins):
            return 0

        if i in memo and amount in memo[i]:
            return memo[i][amount]

        if i not in memo:
            memo[i] = {}

        if coins[i] > amount:
            memo[i][amount] = self.changeUtil(i+1, amount, coins, memo)
        else:
            memo[i][amount] = self.changeUtil(
                i, amount - coins[i], coins, memo) + self.changeUtil(i+1, amount, coins, memo)

        return memo[i][amount]


print(Solution().change(amount=5, coins=[1, 2, 5]))
print(Solution().change(amount=10, coins=[10]))
print(Solution().change(amount=6, coins=[1, 2, 5]))
print(Solution().change(amount=3, coins=[2, 5]))
