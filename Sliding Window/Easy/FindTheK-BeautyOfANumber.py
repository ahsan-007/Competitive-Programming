# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numStr = str(num)
        i = 0
        kBeauty = 0
        while i + k <= len(numStr):
            divisor = int(numStr[i:i+k])
            if divisor != 0 and num % int(divisor) == 0:
                kBeauty = kBeauty + 1

            i = i + 1
        return kBeauty


print(Solution().divisorSubstrings(num=240, k=2))
print(Solution().divisorSubstrings(num=430043, k=2))
