# https://leetcode.com/problems/optimal-division/

from typing import List


class Solution:
    def optimalDivision(self, nums: List[int], ) -> str:
        memo = {}
        _, representation = self.optimalDivisionUtil(nums, memo)
        return representation

    def optimalDivisionUtil(self, nums: List[int], memo):
        if len(nums) == 1:
            return nums[0], f"{nums[0]}"
        if tuple(nums) in memo:
            return memo[tuple(nums)]
        max_res = 0
        div = ""
        for i in range(0, len(nums) - 1):
            numerator = nums[i]
            denominator = nums[i+1]
            nums.pop(i+1)
            nums[i] = numerator/denominator
            res, d = self.optimalDivisionUtil(nums, memo)
            if res > max_res:
                max_res = res
                ind = d.find(f"{numerator/denominator}")
                step = len(f"{numerator/denominator}")
                if (ind+step < len(d) and d[ind+step] == '/') or ind-1 < 0 or d[ind] == '(':
                    div = d.replace(f"{numerator/denominator}",
                                    f"{numerator}/{denominator}")
                else:
                    div = d.replace(f"{numerator/denominator}",
                                    f"({numerator}/{denominator})")
            nums[i] = denominator
            nums.insert(i, numerator)

        memo[tuple(nums)] = (max_res, div)
        return max_res, div


print(Solution().optimalDivision(nums=[1000, 100, 10, 2]))
print(Solution().optimalDivision(nums=[2, 3, 4]))
print(Solution().optimalDivision(nums=[10, 3, 5, 9, 10, 5, 4, 10, 10, 9]))
