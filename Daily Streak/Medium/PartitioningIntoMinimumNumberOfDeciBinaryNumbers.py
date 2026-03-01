# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/?envType=daily-question&envId=2026-03-01

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


print(Solution().minPartitions(n="32"))
print(Solution().minPartitions(n="82734"))
print(Solution().minPartitions(n="27346209830709182346"))
