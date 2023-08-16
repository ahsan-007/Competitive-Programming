# https://leetcode.com/problems/combination-sum/

from typing import List
from copy import deepcopy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = []
        self.combinationSumUtil(0, candidates, target, [])
        return self.combinations

    def combinationSumUtil(self, i, candidates, target, comb):
        if target == 0:
            self.combinations.append(deepcopy(comb))
            return

        if target < 0 or i >= len(candidates):
            return

        if candidates[i] <= target:
            comb.append(candidates[i])
            self.combinationSumUtil(
                i, candidates, target - candidates[i], comb)
            comb.pop()

        self.combinationSumUtil(i+1, candidates, target, comb)


print(Solution().combinationSum(
    candidates=[i for i in range(2, 32)], target=40))
