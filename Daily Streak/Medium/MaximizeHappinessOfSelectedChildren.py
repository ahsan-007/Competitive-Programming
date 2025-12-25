# https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2025-12-25

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        i = 0
        happinessSum = 0
        while i < len(happiness) and i < k and happiness[i] - i > 0:
            happinessSum += happiness[i] - i
            i = i + 1
        return happinessSum

print(Solution().maximumHappinessSum(happiness=[1, 2, 3], k=2))
print(Solution().maximumHappinessSum(happiness=[1, 1, 1, 1], k=2))
print(Solution().maximumHappinessSum(happiness=[2, 3, 4, 5], k=1))
