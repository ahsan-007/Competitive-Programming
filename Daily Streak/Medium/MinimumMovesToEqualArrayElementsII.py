# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/?envType=daily-question&envId=2026-11-02

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(median - num) for num in nums)


print(Solution().minMoves2(nums=[1, 2, 3]))
print(Solution().minMoves2(nums=[1, 10, 2, 9]))
