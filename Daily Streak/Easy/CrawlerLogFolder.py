# https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        class DNode:
            def __init__(self, val, prev=None, next=None) -> None:
                self.val = val
                self.prev = prev
                self.next = next

        currentFolder = DNode('Main')
        for log in logs:
            if log[0] == '.':
                if log[1] == '.':
                    if currentFolder.prev is not None:
                        currentFolder = currentFolder.prev
            else:
                currentFolder.next = DNode(log[:-1], prev=currentFolder)
                currentFolder = currentFolder.next

        minOperations = 0
        while currentFolder.prev is not None:
            currentFolder = currentFolder.prev
            minOperations += 1
        return minOperations

    def minOperationsV2(self, logs: List[str]) -> int:
        folderDepth = 0
        for log in logs:
            if log[0] == ".":
                if log[1] == "." and folderDepth != 0:
                    folderDepth = folderDepth - 1
            else:
                folderDepth = folderDepth + 1
        return folderDepth


print(Solution().minOperations(logs=["d1/", "d2/", "../", "d21/", "./"]))
print(Solution().minOperations(logs=["d1/", "../", "../", "../"]))
print(Solution().minOperations(
    logs=["d1/", "d2/", "./", "d3/", "../", "d31/"]))


print(Solution().minOperationsV2(logs=["d1/", "d2/", "../", "d21/", "./"]))
print(Solution().minOperationsV2(logs=["d1/", "../", "../", "../"]))
print(Solution().minOperationsV2(
    logs=["d1/", "d2/", "./", "d3/", "../", "d31/"]))
