# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description /?envType=daily-question&envId=2024-11-19

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        seen = set()
        subarraySum = 0
        maxSubarrySum = 0
        runningSum = 0
        while j < len(nums):
            if nums[j] in seen:
                seen.remove(nums[i])
                runningSum = runningSum - nums[i]
                i = i + 1

            elif (j - i) + 1 == k:
                seen.add(nums[j])
                runningSum = runningSum + nums[j]
                seen.remove(nums[i])

                maxSubarrySum = max(maxSubarrySum, runningSum)

                subarraySum = subarraySum + runningSum
                runningSum = runningSum - nums[i]

                i = i + 1
                j = j + 1

            else:
                seen.add(nums[j])
                runningSum = runningSum + nums[j]
                j = j + 1

        return maxSubarrySum


print(Solution().maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3))
print(Solution().maximumSubarraySum([4, 4, 4], k=3))
print(Solution().maximumSubarraySum([3, 2, 3, 1], k=3))
