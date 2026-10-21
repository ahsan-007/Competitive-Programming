# https://leetcode.com/problems/minimum-operations-to-sort-a-string/description/?envType=daily-question&envId=2026-10-21

class Solution:
    # Time: O(N)
    def minOperations(self, s: str) -> int:
        def isSorted(s):
            for i in range(1, len(s)):
                if ord(s[i]) < ord(s[i-1]):
                    return False
            return True

        if isSorted(s):
            return 0

        if len(s) <= 2:
            return -1

        min_char_ind = 0
        min_char = s[0]

        max_char = s[0]
        max_char_ind = 0
        for i in range(1, len(s)):
            if ord(s[i]) < ord(min_char):
                min_char = s[i]
                min_char_ind = i

            if ord(s[i]) >= ord(max_char):
                max_char = s[i]
                max_char_ind = i

        if min_char_ind == 0:
            return 1
        elif min_char_ind == len(s) - 1:
            return 3 if max_char_ind == 0 else 2
        else:
            return 1 if max_char_ind == len(s) - 1 else 2


print(Solution().minOperations(s="dog"))
print(Solution().minOperations(s="card"))
print(Solution().minOperations(s="gf"))
