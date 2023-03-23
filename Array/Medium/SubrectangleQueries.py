# https://leetcode.com/problems/subrectangle-queries/

from typing import List
from copy import deepcopy


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = deepcopy(rectangle)

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col] if row > 0 and col >= 0 and row < len(self.rectangle) and col < len(self.rectangle[row]) else None


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

obj = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
print(obj.getValue(0, 2))
obj.updateSubrectangle(0, 0, 3, 2, 5)
print(obj.getValue(0, 2))
print(obj.getValue(3, 1))
obj.updateSubrectangle(3, 0, 3, 2, 10)
print(obj.getValue(3, 1))
print(obj.getValue(0, 2))


obj = SubrectangleQueries([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(obj.getValue(0, 0))
obj.updateSubrectangle(0, 0, 2, 2, 100)
print(obj.getValue(0, 0))
print(obj.getValue(2, 2))
obj.updateSubrectangle(1, 1, 2, 2, 20)
print(obj.getValue(2, 2))
