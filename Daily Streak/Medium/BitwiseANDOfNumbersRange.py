# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/?envType=daily-question&envId=2024-02-21

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bitwiseAnd = left
        bit = 1
        while bitwiseAnd + bit <= right:
            bitwiseAnd = bitwiseAnd & (bitwiseAnd + bit)
            bit = bit * 2
        return bitwiseAnd

    def rangeBitwiseAndV2(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift = shift + 1
        return left << shift


print(Solution().rangeBitwiseAnd(left=5, right=7))
print(Solution().rangeBitwiseAnd(left=0, right=0))
print(Solution().rangeBitwiseAnd(left=1, right=2147483647))


print(Solution().rangeBitwiseAndV2(left=5, right=7))
print(Solution().rangeBitwiseAndV2(left=0, right=0))
print(Solution().rangeBitwiseAndV2(left=1, right=2147483647))
