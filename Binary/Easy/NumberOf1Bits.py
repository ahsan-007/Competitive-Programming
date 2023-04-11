# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n % 2 == 1:
                count = count + 1
            n = n >> 1
        return count


print(Solution().hammingWeight(11))
print(Solution().hammingWeight(128))
