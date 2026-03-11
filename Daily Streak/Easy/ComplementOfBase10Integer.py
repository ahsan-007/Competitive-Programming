# https://leetcode.com/problems/complement-of-base-10-integer/description/?envType=daily-question&envId=2026-03-11

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int("".join("1" if ch == "0" else "0" for ch in bin(n)[2:]), 2)


print(Solution().bitwiseComplement(n=5))
print(Solution().bitwiseComplement(n=7))
print(Solution().bitwiseComplement(n=10))
