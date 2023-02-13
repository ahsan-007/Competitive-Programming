# https://leetcode.com/problems/number-of-good-pairs/

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = {}
        good_pairs = 0
        for num in nums:
            if num in frequency:
                good_pairs = good_pairs + frequency[num]
                frequency[num] = frequency[num] + 1
            else:
                frequency[num] = 1
        return good_pairs


print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
