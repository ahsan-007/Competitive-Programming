# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2023-12-06

class Solution:
    def totalMoney(self, n: int) -> int:
        day = 1
        money = 0
        prevMonday = 1
        currMoney = 1
        for i in range(n):
            money = money + currMoney
            currMoney = currMoney + 1
            day = (day + 1) % 8
            if day == 0:
                day = 1
                currMoney = prevMonday + 1
                prevMonday = currMoney
        return money


print(Solution().totalMoney(n=4))
print(Solution().totalMoney(n=10))
print(Solution().totalMoney(n=20))
