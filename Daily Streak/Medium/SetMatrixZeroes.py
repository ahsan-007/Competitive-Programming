# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=daily-question&envId=2025-05-21

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            j = 0
            while j < len(matrix[i]):
                if matrix[i][j] == 0:
                    if matrix[0][j] != "RC":
                        matrix[0][j] = 'RC' if (
                            i == 0 and j == 0) or matrix[0][j] == 'R' else 'C'

                    if matrix[i][0] != "RC":
                        matrix[i][0] = 'RC' if (
                            i == 0 and j == 0) or matrix[i][0] == 'C' else 'R'
                j = j + 1

        for i in range(len(matrix)):
            if matrix[i][0] in ('R', 'RC'):
                j = 1
                while j < len(matrix[i]):
                    if matrix[i][j] not in ('R', 'C', 'RC'):
                        matrix[i][j] = 0
                    j = j + 1

        for j in range(len(matrix[i])):
            if matrix[0][j] in ('C', 'RC'):
                i = 1
                while i < len(matrix):
                    if matrix[i][j] not in ('R', 'C', 'RC'):
                        matrix[i][j] = 0
                    i = i + 1

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] in ('R', 'C', 'RC'):
                    matrix[i][j] = 0

    def setZeroesV2(self, matrix: List[List[int]]) -> None:
        isFirstColZero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0 and not isFirstColZero:
                isFirstColZero = True

            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[i])-1, 0, -1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

            if isFirstColZero:
                matrix[i][0] = 0


def dislayMatrix(matrix):
    for row in matrix:
        print(row)
    print()


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
dislayMatrix(matrix)
Solution().setZeroes(matrix)
dislayMatrix(matrix)

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
dislayMatrix(matrix)
Solution().setZeroesV2(matrix)
dislayMatrix(matrix)


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
dislayMatrix(matrix)
Solution().setZeroes(matrix)
dislayMatrix(matrix)

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
dislayMatrix(matrix)
Solution().setZeroesV2(matrix)
dislayMatrix(matrix)


matrix = [[0, 1]]
dislayMatrix(matrix)
Solution().setZeroes(matrix)
dislayMatrix(matrix)

matrix = [[0, 1]]
dislayMatrix(matrix)
Solution().setZeroesV2(matrix)
dislayMatrix(matrix)


matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
dislayMatrix(matrix)
Solution().setZeroes(matrix)
dislayMatrix(matrix)

matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
dislayMatrix(matrix)
Solution().setZeroesV2(matrix)
dislayMatrix(matrix)


matrix = [[8, 3, 6, 9, 7, 8, 0, 6], [0, 3, 7, 0, 0, 4, 3, 8], [
    5, 3, 6, 7, 1, 6, 2, 6], [8, 7, 2, 5, 0, 6, 4, 0], [0, 2, 9, 9, 3, 9, 7, 3]]
dislayMatrix(matrix)
Solution().setZeroes(matrix)
dislayMatrix(matrix)

matrix = [[8, 3, 6, 9, 7, 8, 0, 6], [0, 3, 7, 0, 0, 4, 3, 8], [
    5, 3, 6, 7, 1, 6, 2, 6], [8, 7, 2, 5, 0, 6, 4, 0], [0, 2, 9, 9, 3, 9, 7, 3]]
dislayMatrix(matrix)
Solution().setZeroesV2(matrix)
dislayMatrix(matrix)
