# https://leetcode.com/problems/build-an-array-with-stack-operations/description/?envType=daily-question&envId=2023-11-03

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        current_element_in_stream = 1
        irrelevant_pushes = 0
        i = 0
        while i < len(target):
            if target[i] == current_element_in_stream:
                while irrelevant_pushes > 0:
                    operations.append("Pop")
                    irrelevant_pushes = irrelevant_pushes - 1
                operations.append("Push")
                i = i + 1

            elif target[i] > current_element_in_stream:
                operations.append("Push")
                irrelevant_pushes = irrelevant_pushes + 1
            current_element_in_stream = current_element_in_stream + 1
        return operations


print(Solution().buildArray(target=[1, 3], n=3))
print(Solution().buildArray(target=[1, 2, 3], n=3))
print(Solution().buildArray(target=[1, 2], n=4))
