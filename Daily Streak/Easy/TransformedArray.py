# https://leetcode.com/problems/transformed-array/description/?envType=daily-question&envId=2026-02-05

from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(nums[(i + nums[i]) % len(nums)])
            elif nums[i] < 0:
                dec = abs(nums[i]) % len(nums)
                if i - dec >= 0:
                    result.append(nums[i - dec])
                else:
                    result.append(nums[len(nums) - (dec - i)])
            else:
                result.append(nums[i])
        return result


print(Solution().constructTransformedArray(nums=[3, -2, 1, 1]))
print(Solution().constructTransformedArray(nums=[-1, 4, -1]))
