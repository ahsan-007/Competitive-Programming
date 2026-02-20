# https://leetcode.com/problems/special-binary-string/description/?envType=daily-question&envId=2026-02-20

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def getMountains(s):
            counter = 0
            start = 0
            mountains = []
            for i in range(len(s)):
                if s[i] == '1':
                    counter += 1
                else:
                    counter -= 1

                if counter == 0:
                    mountains.append(s[start:i + 1])
                    start = i + 1
            return mountains

        mountains = getMountains(s)
        if not mountains:
            return ""

        newMountains = []
        for mountain in mountains:
            currSpecialMountain = self.makeLargestSpecial(mountain[1:-1])
            if currSpecialMountain:
                newMountains.append('1' + currSpecialMountain + '0')
            else:
                newMountains.append(mountain)

        newMountains.sort(reverse=True)
        return "".join(newMountains)

    def makeLargestSpecialV2(self, s: str) -> str:
        count = 0
        startInd = 0
        speicalSubstrings = []
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1

            if count == 0:
                speicalSubstrings.append(
                    '1' + self.makeLargestSpecial(s[startInd + 1: i]) + '0')
                count = 0
                startInd = i + 1

        speicalSubstrings.sort(reverse=True)
        return "".join(speicalSubstrings)


print(Solution().makeLargestSpecial(s="11011000"))
print(Solution().makeLargestSpecial(s="101100"))
print(Solution().makeLargestSpecial(s="10"))
print(Solution().makeLargestSpecial(s="10110111000011100100"))
print(Solution().makeLargestSpecial(s="11100100"))

print('-'*100)

print(Solution().makeLargestSpecialV2(s="11011000"))
print(Solution().makeLargestSpecialV2(s="101100"))
print(Solution().makeLargestSpecialV2(s="10"))
print(Solution().makeLargestSpecialV2(s="10110111000011100100"))
print(Solution().makeLargestSpecialV2(s="11100100"))
