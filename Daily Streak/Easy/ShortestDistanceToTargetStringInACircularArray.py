# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/?envType=daily-question&envId=2026-04-15

from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        minDistance = float("+inf")
        for i, word in enumerate(words):
            if word == target:
                minDistance = min(
                    minDistance,
                    abs(startIndex - i),

                    (i + (len(words) - startIndex))
                    if i < startIndex else
                    (startIndex + (len(words) - i))
                )
        return minDistance if minDistance != float("+inf") else -1

    def closestTargetV2(self, words: List[str], target: str, startIndex: int) -> int:
        minDistance = float("+inf")
        for i, word in enumerate(words):
            if word == target:
                minDistance = min(
                    minDistance,
                    abs(i-startIndex),
                    len(words) - abs((i-startIndex))
                )
        return minDistance if minDistance != float("+inf") else -1


print(Solution().closestTarget(
    words=["hello", "i", "am", "leetcode", "hello"], target="hello", startIndex=1))
print(Solution().closestTarget(
    words=["a", "b", "leetcode"], target="leetcode", startIndex=0))
print(Solution().closestTarget(
    words=["i", "eat", "leetcode"], target="ate", startIndex=0))

print('-'*100)

print(Solution().closestTargetV2(
    words=["hello", "i", "am", "leetcode", "hello"], target="hello", startIndex=1))
print(Solution().closestTargetV2(
    words=["a", "b", "leetcode"], target="leetcode", startIndex=0))
print(Solution().closestTargetV2(
    words=["i", "eat", "leetcode"], target="ate", startIndex=0))
