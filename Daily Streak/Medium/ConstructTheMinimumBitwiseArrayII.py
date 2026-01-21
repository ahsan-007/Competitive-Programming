# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/description/?envType=daily-question&envId=2026-01-21


from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def getAns(num):
            d = 1
            ans = -1
            while num & d != 0:
                ans = num - d
                d = d << 1
            return ans

        return [getAns(num) for num in nums]


print(Solution().minBitwiseArray(nums=[2, 3, 5, 7]))
print(Solution().minBitwiseArray(nums=[11, 13, 31]))
