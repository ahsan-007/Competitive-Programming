# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsMap = {}
        for ch in jewels:
            jewelsMap[ch] = True

        jewelsInStonres = 0
        for ch in stones:
            if ch in jewelsMap:
                jewelsInStonres = jewelsInStonres + 1
        return jewelsInStonres


print(Solution().numJewelsInStones('aA', 'aAAbbbb'))
print(Solution().numJewelsInStones('z', 'ZZ'))
