# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/?envType=daily-question&envId=2026-03-22

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotateRight(matrix: List[List[int]]) -> List[List[int]]:
            rotated_matrix = [[0] * len(matrix) for _ in range(len(matrix))]
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    rotated_matrix[j][len(matrix) - (i + 1)] = matrix[i][j]
            return rotated_matrix

        def isEqual(mat1, mat2):
            if len(mat1) != len(mat2) or (len(mat1) != 0 and len(mat2) != 0 and len(mat1[0]) != len(mat2[0])):
                return False
            for i in range(len(mat1)):
                for j in range(len(mat1[i])):
                    if mat1[i][j] != mat2[i][j]:
                        return False
            return True

        for i in range(4):
            if isEqual(mat, target):
                return True
            mat = rotateRight(mat)
        return False


print(Solution().findRotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]]))
print(Solution().findRotation(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]]))
print(Solution().findRotation(mat=[[0, 0, 0], [0, 1, 0], [
      1, 1, 1]], target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]]))
