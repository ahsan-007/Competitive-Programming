# https://leetcode.com/problems/richest-customer-wealth/

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for i in range(len(accounts)):
            max_sum = max(max_sum, sum(accounts[i]))
        return max_sum


print(Solution().maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]))
print(Solution().maximumWealth(accounts = [[1,5],[7,3],[3,5]]))
print(Solution().maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]]))
