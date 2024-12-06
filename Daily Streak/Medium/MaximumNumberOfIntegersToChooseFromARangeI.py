# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description /?envType=daily-question&envId=2024-12-06

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        currSum = 0
        count = 0
        for i in range(1, n+1):
            # could use binary search too for lookup in banned list
            if i not in banned:
                if currSum + i <= maxSum:
                    count = count + 1
                    currSum = currSum + i
                else:
                    return count

        return count


print(Solution().maxCount(banned=[1, 6, 5], n=5, maxSum=6))
print(Solution().maxCount(banned=[1, 2, 3, 4, 5, 6, 7], n=8, maxSum=1))
print(Solution().maxCount(banned=[11], n=7, maxSum=50))
