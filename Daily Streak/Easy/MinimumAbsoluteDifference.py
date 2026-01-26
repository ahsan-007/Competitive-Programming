# https://leetcode.com/problems/minimum-absolute-difference/description/?envType=daily-question&envId=2026-01-26

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDifference = float("+inf")
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] < minDifference:
                minDifference = arr[i] - arr[i - 1]

        pairs = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == minDifference:
                pairs.append([arr[i - 1], arr[i]])
        return pairs


print(Solution().minimumAbsDifference(arr=[4, 2, 1, 3]))
print(Solution().minimumAbsDifference(arr=[1, 3, 6, 10, 15]))
print(Solution().minimumAbsDifference(arr=[3, 8, -10, 23, 19, -4, -14, 27]))
