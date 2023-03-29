# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
from typing import List
from itertools import combinations
import bisect


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        sum_threshold = sum(nums) // 2

        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]

        res = abs(sum(left) - sum(right))

        left = self.get_sum(left)
        right = self.get_sum(right)
        total_sum = sum(nums)

        for k in range(len(left)):
            j = len(right) - k - 1
            right_sum = right[j]
            right_sum.sort()
            for ele1 in left[k]:
                r = sum_threshold - ele1
                p = bisect.bisect_left(right_sum, r)
                for q in range(p-1, p+1):
                    if 0 <= q < len(right_sum):
                        left_ans_sum = ele1 + right_sum[q]
                        right_ans_sum = total_sum - left_ans_sum
                        diff = abs(left_ans_sum - right_ans_sum)
                        res = min(res, diff)
        return res

    def get_sum(self, nums):
        nums_sum = [[] for i in range(len(nums) - 1)]
        for i in range(1, (2 ** len(nums)) // 2):
            binary = str(bin(i))[2:][::-1]
            ele_count = 0
            running_sum = 0
            all_sum = sum(nums)
            j = 0
            while j < len(binary):
                if binary[j] == '1':
                    running_sum = running_sum + nums[j]
                    ele_count = ele_count + 1
                j = j + 1
            nums_sum[ele_count - 1].append(running_sum)
            nums_sum[(len(nums) - ele_count) -
                     1].append(all_sum - running_sum)
        return nums_sum

    # def get_sums(nums):  # generate all combinations sum of k elements
    #             ans = {}
    #             N = len(nums)
    #             for k in range(1, N+1):  # takes k element for nums
    #                 sums = []
    #                 for comb in combinations(nums, k):
    #                     s = sum(comb)
    #                     sums.append(s)
    #                 ans[k] = sums
    #             return ans


print(Solution().minimumDifference([1, 2, 3, 4]))
print(Solution().minimumDifference([36, -36]))
print(Solution().minimumDifference([2, -1, 0, 4, -2, -9]))
print(Solution().minimumDifference([3, 9, 7, 3]))
print(Solution().minimumDifference([11051, 87770, -36560, 88162, -74110, 89633,
                                    -53233, -46348, 70900, -79673, 49622, -30734, 50897, -88316, -2296, -23125]))
print(Solution().minimumDifference([-65941, -93008, -16458,
                                   -95021, 268107, 60734, -35654, -38922, -757, 18532]))

print(Solution().minimumDifference([7772197, 4460211, -7641449, -8856364, 546755, -3673029, 527497, -9392076, 3130315, -5309187, -4781283, 5919119, 3093450,
      1132720, 6380128, -3954678, -1651499, -7944388, -3056827, 1610628, 7711173, 6595873, 302974, 7656726, -2572679, 0, 2121026, -5743797, -8897395, -9699694]))
