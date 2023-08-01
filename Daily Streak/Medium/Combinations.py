# https://leetcode.com/problems/combinations/

from typing import List
from copy import deepcopy


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        self.combineUtil(n, k, 1, [], combinations)
        return combinations

    def combineUtil(self, n, k, i, running_combination, combinations):
        if len(running_combination) == k:
            combinations.append(running_combination)
            return
        if i > n:
            return
        for j in range(i, n+1):
            running_combination.append(j)
            self.combineUtil(
                n, k, j+1, deepcopy(running_combination), combinations)
            running_combination.pop()


print(Solution().combine(n=4, k=2))
