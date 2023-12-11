# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/?envType=daily-question&envId=2023-12-11

from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        currDig = -1
        count = 0
        for i in range(len(arr)):
            if currDig != arr[i]:
                currDig = arr[i]
                count = 0
            count = count + 1
            if count > len(arr) // 4:
                return currDig

    def findSpecialIntegerV2(self, arr: List[int]) -> int:
        size = len(arr) // 4
        for i in range(len(arr) - size):
            if arr[i + size] == arr[i]:
                return arr[i]


print(Solution().findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(Solution().findSpecialIntegerV2(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))
