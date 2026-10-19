# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/?envType=daily-question&envId=2026-10-19

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [i for i, num in enumerate(sorted(nums)) if num == target]


print(Solution().targetIndices(nums=[1, 2, 5, 2, 3], target=2))
print(Solution().targetIndices(nums=[1, 2, 5, 2, 3], target=3))
print(Solution().targetIndices(nums=[1, 2, 5, 2, 3], target=5))
