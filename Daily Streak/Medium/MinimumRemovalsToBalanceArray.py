# https://leetcode.com/problems/minimum-removals-to-balance-array/description/?envType=daily-question&envId=2026-02-06

from typing import List


class Solution:
    # Time: O(NlogN)
    def minRemoval(self, nums: List[int], k: int) -> int:
        def binarySearch(i, j, target):
            if i > j:
                return -1

            mid = i + (j - i) // 2
            if nums[mid] > target:
                return binarySearch(i, mid - 1, target)
            else:
                return max(mid, binarySearch(mid + 1, j, target))

        nums.sort()
        minCount = float("+inf")
        i = 0
        for i in range(len(nums)):
            ind = binarySearch(i, len(nums)-1, nums[i] * k)
            minCount = min(minCount, len(nums) - (ind - i + 1))
        return minCount

    # Time: O(NlogN)
    def minRemovalV2(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = 0
        maxCount = 0
        while j < len(nums):
            if i == j or nums[j] <= nums[i] * k:
                maxCount = max(maxCount, j - i + 1)
                j = j + 1
            else:
                i = i + 1
        return len(nums) - maxCount


print(Solution().minRemoval(nums=[2, 1, 5], k=2))
print(Solution().minRemoval(nums=[1, 6, 2, 9], k=3))
print(Solution().minRemoval(nums=[20, 5, 11], k=2))
print(Solution().minRemoval(nums=[4, 6], k=2))

print('-' * 100)

print(Solution().minRemovalV2(nums=[2, 1, 5], k=2))
print(Solution().minRemovalV2(nums=[1, 6, 2, 9], k=3))
print(Solution().minRemovalV2(nums=[20, 5, 11], k=2))
print(Solution().minRemovalV2(nums=[4, 6], k=2))
