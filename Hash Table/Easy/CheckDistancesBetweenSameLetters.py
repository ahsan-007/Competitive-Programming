# https://leetcode.com/problems/check-distances-between-same-letters/

from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        starting_index = [-1 for i in range(26)]
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if starting_index[index] == -1:
                starting_index[index] = i
            elif i - starting_index[index] - 1 != distance[index]:
                return False
        return True


print(
    Solution().checkDistances(s="abaccb", distance=[
        1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
)

print(Solution().checkDistances(s="aa", distance=[
      1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
