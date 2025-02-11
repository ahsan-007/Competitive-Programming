# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/?envType=daily-question&envId=2025-02-11


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        start_ind = 0
        while start_ind != -1:
            start_ind = s.find(part)
            if start_ind != -1:
                s = s[:start_ind] + s[start_ind + len(part):]
        return s


print(Solution().removeOccurrences(s="daabcbaabcbc", part="abc"))
print(Solution().removeOccurrences(s="axxxxyyyyb", part="xy"))
