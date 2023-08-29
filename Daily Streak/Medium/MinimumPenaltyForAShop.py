# https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
    # Two Passes
    def bestClosingTime(self, customers: str) -> int:
        penalty = sum(1 for customer in customers if customer == 'Y')
        minimum_penalty = penalty
        hour = 0
        i = 0
        while i < len(customers):
            penalty = penalty + (1 if customers[i] == 'N' else -1)
            if penalty < minimum_penalty:
                minimum_penalty = penalty
                hour = i + 1
            i = i + 1
        return hour

    # One Pass
    def bestClosingTimeV2(self, customers: str) -> int:
        minimum_penalty = penalty = 0
        hour = 0
        i = 0
        while i < len(customers):
            penalty = penalty + (1 if customers[i] == 'N' else -1)
            if penalty < minimum_penalty:
                minimum_penalty = penalty
                hour = i + 1
            i = i + 1
        return hour


print(Solution().bestClosingTime(customers="YYNY"))
print(Solution().bestClosingTime(customers="NNNNN"))
print(Solution().bestClosingTime(customers="YYYY"))

print(Solution().bestClosingTimeV2(customers="YYNY"))
print(Solution().bestClosingTimeV2(customers="NNNNN"))
print(Solution().bestClosingTimeV2(customers="YYYY"))
