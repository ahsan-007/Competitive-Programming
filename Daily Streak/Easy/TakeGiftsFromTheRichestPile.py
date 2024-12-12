# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description /?envType=daily-question&envId=2024-12-12

from typing import List
import math
import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        def findMax(gifts):
            maxEle = float("-inf")
            maxEleInd = -1
            for i, ele in enumerate(gifts):
                maxEle = max(ele, maxEle)
                if maxEle == ele:
                    maxEleInd = i
            return maxEleInd

        for i in range(k):
            maxEleInd = findMax(gifts)
            gifts[maxEleInd] = math.floor(math.sqrt(gifts[maxEleInd]))
        return sum(gifts)

    def pickGiftsV2(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for i in range(k):
            maxEle = heapq.heappop(gifts)
            heapq.heappush(gifts, -math.floor(math.sqrt(abs(maxEle))))

        return abs(sum(gifts))


print(Solution().pickGifts(gifts=[25, 64, 9, 4, 100], k=4))
print(Solution().pickGifts(gifts=[1, 1, 1, 1], k=4))

print(Solution().pickGiftsV2(gifts=[25, 64, 9, 4, 100], k=4))
print(Solution().pickGiftsV2(gifts=[1, 1, 1, 1], k=4))
