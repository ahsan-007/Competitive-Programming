# https://leetcode.com/problems/merge-similar-items/

from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items = {}
        for item in items1:
            items[item[0]] = items.get(item[0], 0) + item[1]
        for item in items2:
            items[item[0]] = items.get(item[0], 0) + item[1]

        weights = list(items.keys())
        weights.sort()
        return [[weight, items[weight]] for weight in weights]


print(Solution().mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]))
print(Solution().mergeSimilarItems([[1,3],[2,2]], [[7,1],[2,2],[1,4]]))
