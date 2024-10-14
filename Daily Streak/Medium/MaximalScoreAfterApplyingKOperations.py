# https://leetcode.com/problems/maximal-score-after-applying-k-operations/description /?envType=daily-question&envId=2024-10-14

from typing import List
import math
import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        elements = []

        for ele in nums:
            heapq.heappush(elements, -ele)

        score = 0
        for i in range(k):
            maxEle = abs(heapq.heappop(elements))

            score = score + maxEle
            heapq.heappush(elements, -math.ceil(maxEle / 3))

        return score


print(Solution().maxKelements(nums=[10, 10, 10, 10, 10], k=5))
print(Solution().maxKelements(nums=[1, 10, 3, 3, 3], k=3))


heap_test = []
