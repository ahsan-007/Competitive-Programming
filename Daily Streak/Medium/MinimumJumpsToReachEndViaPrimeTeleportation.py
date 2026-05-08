# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/description/?envType=daily-question&envId=2026-05-08

from typing import List
from collections import defaultdict


lim = 1000001
factors = [[] for _ in range(lim)]
for i in range(2, lim):
    if not factors[i]:
        for j in range(i, lim, i):
            factors[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        edges = defaultdict(list)
        for i in range(len(nums)):
            if len(factors[nums[i]]) == 1:
                edges[nums[i]].append(i)

        res = 0
        seen = {-1}
        queue = [len(nums) - 1]
        while True:
            q = []
            for i in queue:
                if i == 0:
                    return res

                if i > 0 and i-1 not in seen:
                    seen.add(i-1)
                    q.append(i-1)

                if i < len(nums) - 1 and i + 1 not in seen:
                    seen.add(i+1)
                    q.append(i+1)

                for p in factors[nums[i]]:
                    for j in edges[p]:
                        if j not in seen:
                            seen.add(j)
                            q.append(j)
                    edges[p] = []
            queue = q
            res += 1


print(Solution().minJumps(nums=[1, 2, 4, 6]))
print(Solution().minJumps(nums=[2, 3, 4, 7, 9]))
print(Solution().minJumps(nums=[4, 6, 5, 8]))
print(Solution().minJumps(nums=[893, 786, 607, 137, 69, 381, 790, 233, 15, 42, 7, 764, 890,
      269, 84, 262, 870, 514, 514, 650, 269, 485, 760, 181, 489, 107, 585, 428, 862, 563]))
