# https://leetcode.com/problems/sum-of-distances/description/?envType=daily-question&envId=2026-04-23

from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        elements = {}
        for i in range(len(nums)):
            elements.setdefault(nums[i], []).append(i)

        arr = [0] * len(nums)
        for indices in elements.values():
            total_sum = sum(indices)
            prefix_total = 0
            sz = len(indices)
            for i, ind in enumerate(indices):
                arr[ind] = total_sum - prefix_total * 2 + ind * (2*i-sz)
                prefix_total += ind
        return arr


print(Solution().distance(nums=[1, 3, 1, 1, 2]))
print(Solution().distance(nums=[0, 5, 3]))
