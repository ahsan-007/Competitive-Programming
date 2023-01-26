# https://leetcode.com/problems/reducing-dishes/

from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        return self.maxSatisfactionUtilDP(satisfaction, 0, 1, {})

    def maxSatisfactionUtil(self, satisfaction, ind, time, sum):
        if ind == len(satisfaction):
            return sum

        return max(self.maxSatisfactionUtil(satisfaction, ind + 1, time + 1, sum + satisfaction[ind] * time),
                   self.maxSatisfactionUtil(satisfaction, ind + 1, time, sum))

    def maxSatisfactionUtilDP(self, satisfaction, i, time, memo):
        if i == len(satisfaction):
            return 0

        if (i, time) not in memo:
            memo[(i, time)] = max(time * satisfaction[i] + self.maxSatisfactionUtilDP(satisfaction, i + 1, time + 1, memo),
                                  self.maxSatisfactionUtilDP(satisfaction, i + 1, time, memo))
        return memo[(i, time)]


print(Solution().maxSatisfaction([-1, -8, 0, 5, -7]))
print(Solution().maxSatisfaction([4, 3, 2]))
print(Solution().maxSatisfaction([-1, -4, -5]))
