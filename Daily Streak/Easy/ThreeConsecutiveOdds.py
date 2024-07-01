# https://leetcode.com/problems/three-consecutive-odds/description /?envType=daily-question&envId=2024-07-01

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False

    def threeConsecutiveOddsV2(self, arr: List[int]) -> bool:
        consecutiveOdds = 0
        for i in range(len(arr)):
            consecutiveOdds = (consecutiveOdds + 1) if arr[i] % 2 == 1 else 0

            if consecutiveOdds == 3:
                return True

        return False


print(Solution().threeConsecutiveOdds(arr=[2, 6, 4, 1]))
print(Solution().threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]))


print(Solution().threeConsecutiveOddsV2(arr=[2, 6, 4, 1]))
print(Solution().threeConsecutiveOddsV2(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]))
