# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = maximum = salary[0]
        sum_of_elements = 0
        for ele in salary:
            sum_of_elements = sum_of_elements + ele
            if ele > maximum:
                maximum = ele
            elif ele < minimum:
                minimum = ele
        return round((sum_of_elements - (minimum + maximum)) / (len(salary) - 2), 5)


print(Solution().average(salary=[4000, 3000, 1000, 2000]))
print(Solution().average(salary=[1000, 2000, 3000]))
print(Solution().average(salary=[1000.342304324, 2000.342304324, 3000]))
