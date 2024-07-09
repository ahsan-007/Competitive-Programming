# https://leetcode.com/problems/average-waiting-time/description /?envType=daily-question&envId=2024-07-09

from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_waiting_time = 0
        for customer in customers:
            if current_time < customer[0]:
                current_time = customer[0]

            total_waiting_time = total_waiting_time + \
                customer[1] + (current_time - customer[0])
            current_time = current_time + customer[1]

        return round(total_waiting_time / len(customers), 5)


print(Solution().averageWaitingTime(customers=[[1, 2], [2, 5], [4, 3]]))
print(Solution().averageWaitingTime(
    customers=[[5, 2], [5, 4], [10, 3], [20, 1]]))
