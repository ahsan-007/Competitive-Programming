# https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        frequency = {}
        for ch in s:
            if ch in frequency:
                count += 1
                frequency.clear()
            frequency[ch] = True
        return count + 1


print(Solution().partitionString("abacaba"))
print(Solution().partitionString("ssssss"))
