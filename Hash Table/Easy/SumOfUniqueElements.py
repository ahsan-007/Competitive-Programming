# https://leetcode.com/problems/sum-of-unique-elements/

from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        frequency = {}
        for ele in nums:
            frequency[ele] = frequency.get(ele, 0) + 1
        return sum([num for num in frequency if frequency[num] == 1])



print(Solution().sumOfUnique([1,2,3,2]))
print(Solution().sumOfUnique([1,1,1,1,1]))
print(Solution().sumOfUnique([1,2,3,4,5]))
