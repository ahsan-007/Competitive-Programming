# https://leetcode.com/problems/relative-sort-array/description /?envType=daily-question&envId=2024-06-11

from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        sortedArray = []
        for ele in arr2:
            sortedArray.extend([ele] * freq[ele])
            freq[ele] = 0

        elements_not_found = []
        for ele in freq:
            if freq[ele] != 0:
                elements_not_found.extend([ele] * freq[ele])
        elements_not_found.sort()
        sortedArray.extend(elements_not_found)

        return sortedArray


print(Solution().relativeSortArray(
    arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))

print(Solution().relativeSortArray(
    arr1=[28, 6, 22, 8, 44, 17], arr2=[22, 28, 8, 6]))


# nput:
# Output: [22, 28, 8, 6, 17, 44]
