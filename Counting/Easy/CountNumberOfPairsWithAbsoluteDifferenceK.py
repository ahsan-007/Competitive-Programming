# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/


from typing import List
from collections import Counter


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        numbers = Counter(nums)
        count = 0
        print(numbers)
        for num in numbers:
            if num + k in numbers:
                count = count + numbers[num + k] * numbers[num]
        return count


print(Solution().countKDifference(nums=[1, 2, 2, 1], k=1))
print(Solution().countKDifference(nums=[1, 3], k=3))
print(Solution().countKDifference(nums=[3, 2, 1, 5, 4], k=2))
