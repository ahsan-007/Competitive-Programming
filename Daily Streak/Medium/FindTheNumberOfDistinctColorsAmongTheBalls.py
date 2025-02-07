# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/?envType=daily-question&envId=2025-02-07


from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colored_balls = {}
        color_frequency = {}
        result = [0] * len(queries)
        for i in range(len(queries)):
            ball, color = queries[i]

            prev_color = colored_balls.get(ball)
            colored_balls[ball] = color
            if prev_color in color_frequency:
                color_frequency[prev_color] = color_frequency[prev_color] - 1
                if color_frequency[prev_color] == 0:
                    del color_frequency[prev_color]
            color_frequency[color] = color_frequency.get(color, 0) + 1

            result[i] = len(color_frequency)
        return result


print(Solution().queryResults(
    limit=4, queries=[[1, 4], [2, 5], [1, 3], [3, 4]]))

print(Solution().queryResults(
    limit=4, queries=[[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]))
