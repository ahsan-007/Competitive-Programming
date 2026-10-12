# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/description/?envType=daily-question&envId=2026-10-12

from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        bit = 1
        while bit <= nums[0]:
            i = 0
            j = len(nums) - 1

            while i < j:
                if nums[i] & bit > 0:
                    i = i + 1
                elif nums[j] & bit == 0:
                    j = j - 1
                else:
                    nums[i] = nums[i] | bit
                    nums[j] = nums[j] & ~(bit)

                    i = i + 1
                    j = j - 1

            bit = bit << 1
        return sum(num**2 for num in nums[:k]) % (pow(10, 9) + 7)


print(Solution().maxSum(nums=[2, 6, 5, 8], k=2))
print(Solution().maxSum(nums=[4, 5, 4, 7], k=3))
