# https://leetcode.com/problems/smallest-unique-subarray/description/?envType=daily-question&envId=2026-11-25

from typing import List
from collections import defaultdict

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        MOD = 1000000007
        BASE = 911382323

        n = len(nums)
        h = [0] * (n + 1)
        p = [0] * (n + 1)
        p[0] = 1

        # Compute prefix hashes and powers of BASE
        for i in range(n):
            h[i + 1] = (h[i] * BASE + nums[i]) % MOD
            p[i + 1] = p[i] * BASE % MOD

        def check(length):
            cnt = {}
            for l in range(n - length + 1):
                r = l + length
                key = (h[r] - h[l] * p[length] % MOD + MOD) % MOD
                cnt[key] = cnt.get(key, 0) + 1

            for times in cnt.values():
                if times == 1:
                    return True
            return False

        def smallestUniqueSubarrayUtil(nums, lb, ub):
            if lb > ub:
                return len(nums)

            mid = lb + (ub - lb) // 2

            if check(mid):
                return min(mid, smallestUniqueSubarrayUtil(nums, lb, mid - 1))

            return smallestUniqueSubarrayUtil(nums, mid + 1, ub)

        return smallestUniqueSubarrayUtil(nums, 1, len(nums))

            


print(Solution().smallestUniqueSubarray(nums = [3,3,3]))
print(Solution().smallestUniqueSubarray(nums = [2,1,2,3,3]))
print(Solution().smallestUniqueSubarray(nums = [1,1,2,2,1]))
print(Solution().smallestUniqueSubarray(nums = [8,3,6,2,8,3,6,2,8,3,6,2,8,3,6,2,8,3,6,2,8,3,6,2,8,3,6,2,8,3,6,2]))