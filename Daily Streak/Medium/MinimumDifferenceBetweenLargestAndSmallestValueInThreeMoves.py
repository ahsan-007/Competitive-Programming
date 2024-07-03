# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description /?envType=daily-question&envId=2024-07-03

from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        max_moves = 3
        if len(nums) <= max_moves + 1:
            return 0

        def sortMoves():
            for move in range(max_moves + 1):
                min_ind = move
                for i in range(move + 1, len(nums)):
                    if nums[i] < nums[min_ind]:
                        min_ind = i
                nums[move], nums[min_ind] = nums[min_ind], nums[move]

            for move in range(max_moves + 1):
                start_ind = max_ind = len(nums) - move - 1
                for i in range(start_ind - 1, -1, -1):
                    if nums[i] > nums[max_ind]:
                        max_ind = i
                nums[max_ind], nums[start_ind] = nums[start_ind], nums[max_ind]

        sortMoves()

        return min(
            nums[-1] - nums[0],  # no updation
            nums[-1] - nums[1],  # update min 1
            nums[-2] - nums[0],  # update max 1
            nums[-2] - nums[1],  # update min 1 and max 1
            nums[-1] - nums[2],  # update min 1, min 2
            nums[-3] - nums[1],  # update min 1, max 1 and max 2
            nums[-2] - nums[2],  # update min 1, min 2 and max 1
            nums[-1] - nums[3],  # update min 1, min 2 and min3
            nums[-4] - nums[0]  # update max 1, max 2 and max3
        )


print(Solution().minDifference([2, 6, 8, 9, 12, 15, 18]))
print(Solution().minDifference([5, 3, 2, 4]))
print(Solution().minDifference([1, 5, 0, 10, 14]))
print(Solution().minDifference([3, 100, 20]))
print(Solution().minDifference([6, 6, 0, 1, 1, 4, 6]))
print(Solution().minDifference([20, 66, 68, 57, 45, 18, 42, 34, 37, 58]))
