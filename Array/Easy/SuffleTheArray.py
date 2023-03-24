# https://leetcode.com/problems/shuffle-the-array/

from typing import List


class Solution:
   
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans


print(Solution().shuffle(nums=[2, 5, 1, 3, 4, 7], n=3))
print(Solution().shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4))
print(Solution().shuffle(nums=[1, 1, 2, 2], n=2))
