# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/description/?envType=daily-question&envId=2026-11-11

class Solution:
    # Time: O(1), Space: O(1)
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        return min(
            costBoth * max(need1, need2),
            costBoth * min(need1, need2) + ((cost1 * (need1 - need2)) if min(need1, need2) == need2 else (cost2 * (need2 - need1))),
            cost1 * need1 + cost2 * need2
        )

print(Solution().minimumCost(cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2))
print(Solution().minimumCost(cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3))
print(Solution().minimumCost(cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0))