# https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/?envType=daily-question&envId=2023-10-22

from typing import List


class Solution:
    # Time: O(n)
    # Space: O(1)
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = j = k
        minimum = maxScore = nums[k]
        while i > 0 or j < len(nums) - 1:
            if i == 0 or (j < len(nums) - 1 and nums[i - 1] < nums[j + 1]):
                minimum = min(minimum, nums[j + 1])
                j = j + 1
            else:
                minimum = min(minimum, nums[i - 1])
                i = i - 1

            maxScore = max(maxScore, minimum * (j - i + 1))

        return maxScore


print(Solution().maximumScore(nums=[1, 4, 3, 7, 4, 5], k=3))
print(Solution().maximumScore(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0))
