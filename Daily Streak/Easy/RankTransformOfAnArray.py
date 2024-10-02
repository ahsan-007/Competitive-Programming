# https://leetcode.com/problems/rank-transform-of-an-array/description /?envType=daily-question&envId=2024-10-02

from typing import List
import copy


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arrCopy = copy.deepcopy(arr)
        arrCopy.sort()
        ranks = {}
        current_rank = 1
        for ele in arrCopy:
            if ele not in ranks:
                ranks[ele] = current_rank
                current_rank = current_rank + 1

        return [ranks[ele] for ele in arr]


print(Solution().arrayRankTransform(arr=[40, 10, 20, 30]))
print(Solution().arrayRankTransform(arr=[100, 100, 100]))
print(Solution().arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]))
