# https://leetcode.com/problems/solving-questions-with-brainpower/

from typing import List


class Solution:
    # Top Down with Memoization
    def mostPoints(self, questions: List[List[int]]) -> int:
        return self.mostPointsUtil(questions, 0, {})

    def mostPointsUtil(self, questions, i, memo):
        if i >= len(questions):
            return 0
        if i in memo:
            return memo[i]
        memo[i] = max(questions[i][0] +
                      self.mostPointsUtil(
                          questions, i+1+questions[i][1], memo),
                      self.mostPointsUtil(questions, i+1, memo))
        return memo[i]

    # Bottom Up
    def mostPointsV2(self, questions: List[List[int]]) -> int:
        dp = [0 for i in range(len(questions))]
        for i in range(len(questions)-1, -1, -1):
            dp[i] = max(questions[i][0] + (dp[i+1 + questions[i][1]] if i+1 + questions[i]
                        [1] < len(dp) else 0),
                        dp[i+1] if i+1 < len(dp) else 0)
        return dp[0]


print(Solution().mostPoints(questions=[[3, 2], [4, 3], [4, 4], [2, 5]]))
print(Solution().mostPoints(
    questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))

print(Solution().mostPointsV2(questions=[[3, 2], [4, 3], [4, 4], [2, 5]]))
print(Solution().mostPointsV2(
    questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
