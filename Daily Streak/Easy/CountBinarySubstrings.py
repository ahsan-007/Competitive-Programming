# https://leetcode.com/problems/count-binary-substrings/description/?envType=daily-question&envId=2026-02-19

class Solution:
    # Time: O(N) (list append has amortized O(1) time complexity), Space: O(N)
    def countBinarySubstrings(self, s: str) -> int:
        frequency = []
        count = 0
        char = ''
        for ch in s:
            if ch != char:
                if count > 0:
                    frequency.append((char, count))
                count = 1
                char = ch
            else:
                count = count + 1

        if count > 0:
            frequency.append((char, count))

        substringCount = 0
        for i in range(1, len(frequency)):
            substringCount = substringCount + \
                min(frequency[i-1][1], frequency[i][1])
        return substringCount

    # Time: O(N), Space: O(1)
    def countBinarySubstringsV2(self, s: str) -> int:
        zeroCount = 0
        oneCount = 0
        i = 0
        substringCount = 0
        for i in range(len(s)):
            if i > 0 and s[i-1] != s[i]:
                if zeroCount > 0 and oneCount > 0:
                    substringCount += min(zeroCount, oneCount)

                    if s[i] == '0':
                        zeroCount = 0
                    else:
                        oneCount = 0

            if s[i] == '0':
                zeroCount += 1
            else:
                oneCount += 1

        return substringCount + min(zeroCount, oneCount)


print(Solution().countBinarySubstrings(s="00110011"))
print(Solution().countBinarySubstrings(s="10101"))
print(Solution().countBinarySubstrings(s="000000"))

print('-'*100)

print(Solution().countBinarySubstringsV2(s="00110011"))
print(Solution().countBinarySubstringsV2(s="10101"))
print(Solution().countBinarySubstringsV2(s="000000"))
