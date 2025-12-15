# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/?envType=daily-question&envId=2025-12-15

from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        consecutiveDescent = 0
        count = 0
        for i in range(1, len(prices)):
            if prices[i-1] - prices[i] == 1:
                consecutiveDescent += 1

            elif consecutiveDescent > 0:
                n = consecutiveDescent + 1
                count += ((n * (n + 1)) // 2) - n
                consecutiveDescent = 0

        if consecutiveDescent > 0:
            n = consecutiveDescent + 1
            count += ((n * (n + 1)) // 2) - n

        return count + len(prices)

    def getDescentPeriodsV2(self, prices: List[int]) -> int:
        consecutiveDescent = 1
        count = 1
        for i in range(1, len(prices)):
            if prices[i-1] - prices[i] == 1:
                consecutiveDescent += 1
            else:
                consecutiveDescent = 1

            count += consecutiveDescent
        return count


print(Solution().getDescentPeriods(prices=[3, 2, 1, 4]))
print(Solution().getDescentPeriods(prices=[8, 6, 7, 7]))
print(Solution().getDescentPeriods(prices=[1]))
print(Solution().getDescentPeriods(prices=[99906, 99905, 99904, 99903, 99902, 99901, 99900, 99905, 99904, 99903, 99902, 99901, 99900, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99903, 99902, 99901, 99900, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99909, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99904,
      99903, 99902, 99901, 99900, 99910, 99909, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99910, 99909, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99900, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99909, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99908, 99907, 99906]))

print('-'*100)

print(Solution().getDescentPeriodsV2(prices=[3, 2, 1, 4]))
print(Solution().getDescentPeriodsV2(prices=[8, 6, 7, 7]))
print(Solution().getDescentPeriodsV2(prices=[1]))
print(Solution().getDescentPeriodsV2(prices=[99906, 99905, 99904, 99903, 99902, 99901, 99900, 99905, 99904, 99903, 99902, 99901, 99900, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99903, 99902, 99901, 99900, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99909, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99904,
      99903, 99902, 99901, 99900, 99910, 99909, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99910, 99909, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99900, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99909, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900, 99908, 99907, 99906]))
