# https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2024-09-04
# https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2026-04-06

from typing import List
from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = 0
        y = 0
        path_obstacles = set(tuple(ob) for ob in obstacles)
        direction = Direction.NORTH
        max_euclidean_distance = 0
        for cmd in commands:
            if cmd in {-1, -2}:
                # if direction is -2 we need to decrement by 1 which is equal to increment by 3
                direction = Direction(
                    (direction.value + (1 if cmd == -1 else 3)) % 4)
            else:
                obstacle_found = False
                k = 0
                while k < cmd and not obstacle_found:
                    if direction == Direction.NORTH:
                        y = y + 1
                        if (x, y) in path_obstacles:
                            obstacle_found = True
                            y = y - 1

                    elif direction == Direction.SOUTH:
                        y = y - 1
                        if (x, y) in path_obstacles:
                            obstacle_found = True
                            y = y + 1

                    elif direction == Direction.EAST:
                        x = x + 1
                        if (x, y) in path_obstacles:
                            obstacle_found = True
                            x = x - 1

                    elif direction == Direction.WEST:
                        x = x - 1
                        if (x, y) in path_obstacles:
                            obstacle_found = True
                            x = x + 1

                    max_euclidean_distance = max(
                        max_euclidean_distance, (x-0)**2 + (y-0)**2)
                    k = k + 1
        return max_euclidean_distance


print(Solution().robotSim(commands=[4, -1, 3], obstacles=[]))
print(Solution().robotSim(commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]))
print(Solution().robotSim(commands=[6, -1, -1, 6], obstacles=[[0, 0]]))
