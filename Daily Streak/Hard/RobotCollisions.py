# https://leetcode.com/problems/robot-collisions/description/?envType=daily-question&envId=2024-07-13
# https://leetcode.com/problems/robot-collisions/description/?envType=daily-question&envId=2026-04-01

from typing import List


class Solution:
    # Time: O(NlogN), Space: O(N)
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # store position to index mapping to sort the ans
        position_index_map = {p: i for i, p in enumerate(positions)}
        indicators = sorted(zip(positions, healths, directions))
        ans = []
        right_robots = []
        for position, health, direction in indicators:
            if direction == 'R':
                right_robots.append([position, health])
            else:
                # current robot has L direction and there is no R robot seen earlier, therefore add it in ans
                if not right_robots:
                    ans.append([position, health])
                else:
                    # while L robot's health is greater than R robot at stack top
                    while right_robots and right_robots[-1][-1] < health:
                        health = health - 1
                        right_robots.pop(-1)

                    # if not R robots are left, add current robot in ans
                    if not right_robots:
                        ans.append([position, health])
                    # if R and L robots have same length, remove R robot
                    elif health == right_robots[-1][-1]:
                        right_robots.pop(-1)
                    # if L robot's health is smaller than the R robot at stack top then decrement health
                    else:
                        right_robots[-1][-1] -= 1
        ans.extend(right_robots)
        # sort the ans as per the original position of the robots
        ans.sort(key=lambda x: position_index_map[x[0]])
        return [health for _, health in ans]


print(Solution().survivedRobotsHealths(positions=[5, 4, 3, 2, 1], healths=[
      2, 17, 9, 15, 10], directions="RRRRR"))

print(Solution().survivedRobotsHealths(
    positions=[3, 5, 2, 6], healths=[10, 10, 15, 12], directions="RLRL"))

print(Solution().survivedRobotsHealths(
    positions=[1, 2, 5, 6], healths=[10, 10, 11, 11], directions="RLRL"))
