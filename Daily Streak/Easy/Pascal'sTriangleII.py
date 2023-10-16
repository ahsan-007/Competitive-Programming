# https://leetcode.com/problems/pascals-triangle-ii/?envType=daily-question&envId=2023-10-16

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr_row = [1]
        for i in range(1, rowIndex + 1):
            next_row = []
            for j in range(i+1):
                next_row.append((curr_row[j-1] if j > 0 else 0) +
                                (curr_row[j] if j < len(curr_row) else 0))
            curr_row = next_row
        return curr_row


print(Solution().getRow(rowIndex=3))
print(Solution().getRow(rowIndex=0))
print(Solution().getRow(rowIndex=1))
print(Solution().getRow(rowIndex=33))
