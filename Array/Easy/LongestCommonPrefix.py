# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[i-1][j]:
                    return strs[i][:j]
        return strs[0]


print(Solution().longestCommonPrefix(strs=["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(strs=["dog", "racecar", "car"]))
