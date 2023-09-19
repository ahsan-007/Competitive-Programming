# https://leetcode.com/problems/find-the-duplicate-number/description/?envType=daily-question&envId=2023-09-19


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i != nums[i] - 1:
                if nums[nums[i]-1] == nums[i]:
                    return nums[i]
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i = i + 1

    def findDuplicateV2(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


print(Solution().findDuplicate(nums=[1, 3, 4, 2, 2]))
print(Solution().findDuplicate(nums=[3, 1, 3, 4, 2]))
print(Solution().findDuplicate(nums=[3, 1, 3, 3, 2]))
print(Solution().findDuplicate(nums=[2, 3, 4, 5, 3, 6, 3, 7]))
print(Solution().findDuplicate(
    nums=[8, 7, 1, 10, 17, 15, 18, 11, 16, 9, 19, 12, 5, 14, 3, 4, 2, 13, 18, 18]))

print(Solution().findDuplicateV2(nums=[1, 3, 4, 2, 2]))
print(Solution().findDuplicateV2(nums=[3, 1, 3, 4, 2]))
print(Solution().findDuplicateV2(nums=[3, 1, 3, 3, 2]))
print(Solution().findDuplicateV2(nums=[2, 3, 4, 5, 3, 6, 3, 7]))
print(Solution().findDuplicateV2(
    nums=[8, 7, 1, 10, 17, 15, 18, 11, 16, 9, 19, 12, 5, 14, 3, 4, 2, 13, 18, 18]))
