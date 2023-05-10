# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for j in range(n)] for i in range(n)]
        self.generateMatrixUtil(mat, 0, 0, 1, n)
        return mat

    def generateMatrixUtil(self, mat, r, c, base, n):
        if r >= n or c >= n:
            return

        i = j = r

        while j < n:
            mat[i][j] = base
            base = base + 1
            j = j + 1
        j = j - 1

        i = i + 1
        while i < n:
            mat[i][j] = base
            base = base + 1
            i = i + 1
        i = i - 1

        j = j - 1
        while j >= c:
            mat[i][j] = base
            base = base + 1
            j = j - 1
        j = j + 1

        i = i - 1
        while i > r:
            mat[i][j] = base
            base = base + 1
            i = i - 1

        self.generateMatrixUtil(mat, r+1, c+1, base, n - 1)


def display(mat):
    for row in mat:
        print(row)


display(Solution().generateMatrix(3))
print('-'*10)
display(Solution().generateMatrix(4))
print('-'*10)
display(Solution().generateMatrix(2))
print('-'*10)
display(Solution().generateMatrix(8))
