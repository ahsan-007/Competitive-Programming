from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for i in range(len(code))]

        elif k > 0:
            windowStart = (len(code) + k-1) % len(code)
            windowEnd = 0
            runningSum = sum([code[i]
                             for i in range(windowEnd, windowStart+1)])
            decrypted = [0] * len(code)
            for i in range(len(code)-1, -1, -1):
                decrypted[i] = runningSum
                runningSum = runningSum - code[windowStart]
                windowStart = (windowStart - 1) % len(code)
                windowEnd = (windowEnd - 1) % len(code)
                runningSum = runningSum + code[windowEnd]

        else:
            windowStart = len(code) - abs(k)
            windowEnd = len(code) - 1
            runningSum = sum([code[i]
                             for i in range(windowStart, windowEnd+1)])
            decrypted = [0] * len(code)
            for i in range(len(code)):
                decrypted[i] = runningSum
                runningSum = runningSum - code[windowStart]

                windowEnd = (windowEnd + 1) % len(code)
                windowStart = (windowStart + 1) % len(code)

                runningSum = runningSum + code[windowEnd]

        return decrypted


print(Solution().decrypt(code=[5, 7, 1, 4], k=3))
print(Solution().decrypt(code=[1, 2, 3, 4], k=0))
print(Solution().decrypt(code=[2, 4, 9, 3], k=-2))
