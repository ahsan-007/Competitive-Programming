# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/?envType=daily-question&envId=2026-01-25

from typing import List


class Solution:
    # Time: O(N*LogN)
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minScore = float("+inf")
        for i in range(len(nums) - k + 1):
            minScore = min(minScore, nums[i + k - 1] - nums[i])
        return minScore


print(Solution().minimumDifference(nums=[90], k=1))
print(Solution().minimumDifference(nums=[9, 4, 1, 7], k=2))
print(Solution().minimumDifference(nums=[24382, 79784, 9930, 63713, 49507, 92917, 12295, 28077, 63938,
                                         95126, 84621, 83487, 18427, 51410, 16931, 23715, 41651, 6453,
                                         72354, 49213, 9206, 92533, 86113, 16984, 51934, 94327, 53001,
                                         78738, 47965, 81659, 1875, 5012, 58236, 92701, 39258, 64897,
                                         39590, 29032, 62291, 22592, 55378, 70484, 79633, 44398, 16952,
                                         18830, 14973, 21740, 57003, 62307, 7790, 49153, 6713, 92891,
                                         82533, 28810, 13120, 95521, 40515, 70824, 89748, 44804, 72171,
                                         45064, 82620, 14253, 2585, 17842, 2606, 2775, 36079, 87227, 44868,
                                         64448, 34594, 36214],
                                   k=72))
