# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description /?envType=daily-question&envId=2025-01-14

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        elementsOfA = set()
        elementsOfB = set()
        prefixCommonArray = [0] * len(A)
        for i in range(len(A)):
            elementsOfA.add(A[i])
            elementsOfB.add(B[i])

            # at i == 0, instead of add i - 1 index of prefixCommonArray
            # 0 should be added, but as at i == 0, i - 1 is -1
            # which will access the last element of prefixCommonArray
            # which is 0, therefore, an additional condition is not needed
            # to explicitly add 0 when i == 0
            prefixCommonArray[i] = (prefixCommonArray[i - 1] +
                                    (1 if A[i] in elementsOfB else 0) +
                                    (1 if B[i] in elementsOfA and A[i] != B[i] else 0))

        return prefixCommonArray


print(Solution().findThePrefixCommonArray(A=[1, 3, 2, 4], B=[3, 1, 2, 4]))
print(Solution().findThePrefixCommonArray(A=[2, 3, 1], B=[3, 1, 2]))
