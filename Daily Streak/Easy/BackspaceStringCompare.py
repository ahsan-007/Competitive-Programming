# https://leetcode.com/problems/backspace-string-compare/description/?envType=daily-question&envId=2023-10-19

class Solution:
    # Time: O(MAX(M, N))
    # Space: O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        b1 = b2 = 0
        while i >= 0 or j >= 0:
            if (i < 0 or s[i] != '#') and (j < 0 or t[j] != '#'):
                if b1 == 0 and b2 == 0:
                    print(i, j)
                    if i < 0 or j < 0 or s[i] != t[j]:
                        return False
                    i = i - 1
                    j = j - 1
                else:
                    if b1 > 0:
                        b1 = b1 - 1
                        i = i - 1

                    if b2 > 0:
                        b2 = b2 - 1
                        j = j - 1
            else:
                if i >= 0 and s[i] == '#':
                    b1 = b1 + 1
                    i = i - 1

                if j >= 0 and t[j] == '#':
                    b2 = b2 + 1
                    j = j - 1

        return i < 0 and j < 0


print(Solution().backspaceCompare(s="ab#c", t="ad#c"))
print(Solution().backspaceCompare(s="ab##", t="c#d#"))
print(Solution().backspaceCompare(s="a#c", t="b"))
print(Solution().backspaceCompare(s="xywrrmp", t="xywrrmu#p"))
print(Solution().backspaceCompare(s="", t="a#b#c#"))
