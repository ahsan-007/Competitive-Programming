# https://leetcode.com/problems/count-zero-request-servers/description/?envType=daily-question&envId=2026-11-06

from typing import List


class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        logs.sort(key=lambda log: log[1])
        ids = sorted(range(len(queries)), key=lambda i: queries[i])
        ans = [0] * len(queries)
        cnt = [0] * (n + 1)
        left = right = active = 0

        for i in ids:
            q = queries[i]
            while right < len(logs) and logs[right][1] <= q:
                id = logs[right][0]
                if cnt[id] == 0:
                    active += 1
                cnt[id] += 1
                right += 1
            while left < right and logs[left][1] < q - x:
                id = logs[left][0]
                cnt[id] -= 1
                if cnt[id] == 0:
                    active -= 1
                left += 1
            ans[i] = n - active

        return ans


print(Solution().countServers(
    n=3, logs=[[1, 3], [2, 6], [1, 5]], x=5, queries=[10, 11]))
print(Solution().countServers(
    n=3, logs=[[2, 4], [2, 1], [1, 2], [3, 1]], x=2, queries=[3, 4]))
