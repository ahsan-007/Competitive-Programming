# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/description/?envType=daily-question&envId=2026-10-17

from typing import List
import math


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        digit_sum = sorted([(sum(int(ch) for ch in str(num)), num)
                           for num in nums])

        index_to_num = {i: nums[i] for i in range(len(nums))}
        num_to_index = {nums[i]: i for i in range(len(nums))}

        swaps = 0
        for i in range(len(digit_sum)):
            _, num = digit_sum[i]
            if i != num_to_index[num]:
                swap_ind = num_to_index[num]
                swap_num = index_to_num[i]

                num_to_index[num], num_to_index[swap_num] = num_to_index[swap_num], num_to_index[num]
                index_to_num[i], index_to_num[swap_ind] = index_to_num[swap_ind], index_to_num[i]

                swaps += 1

        return swaps


print(Solution().minSwaps(nums=[37, 100]))
print(Solution().minSwaps(nums=[22, 14, 33, 7]))
print(Solution().minSwaps(nums=[18, 43, 34, 16]))
print(Solution().minSwaps(nums=[277993448, 416038674, 616955867, 539372283]))
