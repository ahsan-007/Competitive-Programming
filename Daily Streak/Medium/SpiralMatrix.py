# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix and matrix[0]:
            return self.spiralOrderUtil(matrix, 0, 0, len(matrix), len(matrix[0]))
        return []

    def spiralOrderUtil(self, matrix, r, c, m, n):
        if n <= 0 or m <= 0 or r >= m or c >= n:
            return []
        if r == m and c == n:
            return [matrix[r][c]]
        spiral = []
        i = r
        j = c
        while j < n:
            spiral.append(matrix[i][j])
            j = j + 1
        j = j - 1

        i = i + 1
        while i < m:
            spiral.append(matrix[i][j])
            i = i + 1
        i = i - 1

        if i != r and j != c:
            j = j - 1
            while j >= c:
                spiral.append(matrix[i][j])
                j = j - 1
            j = j + 1

            i = i - 1
            while i > r:
                spiral.append(matrix[i][j])
                i = i - 1
            spiral.extend(self.spiralOrderUtil(matrix, r + 1, c+1, m-1, n-1))
        return spiral


print(Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder(
    matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(Solution().spiralOrder(
    matrix=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))

print(Solution().spiralOrder(
    matrix=[[1, 2, 3, 4, 13], [5, 6, 7, 8, 14], [9, 10, 11, 12, 15]]))
print(Solution().spiralOrder(matrix=[[7], [9], [6]]))
print(Solution().spiralOrder(matrix=[[2, 4, 6]]))
print(Solution().spiralOrder(matrix=[[1, 2], [3, 4]]))
