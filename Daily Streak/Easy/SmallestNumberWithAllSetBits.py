# https://leetcode.com/problems/smallest-number-with-all-set-bits/description/?envType=daily-question&envId=2025-10-29

class Solution:
    def smallestNumber(self, n: int) -> int:
        return int('1' * (len(bin(n))-2), 2)

    def smallestNumberV2(self, n: int) -> int:
        return (1 << (len(bin(n))-2)) - 1


print(Solution().smallestNumber(5))
print(Solution().smallestNumber(10))
print(Solution().smallestNumber(3))

print(Solution().smallestNumberV2(5))
print(Solution().smallestNumberV2(10))
print(Solution().smallestNumberV2(3))
