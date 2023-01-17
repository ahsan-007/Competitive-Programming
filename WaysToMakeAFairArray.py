# https://leetcode.com/problems/ways-to-make-a-fair-array/

from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_sum = 0
        odd_sum = 0
        for i in range(1, len(nums)):
            if (i-1) % 2 == 0:
                even_sum = even_sum + nums[i]
            else:
                odd_sum = odd_sum + nums[i]
        
        fair_ways = 1 if odd_sum == even_sum else 0
        
        for i in range(1, len(nums)):
            if (i-1) % 2 == 0:
                even_sum = even_sum - nums[i]
                even_sum = even_sum + nums[i-1]
            else:
                odd_sum = odd_sum - nums[i]
                odd_sum = odd_sum + nums[i-1]
            
            if even_sum == odd_sum:
                fair_ways = fair_ways + 1
        return fair_ways
        


print(Solution().waysToMakeFair([2, 1, 6, 4]))
