# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description/?envType=daily-question&envId=2026-03-29

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1[0] == s2[0]:
            if s1[1] == s2[1]:
                if s1[2] == s2[2]:
                    if s1[3] == s2[3]:
                        return True
            elif s1[1] == s2[3] and s1[3] == s2[1]:
                if s1[2] == s2[2]:
                    return True
        else:
            if s1[0] == s2[2] and s1[2] == s2[0]:
                if s1[1] == s2[1]:
                    if s1[3] == s2[3]:
                        return True
                else:
                    if s1[1] == s2[3] and s1[3] == s2[1]:
                        return True
        return False


print(Solution().canBeEqual(s1="abcd", s2="cdab"))
print(Solution().canBeEqual(s1="abcd", s2="dacb"))
print(Solution().canBeEqual(s1="bnxw", s2="bwxn"))
