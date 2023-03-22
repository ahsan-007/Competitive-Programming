# https://leetcode.com/problems/decompress-run-length-encoded-list/

from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
            ans.extend([nums[i + 1]] * nums[i])
            i = i + 2
        return ans


print(Solution().decompressRLElist(nums=[1, 2, 3, 4]))
print(Solution().decompressRLElist(nums=[1, 1, 2, 3]))
