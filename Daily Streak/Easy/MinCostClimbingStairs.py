# https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=daily-question&envId=2023-10-13

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost1, cost2 = cost[0], cost[1]
        i = 2
        while i < len(cost):
            cost1, cost2 = cost2, min(cost1, cost2) + cost[i]
            i = i + 1
        return min(cost1, cost2)


print(Solution().minCostClimbingStairs(cost=[10, 15, 20]))
print(Solution().minCostClimbingStairs(cost=[0, 2, 2, 1]))
print(Solution().minCostClimbingStairs(
    cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
