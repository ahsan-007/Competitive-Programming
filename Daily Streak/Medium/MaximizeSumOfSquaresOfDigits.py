# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/description/?envType=daily-question&envId=2026-10-14

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        max_sum_num = "9" * (sum // 9)
        if sum % 9 > 0:
            max_sum_num += str(sum % 9)
        return (max_sum_num + "0" * (num - len(max_sum_num))) if len(max_sum_num) <= num else ""


print(Solution().maxSumOfSquares(num=2, sum=3))
print(Solution().maxSumOfSquares(num=2, sum=17))
print(Solution().maxSumOfSquares(num=1, sum=10))
