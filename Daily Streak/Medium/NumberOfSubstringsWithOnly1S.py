# https://leetcode.com/problems/number-of-substrings-with-only-1s/description /?envType=daily-question&envId=2025-11-16

import math


class Solution:
    def numSub(self, s: str) -> int:
        numberOfSubstrings = 0
        ones = 0
        for ch in s:
            if ch == '1':
                ones += 1
            elif ones > 0:
                numberOfSubstrings += (ones * (ones + 1)) // 2
                ones = 0

        if ones > 0:
            numberOfSubstrings += (ones * (ones + 1)) // 2

        return int(numberOfSubstrings % (math.pow(10, 9) + 7))

    def numSubV2(self, s: str) -> int:
        numberOfSubstrings = 0
        ones = 0
        for ch in s:
            if ch == '1':
                ones += 1
                numberOfSubstrings += ones
            elif ones > 0:
                ones = 0

        return int(numberOfSubstrings % (math.pow(10, 9) + 7))

    def numSubV3(self, s: str) -> int:
        return int(sum((len(t) * (len(t)+1)) // 2 for t in s.split("0") if t) % (math.pow(10, 9) + 7))


print(Solution().numSub(s="0110111"))
print(Solution().numSub(s="101"))
print(Solution().numSub(s="111111"))

print('-'*30)

print(Solution().numSubV2(s="0110111"))
print(Solution().numSubV2(s="101"))
print(Solution().numSubV2(s="111111"))

print('-'*30)

print(Solution().numSubV3(s="0110111"))
print(Solution().numSubV3(s="101"))
print(Solution().numSubV3(s="111111"))
