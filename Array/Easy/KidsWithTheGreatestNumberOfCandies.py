# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [True if no_of_candies + extraCandies >= max_candies else False for no_of_candies in candies]


print(Solution().kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
print(Solution().kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
print(Solution().kidsWithCandies(candies=[12, 1, 12], extraCandies=10))
