# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = self.getSubsets(nums)
        subsets_xor = []
        for subset in subsets:
            subsets_xor.append(self.calculateXOR(subset))
        return sum(subsets_xor)

    def getSubsets(self, nums):
        subsets = []
        lim = pow(2, len(nums))
        for i in range(1, lim):
            binary = str(bin(i))[2:][::-1]
            subset = []
            for ind, ch in enumerate(binary):
                if ch == '1':
                    subset.append(nums[ind])
            subsets.append(subset)
        return subsets

    def calculateXOR(self, arr):
        xor = arr[0]
        for ele in arr[1:]:
            xor = xor ^ ele
        return xor


print(Solution().subsetXORSum([1, 3]))
print(Solution().subsetXORSum([5, 1, 6]))
print(Solution().subsetXORSum([3, 4, 5, 6, 7, 8]))
