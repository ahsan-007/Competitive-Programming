# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=daily-question&envId=2024-01-17

from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequences = Counter(arr).values()
        traversed_frequences = set()
        for freq in frequences:
            if freq in traversed_frequences:
                return False
            traversed_frequences.add(freq)

        return True


print(Solution().uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]))
print(Solution().uniqueOccurrences(arr=[1, 2]))
print(Solution().uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
