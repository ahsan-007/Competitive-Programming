# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/?envType=daily-question&envId=2025-05-03

from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        topsSwaps = [0, 0]
        bottomsSwaps = [0, 0]
        for i in range(len(tops)):
            if topsSwaps and tops[0] != tops[i]:
                if tops[0] == bottoms[i]:
                    topsSwaps[0] += 1
                else:
                    topsSwaps = None

            if topsSwaps and tops[0] != bottoms[i]:
                if tops[0] == tops[i]:
                    topsSwaps[1] += 1
                else:
                    topsSwaps = None

            if bottomsSwaps and bottoms[0] != tops[i]:
                if bottoms[0] == bottoms[i]:
                    bottomsSwaps[0] += 1
                else:
                    bottomsSwaps = None

            if bottomsSwaps and bottoms[0] != bottoms[i]:
                if bottoms[0] == tops[i]:
                    bottomsSwaps[1] += 1
                else:
                    bottomsSwaps = None

        if not topsSwaps and not bottomsSwaps:
            return -1

        return min(min(topsSwaps) if topsSwaps else float("+inf"), min(bottomsSwaps) if bottomsSwaps else float("+inf"))


print(Solution().minDominoRotations(
    tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2]))
print(Solution().minDominoRotations(
    tops=[3, 5, 1, 2, 3], bottoms=[3, 6, 3, 3, 4]))
print(Solution().minDominoRotations(
    tops=[1, 2, 1, 1, 1, 2, 2, 2], bottoms=[2, 1, 2, 2, 2, 2, 2, 2]))
