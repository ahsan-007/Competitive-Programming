# https://leetcode.com/problems/maximum-matrix-sum/description/?envType=daily-question&envId=2026-01-05

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minEle = float("+inf")
        negativeCount = 0
        maxSum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] < 0:
                    negativeCount += 1
                maxSum += abs(matrix[i][j])
                minEle = min(minEle, abs(matrix[i][j]))

        if negativeCount % 2 == 0:
            return maxSum

        return maxSum - 2 * minEle


print(Solution().maxMatrixSum(matrix=[[1, -1], [-1, 1]]))
print(Solution().maxMatrixSum(matrix=[[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))
print(Solution().maxMatrixSum(matrix=[[-1, 0, -1], [-2, 1, 3], [3, 2, 2]]))
