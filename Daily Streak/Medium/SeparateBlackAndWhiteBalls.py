# https://leetcode.com/problems/separate-black-and-white-balls/description /?envType=daily-question&envId=2024-10-15

class Solution:
    def minimumSteps(self, s: str) -> int:
        blackBalls = 0
        swaps = 0
        for ch in s:
            if ch == '1':
                blackBalls = blackBalls + 1
            else:
                swaps = swaps + blackBalls
        return swaps


print(Solution().minimumSteps(s="101"))
print(Solution().minimumSteps(s="100"))
print(Solution().minimumSteps(s="0111"))
