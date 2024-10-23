# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description /?envType=daily-question&envId=2024-10-21

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def maxUniqueSplitUtil(s, seen):
            if not s:
                return 0

            i = 0
            maxSplit = 0
            while i < len(s):
                if s[:i+1] not in seen:
                    seen.add(s[:i+1])
                    uniqueSplit = maxUniqueSplitUtil(s[i+1:], seen)
                    if uniqueSplit is not None:
                        maxSplit = max(maxSplit, uniqueSplit + 1)
                    seen.remove(s[:i+1])
                i = i + 1
            return maxSplit

        seen = set()
        return maxUniqueSplitUtil(s, seen)


print(Solution().maxUniqueSplit("ababccc"))
print(Solution().maxUniqueSplit("aba"))
print(Solution().maxUniqueSplit("aa"))
print(Solution().maxUniqueSplit("ababcdcdabefabce"))
