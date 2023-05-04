# https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        i = 0
        while i < len(senate):
            senator = senate[i]
            if senator != 'x':
                senate = self.removeRights(
                    senate, i, 'D' if senate[i] == 'R' else 'R')
                if senate is None:
                    return 'Radiant' if senator == 'R' else 'Dire'
            i = (i + 1) % len(senate)

    def removeRights(self, senate: str, i, senator):
        j = (i + 1) % len(senate)
        while j != i:
            if senate[j] == senator:
                senate = senate[:j]+'x'+senate[j+1:]
                return senate
            j = (j + 1) % len(senate)
        return None


print(Solution().predictPartyVictory('RD'))
print(Solution().predictPartyVictory('RDD'))
print(Solution().predictPartyVictory('RRR'))
print(Solution().predictPartyVictory('DDRRR'))
print(Solution().predictPartyVictory('DRRDDR'))
print(Solution().predictPartyVictory('DRRDRDRDRDDRDRDR'))
