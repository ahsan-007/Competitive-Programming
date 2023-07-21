# https://leetcode.com/problems/asteroid-collision/

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        for i in range(len(asteroids)):
            if asteroids[i] < 0:
                j = i - 1
                keep_going = True
                while j >= 0 and keep_going:
                    if asteroids[j] != 0:
                        if asteroids[j] < 0:
                            keep_going = False
                        else:
                            if asteroids[j] < abs(asteroids[i]):
                                asteroids[j] = 0
                            else:
                                if asteroids[j] == abs(asteroids[i]):
                                    asteroids[j] = 0
                                asteroids[i] = 0
                                keep_going = False
                    j = j - 1
        return [asteroid for asteroid in asteroids if asteroid != 0]

    # using stack
    def asteroidCollisionV2(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                exploded = False
                while stack and not exploded and stack[-1] > 0:
                    if stack[-1] <= abs(asteroid):
                        if stack[-1] == abs(asteroid):
                            exploded = True
                        stack.pop()
                    else:
                        exploded = True
            if asteroid > 0 or not exploded:
                stack.append(asteroid)
        return stack


print(Solution().asteroidCollision(asteroids=[5, 10, -5]))  # [5,10]
print(Solution().asteroidCollision(asteroids=[8, -8]))  # []
print(Solution().asteroidCollision(asteroids=[10, 2, -5]))  # [10]


print(Solution().asteroidCollisionV2(asteroids=[5, 10, -5]))  # [5,10]
print(Solution().asteroidCollisionV2(asteroids=[8, -8]))  # []
print(Solution().asteroidCollisionV2(asteroids=[10, 2, -5]))  # [10]
