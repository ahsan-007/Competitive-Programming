# https://leetcode.com/problems/minimum-falling-path-sum/

from typing import List

# Constraints
# * n == matrix.length == matrix[i].length
# * 1 <= n <= 100
# * -100 <= matrix[i][j] <= 100
# There are 100 levels as 1 <= n <= 100 and each element ranges from -100 to 100
# if at every level max element is found sum reaches 10000, it can never be 100000 that is why MAX_VALUE is set to 100000

MAX_VALUE = 100000


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_sum = MAX_VALUE
        memo = {}
        for j in range(len(matrix)):
            min_sum = min(
                min_sum, self.minFallingPathSumUtil(0, j, matrix, memo))
        print(memo)
        return min_sum

    def minFallingPathSumUtil(self, i, j, matrix, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= len(matrix) or j < 0 or j >= len(matrix):
            return MAX_VALUE

        if i == len(matrix) - 1:
            memo[(i, j)] = matrix[i][j]
            return memo[(i, j)]

        left_sum = self.minFallingPathSumUtil(i + 1, j - 1, matrix, memo)
        below_sum = self.minFallingPathSumUtil(i + 1, j, matrix, memo)
        right_sum = self.minFallingPathSumUtil(i + 1, j + 1, matrix, memo)
        memo[(i, j)] = matrix[i][j] + min(left_sum, below_sum, right_sum)

        return memo[(i, j)]


print(Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(Solution().minFallingPathSum([[-19, 57], [-40, -5]]))
