# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/?envType=daily-question&envId=2024-12-01

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for ele in arr:
            if ele / 2 in seen or ele * 2 in seen:
                return True
            seen.add(ele)
        return False


print(Solution().checkIfExist(arr=[10, 2, 5, 3]))
print(Solution().checkIfExist(arr=[3, 1, 7, 11]))
