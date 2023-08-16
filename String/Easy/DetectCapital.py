# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = word[0].isupper() and len(
            word) > 1 and word[1].isupper()
        for i in range(len(word)):
            if upper and not word[i].isupper():
                return False
            elif not upper and word[i].isupper() and i != 0:
                return False
        return True


print(Solution().detectCapitalUse('Science'))
print(Solution().detectCapitalUse('SCIENCE'))
print(Solution().detectCapitalUse('science'))
print(Solution().detectCapitalUse('sC'))
print(Solution().detectCapitalUse('sciEncE'))
