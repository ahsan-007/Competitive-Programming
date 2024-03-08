# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2024-03-08

from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        max_frequency = float("-inf")
        max_frequency_sum = 0

        for freq in frequency.values():
            if freq == max_frequency:
                max_frequency_sum += freq
            elif freq > max_frequency:
                max_frequency = freq
                max_frequency_sum = freq

        return max_frequency_sum


print(Solution().maxFrequencyElements(nums=[1, 2, 2, 3, 1, 4]))
print(Solution().maxFrequencyElements(nums=[1, 2, 3, 4, 5]))
