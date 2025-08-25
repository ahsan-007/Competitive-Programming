# https://leetcode.com/problems/diagonal-traverse/description/?envType=daily-question&envId=2025-08-25

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        r = 0
        c = 0
        order = []
        isDown = False
        while r != m and c != n:

            i = r
            j = c

            while i < m and j >= 0:
                if isDown:
                    order.append(mat[i][j])
                i = i + 1
                j = j - 1

            if not isDown:

                i = i - 1
                j = j + 1

                while i >= 0 and j < n:
                    order.append(mat[i][j])
                    i = i - 1
                    j = j + 1

            isDown = not isDown

            if c != n - 1:
                c = c + 1
            else:
                r = r + 1

        return order


print(Solution().findDiagonalOrder(
    mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

print(Solution().findDiagonalOrder(
    mat=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

print(Solution().findDiagonalOrder(
    mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
