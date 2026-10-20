# https://leetcode.com/problems/sum-of-sortable-integers/description/?envType=daily-question&envId=2026-10-20

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        def isSortable(nums, target):
            nums = nums + nums
            i = 0
            j = 0
            while i < len(nums) and j < len(target):
                if nums[i] == target[j]:
                    j = j + 1
                else:
                    j = 0
                i = i + 1
            return j == len(target)

        sorted_nums = sorted(nums)
        k = 1
        k_sum = 0
        while k <= len(nums) // 2:
            if len(nums) % k == 0:
                i = 0
                is_countable = True
                while i + k <= len(nums) and is_countable:
                    if not isSortable(nums[i:i+k], sorted_nums[i:i+k]):
                        is_countable = False
                    i = i + k

                if is_countable:
                    k_sum += k
            k = k + 1

        if isSortable(nums, sorted_nums):
            k_sum += len(nums)
        return k_sum


print(Solution().sortableIntegers(nums=[3, 1, 2]))
print(Solution().sortableIntegers(nums=[7, 6, 5]))
print(Solution().sortableIntegers(nums=[5, 8]))
