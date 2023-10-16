# https://leetcode.com/problems/rotate-array/description/

from typing import List


class Solution:
    # Time: O(N)
    # Space: O(K)
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        elements = nums[len(nums) - k:]
        i = (len(nums) - k) - 1
        j = len(nums) - 1
        while i >= 0:
            nums[j] = nums[i]
            i = i - 1
            j = j - 1

        i = 0
        j = 0
        while i < len(elements):
            nums[j] = elements[i]
            i = i + 1
            j = j + 1

        return nums

    # Time: O(N)
    # Space: O(1)
    def rotateV2(self, nums: List[int], k: int) -> None:
        def reverse(arr, i, j):
            if i >= j:
                return
            arr[i], arr[j] = arr[j], arr[i]
            reverse(arr, i + 1, j - 1)

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums) - 1)
        return nums


print(Solution().rotateV2(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
print(Solution().rotateV2(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], k=3))
print(Solution().rotateV2(nums=[-1, -100, 3, 99],  k=2))
print(Solution().rotateV2(nums=[1, 2],  k=3))
print(Solution().rotateV2(nums=[1, 2, 3, 4, 5, 6],  k=4))
print(Solution().rotateV2(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
      13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],  k=38))
