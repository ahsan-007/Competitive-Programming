# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description /?envType=daily-question&envId=2024-07-19

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        luckyNums = []
        for i in range(len(matrix)):
            min_ind = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] < matrix[i][min_ind]:
                    min_ind = j

            max_ind = 0
            for k in range(len(matrix)):
                if matrix[k][min_ind] > matrix[max_ind][min_ind]:
                    max_ind = k

            if max_ind == i:
                luckyNums.append(matrix[max_ind][min_ind])
        return luckyNums


print(Solution().luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(Solution().luckyNumbers(
    matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(Solution().luckyNumbers(matrix=[[7, 8], [1, 2]]))
