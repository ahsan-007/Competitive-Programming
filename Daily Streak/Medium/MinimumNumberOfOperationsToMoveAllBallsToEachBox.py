# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description /?envType=daily-question&envId=2025-01-06


from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        updatedBoxes = [0] * len(boxes)

        def minOperationsUtil(i, left_moves, leftOnes):
            if i >= len(boxes):
                return 0, 0

            right_moves, rightOnes = minOperationsUtil(
                i + 1, left_moves + leftOnes, leftOnes + int(boxes[i]))
            updatedBoxes[i] = left_moves + leftOnes + right_moves + rightOnes
            return right_moves + rightOnes, rightOnes + int(boxes[i])

        minOperationsUtil(0, 0, 0)
        return updatedBoxes


print(Solution().minOperations(boxes="110"))
print(Solution().minOperations(boxes="001011"))
