# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/?envType=daily-question&envId=2026-03-06

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        oneSeen = False
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                if not oneSeen:
                    oneSeen = True
            elif s[i] == '0' and oneSeen:
                return False
        return True

    def checkOnesSegmentV2(self, s: str) -> bool:
        return "01" not in s


print(Solution().checkOnesSegment(s="1001"))
print(Solution().checkOnesSegment(s="110"))
print(Solution().checkOnesSegment(s="1"))

print('-'*100)

print(Solution().checkOnesSegmentV2(s="1001"))
print(Solution().checkOnesSegmentV2(s="110"))
print(Solution().checkOnesSegmentV2(s="1"))
