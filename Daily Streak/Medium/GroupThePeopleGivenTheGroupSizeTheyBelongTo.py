# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/?envType=daily-question&envId=2023-09-11

from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = []
        current_groups = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in current_groups:
                current_groups[groupSizes[i]] = []
            current_groups[groupSizes[i]].append(i)

            if len(current_groups[groupSizes[i]]) == groupSizes[i]:
                groups.append(current_groups[groupSizes[i]])
                current_groups[groupSizes[i]] = []

        return groups


print(Solution().groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3]))
print(Solution().groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2]))
