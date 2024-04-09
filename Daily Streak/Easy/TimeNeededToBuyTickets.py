# https://leetcode.com/problems/time-needed-to-buy-tickets/description /?envType=daily-question&envId=2024-04-09

from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        totalTime = 0
        for i in range(len(tickets)):
            totalTime = totalTime + \
                min(tickets[i], tickets[k] if i <= k else tickets[k]-1)
        return totalTime

    # One liner
    def timeRequiredToBuyV2(self, tickets: List[int], k: int) -> int:
        return sum([min(tickets[i], tickets[k] if i <= k else tickets[k]-1) for i in range(len(tickets))])


print(Solution().timeRequiredToBuy(tickets=[2, 3, 2], k=2))
print(Solution().timeRequiredToBuy(tickets=[5, 1, 1, 1], k=0))
print(Solution().timeRequiredToBuy(
    tickets=[84, 49, 5, 24, 70, 77, 87, 8], k=3))

print('-'*100)

print(Solution().timeRequiredToBuyV2(tickets=[2, 3, 2], k=2))
print(Solution().timeRequiredToBuyV2(tickets=[5, 1, 1, 1], k=0))
print(Solution().timeRequiredToBuyV2(
    tickets=[84, 49, 5, 24, 70, 77, 87, 8], k=3))
