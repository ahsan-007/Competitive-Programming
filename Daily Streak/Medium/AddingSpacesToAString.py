# https://leetcode.com/problems/adding-spaces-to-a-string/description /?envType=daily-question&envId=2024-12-03

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sWithSpacing = [' '] * (len(s) + len(spaces))
        stringIndex = 0
        spaceIndex = 0
        for i in range(len(sWithSpacing)):
            # as each space is added, an offset should be added to next spaceIndex because
            # the string shifted right by 1 so index is 1 more character further than it should be
            # offset=1 when 1 space is added
            # offset=2 when 2 spaces are added
            # offset=n when n spaces are added
            # an offset variable can be used by intializing it to 0 and incrementing it each time
            # a space is added, but we can also reuse spaceIndex as it is also being incremented
            # each time a space is added
            if spaceIndex < len(spaces) and i == spaces[spaceIndex] + spaceIndex:
                spaceIndex = spaceIndex + 1
            else:
                sWithSpacing[i] = s[stringIndex]
                stringIndex = stringIndex + 1
        return ''.join(sWithSpacing)


print(Solution().addSpaces(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15]))
print(Solution().addSpaces(s="icodeinpython", spaces=[1, 5, 7, 9]))
print(Solution().addSpaces(s="spacing", spaces=[0, 1, 2, 3, 4, 5, 6]))
