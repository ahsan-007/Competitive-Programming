# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        group_list = []
        for i in range(len(groupSizes)):
            if groupSizes[i] not in groups:
                groups[groupSizes[i]] = []

            groups[groupSizes[i]].append(i)

            if len(groups[groupSizes[i]]) == groupSizes[i]:
                group_list.extend([groups[groupSizes[i]]])
                groups[groupSizes[i]] = []
        return group_list


print(Solution().groupThePeople([3, 3, 3, 3, 3, 1, 3]))
print(Solution().groupThePeople([2, 1, 3, 3, 3, 2]))
