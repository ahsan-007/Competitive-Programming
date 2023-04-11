# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        # b should be initialized to 2
        # but then an extra if condition will be needed to handle the case when n == 1
        # after setting b = 1 and starting iteration from 2, if condition will no longer be needed
        for i in range(2, n+1):
            a, b = b, a + b
        return b


print(Solution().climbStairs(3))
print(Solution().climbStairs(5))
