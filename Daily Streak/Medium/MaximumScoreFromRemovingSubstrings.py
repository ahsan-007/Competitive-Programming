# https://leetcode.com/problems/maximum-score-from-removing-substrings/description /?envType=daily-question&envId=2024-07-12

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def findCount(s, substr):
            count = 0
            i = 0
            while i < len(s) - 1:
                if s[i:i+2] == substr:
                    count = count + 1
                    s = s[:i] + s[i+2:]
                    i = i - 1
                else:
                    i = i + 1
            return s, count

        s, count = findCount(s, "ab" if x > y else "ba")
        maxGain = count * max(x, y)
        s, count = findCount(s, "ab" if x < y else "ba")
        return maxGain + count * min(x, y)


print(Solution().maximumGain(s="cdbcbbaaabab", x=4, y=5))
print(Solution().maximumGain(s="aabbaaxybbaabb", x=5, y=4))
