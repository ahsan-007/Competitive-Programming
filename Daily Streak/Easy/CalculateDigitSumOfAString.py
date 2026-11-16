# https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/?envType=daily-question&envId=2026-11-16

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            newS = ""
            i = 0
            while i < len(s):
                newS += str(sum((int(ch) for ch in s[i:i+k])))
                i = i + k
            s = newS
        return s

print(Solution().digitSum(s = "11111222223", k = 3))
print(Solution().digitSum(s = "00000000", k = 3))