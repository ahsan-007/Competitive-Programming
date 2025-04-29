# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2024-03-29

from typing import List


class Solution:
    # Time: O(N), Space: O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        maxEle = max(nums)
        maxEleCount = 0
        i = 0
        j = 0
        while j < len(nums) or maxEleCount == k:
            if maxEleCount == k:
                count = count + 1
                if j < len(nums):
                    count = count + len(nums) - j

                if nums[i] == maxEle:
                    maxEleCount = maxEleCount - 1
                i = i + 1
            else:
                if nums[j] == maxEle:
                    maxEleCount = maxEleCount + 1
                j = j + 1

            # alternate approach with a nested loop, Time complexity is still O(N)
            # if nums[j] == maxEle:
            #     maxEleCount = maxEleCount + 1

            # while i <= j and maxEleCount == k:
            #     count = count + 1 + (len(nums) - (j + 1))

            #     if nums[i] == maxEle:
            #         maxEleCount = maxEleCount - 1
            #     i = i + 1
            # j = j + 1

        return count


print(Solution().countSubarrays(nums=[1, 3, 2, 3, 3], k=2))
print(Solution().countSubarrays(nums=[1, 4, 2, 1], k=3))
print(Solution().countSubarrays(nums=[1, 4, 2, 1], k=1))
