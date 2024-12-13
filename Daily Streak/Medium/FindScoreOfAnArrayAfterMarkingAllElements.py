# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description /?envType=daily-question&envId=2024-12-13

from typing import List
import heapq


class Solution:
    def findScore(self, nums: List[int]) -> int:
        mapping = {}
        for i, num in enumerate(nums):
            if num not in mapping:
                mapping[num] = []
            mapping[num].append(i)

        heap = [num for num in nums]
        heapq.heapify(heap)
        score = 0
        while heap:
            minEle = heapq.heappop(heap)
            while mapping[minEle] and nums[mapping[minEle][0]] is None:
                mapping[minEle].pop(0)

            if mapping[minEle]:
                score = score + minEle
                nums[mapping[minEle][0]] = None
                if mapping[minEle][0] - 1 >= 0:
                    nums[mapping[minEle][0] - 1] = None
                if mapping[minEle][0] + 1 < len(nums):
                    nums[mapping[minEle][0] + 1] = None
        return score

    def findScoreV2(self, nums: List[int]) -> int:
        marked = [False] * len(nums)
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        score = 0
        while heap:
            minEle, ind = heapq.heappop(heap)
            if not marked[ind]:
                score = score + minEle
                marked[ind] = True
                if ind - 1 >= 0:
                    marked[ind-1] = True
                if ind + 1 < len(marked):
                    marked[ind+1] = True
        return score


print(Solution().findScore(nums=[2, 1, 3, 4, 5, 2]))
print(Solution().findScore(nums=[2, 3, 5, 1, 3, 2]))
print(Solution().findScore(nums=[
      10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]))

print()

print(Solution().findScoreV2(nums=[2, 1, 3, 4, 5, 2]))
print(Solution().findScoreV2(nums=[2, 3, 5, 1, 3, 2]))
print(Solution().findScoreV2(nums=[
      10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]))
