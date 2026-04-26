# https://leetcode.com/problems/detect-cycles-in-2d-grid/description/?envType=daily-question&envId=2026-04-26

from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def isCycleExists(i, j, dir, target, curr_seen, global_seen):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != target:
                return False

            if (i, j) in curr_seen:
                return True

            curr_seen.add((i, j))
            global_seen.add((i, j))
            return (
                (dir != 'U' and isCycleExists(i+1, j, 'D', target, curr_seen, global_seen)) or
                (dir != 'D' and isCycleExists(i-1, j, 'U', target, curr_seen, global_seen)) or
                (dir != 'L' and isCycleExists(i, j+1, 'R', target, curr_seen, global_seen)) or
                (dir != 'R' and isCycleExists(
                    i, j-1, 'L', target, curr_seen, global_seen))
            )

        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in seen:
                    if isCycleExists(i, j, '', grid[i][j], set(), seen):
                        return True
        return False


print(Solution().containsCycle(grid=[["a", "a", "a", "a"], [
      "a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]))

print(Solution().containsCycle(grid=[["c", "c", "c", "a"], [
      "c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]))
print(Solution().containsCycle(
    grid=[["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]))
