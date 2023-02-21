# https://leetcode.com/problems/finding-the-users-active-minutes/

from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        log_map = {}
        for id, minute in logs:
            if id not in log_map:
                log_map[id] = set()
            log_map[id].add(minute)
        UAM_list = [0 for i in range(k)]
        for id in log_map:
            UAM_list[len(log_map[id]) - 1] = UAM_list[len(log_map[id]) - 1] + 1
        return UAM_list


print(Solution().findingUsersActiveMinutes(
    [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], 5))
print(Solution().findingUsersActiveMinutes([[1, 1], [2, 2], [2, 3]], 4))
