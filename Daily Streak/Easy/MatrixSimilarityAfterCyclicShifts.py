# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description/?envType=daily-question&envId=2026-03-27

from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        modified_matrix = []
        k = k % len(mat[0])
        for i in range(len(mat)):
            if i % 2 == 0:
                modified_matrix.append(mat[i][k:] + mat[i][:k])
            else:
                modified_matrix.append(
                    mat[i][-k:] + mat[i][:(len(mat[i]) - k)])

            for j in range(len(mat[i])):
                if mat[i][j] != modified_matrix[i][j]:
                    return False
        return True


# print(Solution().areSimilar(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=4))
# print(Solution().areSimilar(
#     mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2))
# print(Solution().areSimilar(mat=[[2, 2], [2, 2]], k=3))
# print(Solution().areSimilar(mat=[[1, 2]], k=1))
# print(Solution().areSimilar(mat=[[7, 7], [10, 10], [4, 4]], k=2))
print(Solution().areSimilar(
    mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2))
