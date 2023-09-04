# https://leetcode.com/problems/counting-bits/?envType=daily-question&envId=2023-09-01

from typing import List


class Solution:
	def countBits(self, n: int) -> List[int]:
		bits = [0]
		for i in range(1, n + 1):
			bits.append(bits[i // 2] + (i % 2))
		return bits


print(Solution().countBits(n=2))
print(Solution().countBits(n=5))
print(Solution().countBits(n=15))
