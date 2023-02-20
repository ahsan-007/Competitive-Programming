# https://leetcode.com/problems/divide-array-into-equal-pairs/

from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] = frequency[num] + 1
            else:
                frequency[num] = 1
        for value in frequency.values():
            if value % 2 != 0:
                return False
        return True

    def divideArrayXOR(self, nums: List[int]) -> bool:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        return xor == 0


print(Solution().divideArray([3, 2, 3, 2, 2, 2]))
print(Solution().divideArray([1, 2, 3, 4]))
print(Solution().divideArray([9, 9, 19, 10, 9, 12, 2, 12, 3, 3, 11, 5, 8, 4, 13, 6, 2, 11, 9, 19, 11, 15, 9, 17, 15, 12, 5,
      14, 12, 16, 18, 16, 10, 3, 8, 9, 16, 20, 2, 4, 16, 12, 11, 14, 20, 16, 2, 18, 17, 20, 3, 13, 16, 17, 1, 1, 11, 20, 20, 4]))
