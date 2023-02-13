# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            if num in frequency:
                return num
            else:
                frequency[num] = True
                
                
print(Solution().repeatedNTimes([1,2,3,3]))
print(Solution().repeatedNTimes([2,1,2,5,3,2]))
print(Solution().repeatedNTimes([5,1,5,2,5,3,5,4]))
