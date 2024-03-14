# https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-03-13


class Solution:
    # Time: O(log N), Space: O(1)
    def pivotInteger(self, n: int) -> int:
        lb = 1
        ub = n

        while lb <= ub:
            mid = lb + (ub - lb) // 2

            left_sum = (1 + mid) * (mid // 2) + \
                (mid - (mid//2) if mid % 2 != 0 else 0)
            right_sum = (mid + n) * ((n - mid + 1) // 2) + \
                ((n - (n-mid+1) // 2) if (n-mid+1) % 2 != 0 else 0)

            if left_sum == right_sum:
                return mid

            if left_sum > right_sum:
                ub = mid - 1
            else:
                lb = mid + 1
        return -1

    # Time: O(N), Space: O(1)
    def pivotIntegerV2(self, n: int) -> int:
        left_sum = 1
        right_sum = (n * (n + 1)) // 2
        pivot = 1

        while pivot <= n:
            if left_sum == right_sum:
                return pivot

            right_sum = right_sum - pivot
            pivot = pivot + 1
            left_sum = left_sum + pivot

        return - 1


print(Solution().pivotInteger(8))
print(Solution().pivotInteger(1))
print(Solution().pivotInteger(4))


print(Solution().pivotIntegerV2(8))
print(Solution().pivotIntegerV2(1))
print(Solution().pivotIntegerV2(4))
