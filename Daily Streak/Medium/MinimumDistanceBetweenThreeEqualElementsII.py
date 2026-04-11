# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/editorial/?envType=daily-question&envId=2026-04-11


from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        minDistance = float("+inf")
        map = {}
        for i, num in enumerate(nums):
            if num not in map:
                map[num] = [i]

            elif len(map[num]) < 3:
                map[num].append(i)

            else:
                map[num][0], map[num][1], map[num][2] = map[num][1], map[num][2], i

            if len(map[num]) == 3:
                minDistance = min(minDistance,
                                  abs(map[num][0] - map[num][1]) + abs(map[num][1] - map[num][2]) + abs(map[num][2] - map[num][0]))

        return minDistance if minDistance != float("+inf") else -1


print(Solution().minimumDistance(nums=[1, 2, 1, 1, 3]))
print(Solution().minimumDistance(nums=[1, 1, 2, 3, 2, 1, 2]))
