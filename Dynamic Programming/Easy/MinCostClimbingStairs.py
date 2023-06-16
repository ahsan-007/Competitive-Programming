# https://leetcode.com/problems/min-cost-climbing-stairs/?envType=study-plan-v2&envId=dynamic-programming

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(self.minCost(cost, 0, memo), self.minCost(cost, 1, memo))

    # def minCost(self, cost, i, memo):
    #     if i >= len(cost):
    #         return 0

    #     if i not in memo:
    #         memo[i] = cost[i] + \
    #             min(self.minCost(cost, i+1, memo),
    #                 self.minCost(cost, i+2, memo))

    #     return memo[i]
    
    def minCost(self, cost, memo):
        step1 = 0
        step2 = 0
        current_step = 0
        while current_step < len(cost):
            step1 += cost
            step2 += cost
            


print(Solution().minCostClimbingStairs(cost=[10, 15, 20]))
print(Solution().minCostClimbingStairs(
    cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
