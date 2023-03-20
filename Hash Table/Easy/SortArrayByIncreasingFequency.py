# https://leetcode.com/problems/sort-array-by-increasing-frequency/

from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        numbers = {}
        for key in frequency:
            if frequency[key] not in numbers:
                numbers[frequency[key]] = []
            numbers[frequency[key]].extend([key] * frequency[key])

        keys = list(numbers.keys())
        keys.sort()
        sorted_list = []
        for key in keys:
            numbers[key].sort(reverse=True)
            sorted_list.extend(numbers[key])
        return sorted_list


# print(Solution().frequencySort(nums=[1, 1, 2, 2, 2, 3]))
# print(Solution().frequencySort(nums=[2, 3, 1, 3, 2]))
# print(Solution().frequencySort(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1]))
nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
print(sorted(sorted(nums, reverse=True), key=nums.count))
