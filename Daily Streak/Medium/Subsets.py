# https://leetcode.com/problems/subsets/description /?envType=daily-question&envId=2024-05-21

from typing import List
import math


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        exp = int(math.pow(2, len(nums)))
        subsets = []
        for i in range(exp):
            subset = []
            binary = bin(i)[2:][::-1]
            j = 0
            while j < len(binary):
                if binary[j] == '1':
                    subset.append(nums[j])
                j = j + 1
            subsets.append(subset)
        return subsets


print(Solution().subsets(nums=[1, 2, 3]))
print(Solution().subsets(nums=[1]))
print(Solution().subsets(nums=[1, 2, 3, 4]))
