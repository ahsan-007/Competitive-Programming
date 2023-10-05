# https://leetcode.com/problems/majority-element-ii/description/?envType=daily-question&envId=2023-10-05

from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = candidate2 = count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 = count1 + 1

            elif num == candidate2:
                count2 = count2 + 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 = count1 - 1
                count2 = count2 - 1

        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 = count1 + 1
            elif num == candidate2:
                count2 = count2 + 1

        majorityElements = []
        if count1 > len(nums) // 3:
            majorityElements.append(candidate1)

        if count2 > len(nums) // 3:
            majorityElements.append(candidate2)

        return majorityElements


print(Solution().majorityElement(nums=[3, 2, 3]))
print(Solution().majorityElement(nums=[1]))
print(Solution().majorityElement(nums=[1, 2]))
print(Solution().majorityElement(nums=[1, 1, 1, 2, 2, 2]))
