# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2024-01-03

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        lasers = 0
        for row in bank:
            cnt = row.count("1")
            if cnt > 0:
                if lasers > 0:
                    beams = beams + lasers * cnt
                lasers = cnt
        return beams


print(Solution().numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
print(Solution().numberOfBeams(bank=["000", "111", "000"]))
