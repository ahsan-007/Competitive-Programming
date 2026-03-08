# https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2026-03-08

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        for i in range(pow(2, len(nums))):
            binary = bin(i)[2:].zfill(len(nums))
            if binary not in nums:
                return binary

    # Cantor's Diagonal Argument
    def findDifferentBinaryStringV2(self, nums: List[str]) -> str:
        differentBinary = ""
        for i in range(len(nums)):
            differentBinary += "1" if nums[i][i] == "0" else "0"
        return differentBinary

    # Cantor's Diagonal Argument (one liner)
    def findDifferentBinaryStringV3(self, nums: List[str]) -> str:
        return "".join("1" if nums[i][i] == "0" else "0" for i in range(len(nums)))


print(Solution().findDifferentBinaryString(nums=["01", "10"]))
print(Solution().findDifferentBinaryString(nums=["111", "011", "001"]))
print(Solution().findDifferentBinaryString(nums=["00", "01"]))

print('-' * 100)

print(Solution().findDifferentBinaryStringV2(nums=["01", "10"]))
print(Solution().findDifferentBinaryStringV2(nums=["111", "011", "001"]))
print(Solution().findDifferentBinaryStringV2(nums=["00", "01"]))

print('-' * 100)

print(Solution().findDifferentBinaryStringV3(nums=["01", "10"]))
print(Solution().findDifferentBinaryStringV3(nums=["111", "011", "001"]))
print(Solution().findDifferentBinaryStringV3(nums=["00", "01"]))
