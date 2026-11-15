# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/?envType=daily-question&envId=2026-11-15

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = prefix_sum = 0

        odd_count = 0
        even_count = 1

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                count += odd_count
                even_count += 1
            else:
                count += even_count
                odd_count += 1

            count = count % (pow(10, 9) + 7)

        return count


print(Solution().numOfSubarrays(arr=[1, 3, 5]))
print(Solution().numOfSubarrays(arr=[2, 4, 6]))
print(Solution().numOfSubarrays(arr=[1, 2, 3, 4, 5, 6, 7]))
