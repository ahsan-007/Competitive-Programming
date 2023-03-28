# https://leetcode.com/problems/reverse-string/

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i = i + 1
            j = j - 1
        return s
    
print(Solution().reverseString(s = ["h","e","l","l","o"]))
print(Solution().reverseString(s = ["H","a","n","n","a","h"]))
