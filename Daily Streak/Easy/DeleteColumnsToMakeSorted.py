# https://leetcode.com/problems/delete-columns-to-make-sorted/description/?envType=daily-question&envId=2025-12-20

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletedColumnsCount = 0
        for i in range(len(strs[0])):
            j = 1
            isColumnSorted = True
            while j < len(strs) and isColumnSorted:
                if strs[j][i] < strs[j-1][i]:
                    deletedColumnsCount += 1
                    isColumnSorted = False
                j = j + 1
        return deletedColumnsCount


print(Solution().minDeletionSize(strs=["cba", "daf", "ghi"]))
print(Solution().minDeletionSize(strs=["a", "b"]))
print(Solution().minDeletionSize(strs=["zyx", "wvu", "tsr"]))
