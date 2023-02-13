# https://leetcode.com/problems/destination-city/

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_path = {}
        for path in paths:
            outgoing_path[path[0]] = True
            if path[1] not in outgoing_path:
                outgoing_path[path[1]] = False

        for key in outgoing_path:
            if outgoing_path[key] == False:
                return key


print(Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(Solution().destCity([["B","C"],["D","B"],["C","A"]]))
