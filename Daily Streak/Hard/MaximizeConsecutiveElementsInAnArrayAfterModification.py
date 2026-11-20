# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/description/?envType=daily-question&envId=2026-11-20

from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        memo = {}
        maxElements = 0
        for num in nums:
            memo[num + 1] = max(memo.get(num+1, 0), memo.get(num, 0) + 1)
            memo[num] = max(memo.get(num, 0), memo.get(num-1, 0) + 1)
            maxElements = max(maxElements, memo[num], memo[num + 1])
        return maxElements


print(Solution().maxSelectedElements(nums=[2, 1, 5, 1, 1]))
print(Solution().maxSelectedElements(nums=[1, 4, 7, 10]))
print(Solution().maxSelectedElements(
    nums=[8, 10, 6, 12, 9, 12, 2, 3, 13, 19, 11, 18, 10, 16]))
