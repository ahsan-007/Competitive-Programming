# https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/?envType=daily-question&envId=2026-03-04

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowsOnes = [0] * len(mat)
        columnsOnes = [0] * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    rowsOnes[i] += 1
                    columnsOnes[j] += 1

        specialCount = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1 and rowsOnes[i] == 1 and columnsOnes[j] == 1:
                    specialCount += 1
        return specialCount


print(Solution().numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
print(Solution().numSpecial(mat=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
