# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/?envType=daily-question&envId=2026-03-03

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def getSn(i):
            if i == 1:
                return "0"

            s = getSn(i-1)
            return s + "1" + "".join("0" if ch == "1" else "1" for ch in s)[::-1]

        return getSn(n)[k-1]


print(Solution().findKthBit(n=3, k=1))
print(Solution().findKthBit(n=4, k=11))
