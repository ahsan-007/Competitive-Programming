# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/?envType=daily-question&envId=2023-09-20


from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x

        if target == 0:
            return len(nums)

        max_length = curr_sum = left = 0

        for right, value in enumerate(nums):
            curr_sum = curr_sum + value

            while curr_sum > target and left <= right:
                curr_sum = curr_sum - nums[left]
                left = left + 1

            if curr_sum == target:
                max_length = max(max_length, right-left + 1)

        return (len(nums) - max_length) if max_length else -1


print(Solution().minOperations(nums=[1, 1, 4, 2, 3], x=5))
print(Solution().minOperations(nums=[5, 6, 7, 8, 9], x=4))
print(Solution().minOperations(nums=[3, 2, 20, 1, 1, 3], x=10))
