# https://leetcode.com/problems/pascals-triangle/?envType=daily-question&envId=2023-09-08

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            row = []
            for j in range(i+1):
                row.append((rows[i-1][j-1] if j-1 >= 0 else 0) +
                           (rows[i-1][j] if j != i else 0))
            rows.append(row)
        return rows


print(Solution().generate(5))
print(Solution().generate(1))
