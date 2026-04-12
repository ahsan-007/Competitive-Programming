# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/description/?envType=daily-question&envId=2026-04-12

from typing import List


class Solution:
    def minimumDistance(self, word: str) -> int:
        memo = {}

        def minimumDistanceUtil(finger1, finger2, i):
            def get_distance(a, b):
                return (abs(a[0]-b[0]) + abs(a[1]-b[1])) if a is not None and b is not None else 0

            if i >= len(word):
                return 0

            if (finger1, finger2, i) not in memo:
                ascii = ord(word[i]) - ord('A')
                pos = (ascii//6, ascii % 6)

                memo[(finger1, finger2, i)] = min(
                    minimumDistanceUtil(pos, finger2, i + 1) +
                    get_distance(finger1, pos),
                    minimumDistanceUtil(finger1, pos, i + 1) +
                    get_distance(finger2, pos)
                )

            return memo[(finger1, finger2, i)]

        return minimumDistanceUtil(None, None, 0)


print(Solution().minimumDistance(word="CAKE"))
print(Solution().minimumDistance(word="HAPPY"))
