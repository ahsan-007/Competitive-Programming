# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/?envType=daily-question&envId=2025-04-28

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def binarySearch(prefixSum, i, j, startInd):
            if j - i == 1:
                return i if (prefixSum[startInd] - prefixSum[i]) * (startInd - i) < k else -1

            if i >= j:
                return -1

            mid = i + (j - i) // 2
            if (prefixSum[startInd] - prefixSum[mid]) * (startInd - mid) < k:
                ind = binarySearch(prefixSum, i, mid, startInd)
                return min(mid, ind if ind != -1 else mid)

            return binarySearch(prefixSum, mid, j, startInd)

        prefixSum = [0] * len(nums)
        for i in range(len(nums)):
            prefixSum[i] = nums[i] + (prefixSum[i - 1] if i > 0 else 0)

        count = 0
        for i in range(len(prefixSum)):
            if prefixSum[i] * (i + 1) < k:
                count = count + i + 1
            else:
                ind = binarySearch(prefixSum, 0, i, i)
                if ind != -1:
                    count = count + (i - ind)
        return count

    def countSubarraysV2(self, nums: List[int], k: int) -> int:
        count = 0
        cumulativeSum = 0
        i = 0
        for j in range(len(nums)):
            cumulativeSum = cumulativeSum + nums[j]
            while i <= j and cumulativeSum * (j - i + 1) >= k:
                cumulativeSum = cumulativeSum - nums[i]
                i = i + 1
            count = count + j - i + 1
        return count


print(Solution().countSubarrays(nums=[2, 1, 4, 3, 5], k=10))
print(Solution().countSubarrays(nums=[1, 1, 1], k=5))
print(Solution().countSubarrays(nums=[4, 3, 5], k=11))
print(Solution().countSubarrays(
    nums=[9, 5, 3, 8, 4, 7, 2, 7, 4, 5, 4, 9, 1, 4, 8, 10, 8, 10, 4, 7], k=4))

print('-' * 100)

print(Solution().countSubarraysV2(nums=[2, 1, 4, 3, 5], k=10))
print(Solution().countSubarraysV2(nums=[1, 1, 1], k=5))
print(Solution().countSubarraysV2(nums=[4, 3, 5], k=11))
print(Solution().countSubarraysV2(
    nums=[9, 5, 3, 8, 4, 7, 2, 7, 4, 5, 4, 9, 1, 4, 8, 10, 8, 10, 4, 7], k=4))
