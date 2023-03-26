# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

from typing import List


class Solution:
    # Time: O(N ^ 2)
    def minOperations(self, boxes: str) -> List[int]:
        i = 0
        operations = []
        while i < len(boxes):
            j = 0
            op = 0
            while j < len(boxes):
                if boxes[j] == '1':
                    op = op + abs(j - i)
                j = j + 1
            operations.append(op)
            i = i + 1
        return operations

    # Time O(N)
    def minOperationsV2(self, boxes: str) -> List[int]:
        ans = [0]

        count = cost = 0
        for i in range(1, len(boxes)):
            if boxes[i - 1] == '1':
                count = count + 1
            cost = cost + count
            ans.append(cost)

        count = cost = 0
        for i in range(len(boxes) - 2, -1, -1):
            if boxes[i + 1] == '1':
                count = count + 1
            cost = cost + count
            ans[i] = ans[i] + cost

        return ans


print(Solution().minOperations(boxes="110"))
print(Solution().minOperations(boxes="001011"))

print(Solution().minOperationsV2(boxes="110"))
print(Solution().minOperationsV2(boxes="001011"))
