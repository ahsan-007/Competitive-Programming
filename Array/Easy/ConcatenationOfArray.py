# https://leetcode.com/problems/concatenation-of-array/

from typing import List


class Solution:
    # One Liner
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2

    # Version 2
    def getConcatenationV2(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            ans.insert(i, nums[i])
            ans.append(nums[i])
            i = i + 1
        return ans

    # Version 3
    def getConcatenationV3(self, nums: List[int]) -> List[int]:
        ans = [0 for i in range(len(nums) * 2)]
        for i in range(len(nums)):
            ans[i] = ans[i + len(nums)] = nums[i]
        return ans


print(Solution().getConcatenation(nums=[1, 2, 1]))
print(Solution().getConcatenationV2(nums=[1, 2, 1]))
print(Solution().getConcatenationV3(nums=[1, 2, 1]))

print(Solution().getConcatenation(nums=[1, 3, 2, 1]))
print(Solution().getConcatenationV2(nums=[1, 3, 2, 1]))
print(Solution().getConcatenationV3(nums=[1, 3, 2, 1]))
