# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i]-arr[i-1] != diff:
                return False
        return True


print(Solution().canMakeArithmeticProgression(arr=[3, 5, 1]))
print(Solution().canMakeArithmeticProgression(arr=[1, 2, 4]))
