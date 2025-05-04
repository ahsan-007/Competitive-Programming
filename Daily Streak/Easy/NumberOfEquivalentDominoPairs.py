# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-04


from typing import List
from collections import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = {}
        dominiPairs = 0
        for domino in dominoes:
            dominoTup = tuple(
                domino) if domino[0] <= domino[1] else tuple(domino[::-1])

            if dominoTup in freq:
                dominiPairs = dominiPairs + freq[dominoTup]
                freq[dominoTup] += 1
            else:
                freq[dominoTup] = 1

        return dominiPairs

    # one liner
    def numEquivDominoPairsV2(self, dominoes: List[List[int]]) -> int:
        return sum(pairFrequency*(pairFrequency-1)//2 for pairFrequency in Counter(tuple(sorted(domino)) for domino in dominoes).values())


print(Solution().numEquivDominoPairs(
    dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]))
print(Solution().numEquivDominoPairs(
    dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))

print(Solution().numEquivDominoPairsV2(
    dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]))
print(Solution().numEquivDominoPairsV2(
    dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
