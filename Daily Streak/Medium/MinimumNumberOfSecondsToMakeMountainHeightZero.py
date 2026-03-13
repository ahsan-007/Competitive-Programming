# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/?envType=daily-question&envId=2026-03-13

from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        maxTime = max(workerTimes)
        lb = 1
        ub = maxTime * mountainHeight * (mountainHeight + 1) // 2
        ans = 0
        eps = 1e-7

        while lb <= ub:
            mid = (lb + ub) // 2
            count = 0
            for time in workerTimes:
                work = mid // time
                count += int((-1 + ((1 + work * 8) ** 0.5)) / 2 + eps)

            if count >= mountainHeight:
                ans = mid
                ub = mid - 1
            else:
                lb = mid + 1
        return ans


print(Solution().minNumberOfSeconds(mountainHeight=4, workerTimes=[2, 1, 1]))
print(Solution().minNumberOfSeconds(
    mountainHeight=10, workerTimes=[3, 2, 2, 4]))
print(Solution().minNumberOfSeconds(
    mountainHeight=5, workerTimes=[1]))
print(Solution().minNumberOfSeconds(
    mountainHeight=5, workerTimes=[1, 5]))
