# https://leetcode.com/problems/walking-robot-simulation-ii/description/?envType=daily-question&envId=2026-04-07

from enum import Enum
from typing import List


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @property
    def label(self):
        return self.name.title()


class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [0, 0]
        self.direction = Direction.EAST

    def getCounterClockwiseDirection(self):
        return Direction((self.direction.value + 3) % 4)

    def step(self, num: int) -> None:
        parameter = ((self.width + self.height) * 2) - 4
        if self.pos[0] == 0 and self.pos[1] == 0 and num >= parameter:
            num = num % parameter
            self.direction = Direction.WEST if self.direction == Direction.NORTH else Direction.SOUTH

        if self.direction == Direction.NORTH:
            if self.pos[1] + num < self.height:
                self.pos[1] += num
                num = 0
            else:
                num = num - (self.height - self.pos[1] - 1)
                self.pos[1] = self.height - 1

        elif self.direction == Direction.SOUTH:
            if self.pos[1] - num >= 0:
                self.pos[1] -= num
                num = 0
            else:
                num = num - self.pos[1]
                self.pos[1] = 0

        elif self.direction == Direction.EAST:
            if self.pos[0] + num < self.width:
                self.pos[0] += num
                num = 0
            else:
                num = num - (self.width - self.pos[0] - 1)
                self.pos[0] = self.width - 1

        elif self.direction == Direction.WEST:
            if self.pos[0] - num >= 0:
                self.pos[0] -= num
                num = 0
            else:
                num = num - self.pos[0]
                self.pos[0] = 0

        if num > 0:
            self.direction = self.getCounterClockwiseDirection()
            return self.step(num)

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.direction.label


obj = Robot(6, 3)
obj.step(2)
obj.step(2)
print(obj.getPos())
print(obj.getDir())
obj.step(2)
obj.step(1)
obj.step(4)
print(obj.getPos())
print(obj.getDir())
