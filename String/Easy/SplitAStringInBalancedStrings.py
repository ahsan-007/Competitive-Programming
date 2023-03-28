# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 1 if s[0] == 'R' else -1
        count = 0
        for i in range(1, len(s)):
            balance = balance + 1 if s[i] == 'R' else balance - 1
            if balance == 0:
                count = count + 1
        return count


print(Solution().balancedStringSplit(s="RLRRLLRLRL"))
print(Solution().balancedStringSplit(s="RLRRRLLRLL"))
print(Solution().balancedStringSplit(s="LLLLRRRR"))
