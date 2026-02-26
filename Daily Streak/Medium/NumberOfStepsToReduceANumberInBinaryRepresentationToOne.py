# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description /?envType=daily-question&envId=2024-05-29

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        while len(s) != 1:
            if s[-1] == '0':
                s = s[:-1]
            else:
                i = len(s) - 1
                while i >= 0 and s[i] == '1':
                    i = i - 1

                s = (s[:i] if i > 0 else "") + "1" + ("0" * (len(s) - i - 1))
            steps = steps + 1
        return steps

    def numStepsV2(self, s: str) -> int:
        i = len(s) - 1
        steps = 0
        carry = 0
        while i > 0:
            digit = int(s[i]) + carry
            if digit % 2 == 0:
                steps += 1
            else:
                steps += 2
                carry = 1
            i = i - 1
        return steps + carry

    def numStepsV3(self, s: str) -> int:
        num = int(s, 2)
        steps = 0
        while num > 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num + 1
            steps = steps + 1
        return steps


print(Solution().numSteps(s="1101"))
print(Solution().numSteps(s="10"))
print(Solution().numSteps(s="1"))

print('-'*100)

print(Solution().numStepsV2(s="1101"))
print(Solution().numStepsV2(s="10"))
print(Solution().numStepsV2(s="1"))

print('-'*100)

print(Solution().numStepsV3(s="1101"))
print(Solution().numStepsV3(s="10"))
print(Solution().numStepsV3(s="1"))
