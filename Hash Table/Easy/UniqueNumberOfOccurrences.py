# https://leetcode.com/problems/unique-number-of-occurrences/

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for ele in arr:
            occurrences[ele] = occurrences.get(ele, 0) + 1

        processed = {}
        for value in occurrences.values():
            if value in processed:
                return False
            processed[value] = True
        return True
    
    
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
print(Solution().uniqueOccurrences([1,2]))
print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
