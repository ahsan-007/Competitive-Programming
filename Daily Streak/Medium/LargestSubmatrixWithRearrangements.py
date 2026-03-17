# https://leetcode.com/problems/largest-submatrix-with-rearrangements/editorial/?envType=daily-question&envId=2026-03-17

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(matrix)):
            if i > 0:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 1:
                        matrix[i][j] += matrix[i - 1][j]

            row = sorted(matrix[i], reverse=True)
            for k in range(len(row)):
                maxArea = max(maxArea, row[k] * (k + 1))
        return maxArea


print(Solution().largestSubmatrix(matrix=[[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
print(Solution().largestSubmatrix(matrix=[[1, 0, 1, 0, 1]]))
print(Solution().largestSubmatrix(matrix=[[1, 1, 0], [1, 0, 1]]))
