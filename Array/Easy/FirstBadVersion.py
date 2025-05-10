# https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        def firstBadVersionUtil(i, j):
            if i == j:
                return i if isBadVersion(i) else -1

            mid = i + (j - i) // 2
            isMidBad = isBadVersion(mid)
            if isMidBad and (mid == 0 or not isBadVersion(mid-1)):
                return mid

            elif isMidBad:
                return firstBadVersionUtil(i, mid - 1)

            else:
                return firstBadVersionUtil(mid + 1, j)

        return firstBadVersionUtil(1, n)
