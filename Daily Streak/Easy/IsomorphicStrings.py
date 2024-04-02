# https://leetcode.com/problems/isomorphic-strings/description/?envType=daily-question&envId=2024-04-02

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sChars = {}
        tChars = {}
        for i in range(len(s)):
            if sChars.get(s[i], t[i]) != t[i]:
                return False

            if tChars.get(t[i], s[i]) != s[i]:
                return False

            if s[i] not in sChars:
                sChars[s[i]] = t[i]
                tChars[t[i]] = s[i]
        return True

    def isIsomorphicV2(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


print(Solution().isIsomorphic(s="egg", t="add"))
print(Solution().isIsomorphic(s="foo", t="bar"))
print(Solution().isIsomorphic(s="paper", t="title"))

print('-'*100)

print(Solution().isIsomorphicV2(s="egg", t="add"))
print(Solution().isIsomorphicV2(s="foo", t="bar"))
print(Solution().isIsomorphicV2(s="paper", t="title"))
