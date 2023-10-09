# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=daily-question&envId=2023-10-09


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.searchRangeUtil(nums, target, 0, len(nums)-1, True), self.searchRangeUtil(nums, target, 0, len(nums)-1, False)

    def searchRangeUtil(self, nums, target, lb, ub, left_most):
        if lb > ub:
            return -1

        mid = lb + (ub - lb) // 2
        if nums[mid] == target:
            if left_most:
                return mid if mid == lb or nums[mid-1] != target else self.searchRangeUtil(nums, target, lb, mid - 1, left_most)
            else:
                return mid if mid == ub or nums[mid+1] != target else self.searchRangeUtil(nums, target, mid+1, ub, left_most)
        elif target < nums[mid]:
            return self.searchRangeUtil(nums, target, lb, mid - 1, left_most)

        else:
            return self.searchRangeUtil(nums, target, mid+1, ub, left_most)


print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
print(Solution().searchRange(nums=[], target=0))
