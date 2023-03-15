# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import List
from copy import deepcopy


class Solution:
    # O (N lgN)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_copy = deepcopy(nums)
        nums_copy.sort()
        map = {}
        for i in range(len(nums_copy)):
            if nums_copy[i] not in map:
                map[nums_copy[i]] = i
                
        return [map[num] for num in nums]
    
    # O(N)
    def smallerNumbersThanCurrentV2(self, nums: List[int]) -> List[int]:
        commulative_frequency = [0 for i in range(102)]
        for num in nums:
            commulative_frequency[num + 1] += 1
        
        for i in range(1, 102):
            commulative_frequency[i] = commulative_frequency[i] + commulative_frequency[i - 1]
        
        return [commulative_frequency[num] for num in nums]


print(Solution().smallerNumbersThanCurrent([6, 5, 4, 8]))
print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))


print(Solution().smallerNumbersThanCurrentV2([6, 5, 4, 8]))
print(Solution().smallerNumbersThanCurrentV2([8, 1, 2, 2, 3]))
